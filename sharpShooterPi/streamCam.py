import cv2

vc = cv2.VideoCapture(0)

while True:
	ret, frame = vc.read()

	if not frame:
		break

	cv2.imshow("Test", frame)
