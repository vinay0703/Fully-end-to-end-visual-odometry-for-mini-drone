# Visual-Inertial Odometry for DJI Tello Minidrone
[![Python3](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org/)
[![Tensorflow](https://img.shields.io/badge/Python3-Tensorflow-green.svg)](https://www.tensorflow.org/)
[![MATLAB](https://img.shields.io/badge/MATLAB-SIMULINK-blue.svg)](https://www.mathworks.com/help/simulink/)

### Project Motivation
Using an airborne vehicle to explore an inside environment is a burgeoning topic, whether for equipment maintenance or greenhouse monitoring. Indoor aerial vehicles may play a key role in situations when human access is impossible. However, driving an aerial vehicle in an interior environment is difficult, particularly because the GPS sensor cannot provide positional information. This is where odometry might be useful; it aids in estimating the change in location by analyzing the change in sensor readings. Using sensor data such as an Inertial Measurement Unit (IMU), camera, etc., the approach estimates the change in position as the vehicle travels through space.


### Project Description
Design a visual-inertial odometry system for a tiny aerial vehicle using MATLAB and Simulink. 
Utilize the downward-facing camera on the DJI Tello Minidrone in conjunction with the 6-axis IMU data to construct the method that will enhance state estimates and replace the presently employed optical flow modeling approach.

### Simulation
Used MATLAB Simulink Educational along with Python-Tensorflow to create scenario and train the RCNN model.

### Libraries
The following Libraries have been used.
```
djitellopy==2.4.0
et-xmlfile==1.1.0
numpy==1.23.4
opencv-contrib-python==4.6.0.66
opencv-python==4.6.0.66
openpyxl==3.0.10
pandas==1.5.1
pygame==2.1.2
python-dateutil==2.8.2
pytz==2022.6
six==1.16.0
```

### Installation
Below is an example of how you can instruct your audience on installing and setting up.
```
1. Fork the repository and pull it into your local machine.
2. Install all the required packages by simply typing 
        "pip3 install -r requirements.txt"
   in the terminal opened inside the root folder.
```


### Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.
If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star!
Thanks again!


### Authors
- [@vinay0703](https://github.com/vinay0703)
- [@utkarsh-vats-2000](https://github.com/Utkarsh-Vats-2000)
