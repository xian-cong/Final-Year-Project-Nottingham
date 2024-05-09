import serial
import streamlit as st
import plotly.graph_objects as go

st.title('Real-Time ECG Emotion Classification')
st.sidebar.title('Settings')

# User input for baud rate and serial port in the sidebar
baud_rate = st.sidebar.number_input('Enter Baud Rate', min_value=9600, max_value=115200, value=115200, step=9600)
serial_port = st.sidebar.selectbox('Select Serial Port', options=['COM5', 'COM1', 'COM2', 'COM3', 'COM4'])

# Open the serial port
ser = serial.Serial(serial_port, baud_rate)

main_container = st.container()

chart = st.plotly_chart(go.Figure(), use_container_width=True)

ecg_values = []  # Define ecg_values as a global variable
prediction_text = st.metric(label="Prediction", value="", delta=None)
confidence_0_text = st.metric(label="Model Confidence 0", value="", delta=None)
confidence_1_text = st.metric(label="Model Confidence 1", value="", delta=None)
duration_text = st.metric(label="Duration (ms)", value="", delta=None)

def parse_serial_data(data):
    global ecg_values
    data = data.decode().strip()
    if data.startswith("Running inference"):
        confidence_line_0 = ser.readline().decode().strip()
        confidence_line_1 = ser.readline().decode().strip()
        prediction_line = ser.readline().decode().strip()
        duration_line = ser.readline().decode().strip()

        confidence_0 = float(confidence_line_0.split(':')[-1].strip())
        confidence_1 = float(confidence_line_1.split(':')[-1].strip())
        prediction_info = prediction_line.split(':')[-1].split('-')
        prediction = int(prediction_info[0].strip()) if prediction_info[0].strip() != "Sensor Detached" else "Sensor Detached"
        duration = float(duration_line.split(':')[-1].strip())

        prediction_text.metric(label="Prediction", value="stress" if prediction == 1 else "non-stress" if prediction == 0 else prediction, delta=None)
        confidence_0_text.metric(label="Model Confidence (Non-stress)", value=confidence_0, delta=None)
        confidence_1_text.metric(label="Model Confidence (Stress)", value=confidence_1, delta=None)
        duration_text.metric(label="Duration (ms)", value=duration, delta=None)

    elif '.' in data:  # Check if the data contains a decimal point
        try:
            ecg_values.append(float(data))
            if len(ecg_values) >= 500:
                chart.plotly_chart(go.Figure(), use_container_width=True)
                ecg_values.clear()
            else:
                # Update the chart with new ECG data
                chart.plotly_chart(go.Figure(data=[go.Scatter(x=list(range(len(ecg_values))), y=ecg_values, mode='lines', name='ECG Sensor ADC Value')]), use_container_width=True)
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

update_graph()