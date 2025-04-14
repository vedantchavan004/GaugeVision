from ultralytics import YOLO
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image

# === Load image ===
image_path = "valve3.png"
img = cv2.imread(image_path)

# === Run YOLOv8-pose inference ===
model = YOLO('best.pt')
results = model(img, save=False)

# === Extract keypoints ===
try:
    kpts_tensor = results[0].keypoints.xy[0]
    max_pt, min_pt, center_pt, tip_pt = [pt.cpu().numpy() for pt in kpts_tensor]
except Exception as e:
    print("❌ Error extracting keypoints:", e)
    exit()

# === Detect and decode QR Code ===
detector = cv2.QRCodeDetector()
data, bbox, _ = detector.detectAndDecode(img)

if data:    
    # Draw QR bounding box
    if bbox is not None:
        bbox = bbox.astype(int)
        for i in range(len(bbox[0])):
            pt1 = tuple(bbox[0][i])
            pt2 = tuple(bbox[0][(i + 1) % len(bbox[0])])
            cv2.line(img, pt1, pt2, color=(0, 255, 0), thickness=2)

        cv2.putText(img, data, (bbox[0][0][0], bbox[0][0][1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
else:
    print("⚠️ No QR Code found.")

# === Visualization ===
plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax = plt.gca()

# Keypoint labels
colors = ['black', 'lime']  # center, tip
points = [center_pt, tip_pt]

for i, (x, y) in enumerate(points):
    ax.plot(x, y, 'o', color=colors[i], markersize=8)

# Draw line (needle)
ax.plot([center_pt[0], tip_pt[0]], [center_pt[1], tip_pt[1]],
        color='cyan', linewidth=2, label='needle')

plt.axis("off")
plt.legend()
plt.show()
