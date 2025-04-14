
# GaugeVision 🔧📷

**GaugeVision** is a computer vision-based tool that combines **YOLOv11-pose estimation** and **QR code recognition** to extract pressure readings from analog gauges while identifying the gauge through an embedded QR code.

---

## 📌 Features

- 🧠 **YOLOv8 Pose Estimation**: Detects four keypoints (min, max, center, tip) on the analog gauge.
- 🔍 **QR Code Recognition**: Extracts QR data using OpenCV's built-in QRCodeDetector.
- 📐 **Needle Visualization**: Displays the direction of the needle using pose keypoints.
- 🖼️ **Overlay Output**: Visualizes keypoints, needle, and QR bounding boxes.

---

## 🖼️ Demo

![output](https://github.com/user-attachments/assets/ac41bea7-2105-47bc-b975-e62a096e88ea)


---

## 🛠️ Requirements

Install the necessary dependencies:

```bash
pip install ultralytics opencv-python matplotlib pillow numpy
```

Ensure you have:
- `valve3.png` - test image containing an analog gauge and QR code
- `best.pt` - a trained YOLOv8-pose model suitable for gauge keypoints

---

## 🚀 How to Run

1. Clone the repository or copy the files into your project folder.
2. Ensure the following files are in the same directory:
   - `gauge_qr_reader.py`
   - `valve3.png`
   - `best.pt`
3. Run the script:

```bash
python gauge_qr_reader.py
```

---

## 📁 Project Structure

```
.
├── best.pt                  # Trained YOLOv8 pose model for gauge keypoints
├── valve3.png               # Input test image
├── gauge_qr_reader.py       # Main script with pose and QR detection
└── README.md                # Project documentation
```

---

## 📚 How It Works

1. Load the input image.
2. Detect keypoints using YOLOv8-pose model (min, max, center, tip).
3. Detect and decode QR code using OpenCV.
4. Draw:
   - Center and tip keypoints
   - Needle direction
   - QR bounding box and text
5. Display the final result using Matplotlib.

---

## ✅ Sample Output

```bash
✅ QR Code Data: -1 6 2.5 4.3
```

Visual output shows:
- Center and tip marked
- Cyan line representing the needle
- Green box around the QR code with the data displayed

---

## 🔮 Future Plans

- [ ] Add pressure estimation from needle angle
- [ ] Export results (QR + pressure) to CSV

---

