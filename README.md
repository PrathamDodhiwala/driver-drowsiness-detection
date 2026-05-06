# 🚗 Driver Drowsiness Detection System

A real-time **Driver Drowsiness Detection Web App** built using **Python, OpenCV, MediaPipe, and Streamlit**.
This application monitors a driver’s eye movements through a webcam and detects drowsiness based on eye closure using the **Eye Aspect Ratio (EAR)**.

If the system detects prolonged eye closure, it triggers a **visual and audio alert** to prevent accidents.


## 🚀 Features

* 🎥 Real-time webcam monitoring
* 👁️ Eye tracking using MediaPipe Face Mesh
* 📉 Eye Aspect Ratio (EAR) calculation
* ⚠️ Drowsiness detection with alert system
* 🔊 Audio alarm for warnings
* 🌐 Interactive Streamlit UI
* ▶️ Start / Stop detection controls
* 📊 Live EAR monitoring
* 🔢 Drowsiness frame counter


## 🛠️ Tech Stack

* Python 🐍
* Streamlit 🎨
* OpenCV 📷
* MediaPipe 🤖
* NumPy 🔢
* Playsound 🔊


## 📂 Project Structure

```
driver-drowsiness-detection/
│── enhanced_drowsiness_ui.py   # Main Streamlit app
│── alarm.wav                   # Alert sound file
│── requirements.txt            # Dependencies
│── README.md                   # Documentation
```


## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/driver-drowsiness-detection.git
cd driver-drowsiness-detection
```


### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

Or install manually:

```
pip install streamlit opencv-python mediapipe numpy playsound
```


### 3️⃣ Add alarm sound

* Place an audio file named **alarm.wav** in the project folder
* This will be used for drowsiness alerts


### 4️⃣ Run the application

```
streamlit run enhanced_drowsiness_ui.py
```


## 🧠 How It Works

1. Captures live video from webcam
2. Detects face landmarks using **MediaPipe Face Mesh**
3. Extracts eye coordinates
4. Calculates **Eye Aspect Ratio (EAR)**
5. Monitors EAR over consecutive frames
6. If EAR falls below threshold for a set duration:

   * ⚠️ Displays alert on screen
   * 🔊 Plays alarm sound


## 📊 Key Parameters

* **EAR Threshold**: `0.25`
* **Consecutive Frames Threshold**: `15`

These values can be tuned for better sensitivity.


## 🖥️ UI Overview

* Live webcam feed
* Start / Stop buttons
* Real-time EAR value
* Drowsiness counter
* Alert status display


## 📈 Future Improvements

* 📊 Add live EAR graph visualization
* 🧠 Use deep learning models for better accuracy
* 📱 Mobile compatibility
* ☁️ Deploy on cloud platforms
* 🚘 Integrate with IoT/vehicle systems


## ⚠️ Limitations

* Works best in good lighting conditions
* Requires a functional webcam
* Accuracy may vary based on face visibility and angle


## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request


## 📜 License

This project is open-source and available under the **MIT License**.


## 👨‍💻 Author

Pratham Dodhiwala
GitHub: https://github.com/PrathamDodhiwala

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub!

