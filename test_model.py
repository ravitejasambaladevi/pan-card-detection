from ultralytics import YOLO

model = YOLO("runs/detect/train7/weights/best.pt")

model.predict(
    source="pan_aadhar.jpg",
    show=True,
    save=True
)