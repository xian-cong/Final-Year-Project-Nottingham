import serial
import streamlit as st
import plotly.graph_objects as go

# Open the serial port
ser = serial.Serial('COM5', 115200)  # Change 'COM5' to your COM port and 9600 to your baud rate

# Streamlit UI
st.title('Real-Time ECG Sensor Data Visualization')

# Create placeholders for inference results
prediction_placeholder = st.empty()
confidence_placeholder = st.empty()
duration_placeholder = st.empty()

# Create plotly chart
chart = st.plotly_chart(go.Figure())

# Initialize lists to store data
ecg_values = []
model_confidence = []
predictions = []
durations = []
inputs_count = 0

# Function to parse the serial data
def parse_serial_data(data):
    global ecg_values, model_confidence, predictions, durations, inputs_count
    data = data.decode().strip()
    print("Received data:", data)  # Debugging statement
    if data.startswith("Prediction"):
        parts = data.split(':')
        prediction_info = parts[1].split('-')
        predictions.append(int(prediction_info[0].strip()))
        model_confidence.append(float(prediction_info[1].split()[0].strip()))
        durations.append(int(prediction_info[2].split()[0].strip()))
        
        # Update inference results
        prediction_placeholder.write("Prediction: {}".format(predictions[-1]))
        confidence_placeholder.write("Model Confidence: {:.2f}".format(model_confidence[-1]))
        duration_placeholder.write("Duration: {} ms".format(durations[-1]))
        
    elif '.' in data:  # Check if the data contains a decimal point
        try:
            ecg_values.append(float(data))
            inputs_count += 1
            if inputs_count >= 500:
                inputs_count = 0
                # Update the chart with new ECG data and clear the stored data
                chart.plotly_chart(go.Figure())
                ecg_values = []
                model_confidence = []
                predictions = []
                durations = []
            else:
                # Update the chart with new ECG data
                chart.plotly_chart(go.Figure(data=[go.Scatter(x=list(range(len(ecg_values))), y=ecg_values, mode='lines', name='ECG Sensor ADC Value')]))
            print("Chart updated.")  # Debugging statement
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
