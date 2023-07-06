import cv2
import numpy as np

img = cv2.imread('images/colours.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def nothing(x):
    pass


cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)


while True:

    # read values from the trackbars
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    # lower and upper bounds for color detection
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    # create an image mask
    mask = cv2.inRange(hsv, l_b, u_b)

    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("result", result)
    if cv2.waitKey(1) == 13:
        break
cv2.destroyAllWindows()
print(l_b)
print(u_b)
