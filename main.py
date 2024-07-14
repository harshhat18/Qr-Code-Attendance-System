import cv2
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
import numpy as np

# Path to the QR code image
img_path = r"./sample1.jpeg"

# Read the image
img = cv2.imread(img_path)

# Decode the QR codes in the image
qr_info = decode(img)

# Check if any QR code was detected
if qr_info:
    for qr in qr_info:
        data = qr.data  # Data contained in the QR code
        rect = qr.rect  # Bounding box of the QR code
        polygon = qr.polygon  # Polygon vertices of the QR code

        # Print the data, rect, and polygon information
        print("Data:", data)
        print("Rect:", rect)
        print("Polygon:", polygon)

        # Draw a rectangle around the QR code
        img = cv2.rectangle(
            img,
            (rect.left, rect.top),
            (rect.left + rect.width, rect.top + rect.height),
            (0, 255, 0),  # Green color
            5,  # Thickness
        )

        # Convert polygon vertices to numpy array and reshape
        pts = np.array(polygon, np.int32)
        pts = pts.reshape((-1, 1, 2))

        # Draw a polygon around the QR code
        img = cv2.polylines(
            img,
            [pts],
            True,  # Closed polygon
            (255, 0, 0),  # Blue color
            5,  # Thickness
        )

    # Display the image with the drawn shapes
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
else:
    print("No QR code detected")
