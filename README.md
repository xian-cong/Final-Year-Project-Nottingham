# WellnessAI+
## Overview of the Project
WellnessAI+ is an intelligent wearable device equipped with electrocardiogram (**ECG**) and advanced **AI** capabilities to offer a groundbreaking approach to **edge computing** to not only **predict heart disease** but also delve into the depths of **human emotions**. In this era of smart wearables, the integration of ECG with AI technology holds the potential to revolutionize the way we understand, monitor, and manage both our physical and emotional well-being. This dual-purpose capability signifies a pivotal leap forward in personalised healthcare and wellness management, ushering in a new era of preventative and predictive medicine.

### Demo
[![demo](https://youtu.be/qq1fBSTt8C8)](https://youtu.be/qq1fBSTt8C8)

### Features
- **ECG Monitoring**: The ECG sensor is used to measure the electrical activity of the heart and display the ECG waveform on the screen. The ECG waveform is also sent to the cloud for further analysis.
- **Heart Disease Prediction**: The ECG waveform is sent to the cloud for further analysis. The cloud will then predict the possibility of heart disease based on the ECG waveform.
- **Emotion Recognition**: The ECG waveform is sent to the edge for further analysis. The edge will then predict the real-time emotion of the user based on the ECG waveform.

### Design
| Front | Back | Inside | Side |
| :------: | :------: | :------: | :------: |
|<div style="text-align:center"><img src="3d%20model\pic\Front.png" alt="front" width="100%" height="100%"></div> | <div style="text-align:center"><img src="3d%20model\pic\back.png" alt="front" width="40%" height="100%"></div> | <div style="text-align:center"><img src="3d%20model\pic\Inside+screen.png" alt="front" width="40%" height="30%"></div> | <div style="text-align:center"><img src="3d%20model\pic\Side_1.png" alt="front" width="40%" height="30%"></div> 

### Tools and Technologies Used
![Block Diagram](links%20and%20documents/block%20diagram/WellnessAI+%20Block%20Diagram%20Architecture_updated.png)

## System Requirements
### Hardware
- STM32MP157F-DK2
- ECG Measurement Kit

### Software
- STM32CubeIDE
- Ubuntu 20.04 LTS
- Python

## Getting Started
### Clone Project
```
git clone https://github.com/xian-cong/Final-Year-Project-Nottingham.git
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Run the Program
```
conda activate fyp_venv
python3 main.py
```

### Hardware Setup
<div style="text-align:center"><img src="img/Hardware%20connections.png" alt="Hardware Setup" width="50%" height="50%"></div>

## Time Management
### Gantt Chart
![Gantt Chart](links%20and%20documents/gantt%20chart/Gantt%20Chart_3-1.png)

## Project Documentation
### Project Outline and Planning Report
[Project Proposal](links%20and%20documents/project%20outline%20and%20planning%20report/Project%20Outline%20and%20Planning%20Report.pdf)

### Project Specification
[Project Report](links%20and%20documents/FYP%20Project%20Specification.pdf)