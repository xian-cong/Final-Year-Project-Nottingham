import serial
import streamlit as st
import plotly.graph_objects as go

# Open the serial port
ser = serial.Serial('COM5', 115200)  # Change 'COM5' to your COM port and 9600 to your baud rate

# Streamlit UI
st.title('Real-Time ECG Sensor Data Visualization')

# Create plotly chart
chart = st.plotly_chart(go.Figure())

# Initialize variables for prediction, model confidence, and duration
ecg_values = []  # Define ecg_values as a global variable
prediction_text = st.empty()
confidence_text_0 = st.empty()
confidence_text_1 = st.empty()
duration_text = st.empty()

# Function to parse the serial data
def parse_serial_data(data):
    global ecg_values
    data = data.decode().strip()
    # print("Received data:", data)  # Debugging statement
    if data.startswith("Running inference"):
        confidence_line_0 = ser.readline().decode().strip()
        confidence_line_1 = ser.readline().decode().strip()
        prediction_line = ser.readline().decode().strip()
        duration_line = ser.readline().decode().strip()
        
        confidence_0 = float(confidence_line_0.split(':')[-1].strip())
        confidence_1 = float(confidence_line_1.split(':')[-1].strip())
        prediction_info = prediction_line.split(':')
        prediction = int(prediction_info[1].split('-')[0].strip())
        duration = int(duration_line.split(':')[-1].strip())
        
        # Update the Streamlit UI with inference results
        if prediction == 1:
            prediction_text.text("Prediction: stress")
        else:
            prediction_text.text("Prediction: non-stress")
        confidence_text_0.text("Model Confidence 0: {:.6f}".format(confidence_0))
        confidence_text_1.text("Model Confidence 1: {:.6f}".format(confidence_1))
        duration_text.text("Duration: {} ms".format(duration))
        
    elif '.' in data:  # Check if the data contains a decimal point
        try:
            ecg_values.append(float(data))
            if len(ecg_values) >= 500:
                # Update the chart with new ECG data and clear the stored data
                chart.plotly_chart(go.Figure())
                ecg_values.clear()
            else:
                # Update the chart with new ECG data
                chart.plotly_chart(go.Figure(data=[go.Scatter(x=list(range(len(ecg_values))), y=ecg_values, mode='lines', name='ECG Sensor ADC Value')]))
            # print("Chart updated.")  # Debugging statement
        except ValueError:
            pass  # Ignore if the data cannot be converted to float
    else:
        pass  # Ignore other cases

# Function to continuously read data from serial and update the graph
def update_graph():
    try:
        while True:
            line = ser.readline()
            parse_serial_data(line)
    except KeyboardInterrupt:
        ser.close()

# Run the update graph function
update_graph()
