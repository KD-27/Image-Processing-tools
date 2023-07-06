import cv2

img = cv2.imread('images/laser_cut.jpg')
gblur = cv2.GaussianBlur(img , (9,9), 0)


def canny_edge_detection(threshold1, threshold2):
    gray = cv2.cvtColor(gblur, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1, threshold2)
    cv2.imshow('Canny Edge Detection', edges)


cv2.namedWindow('Canny Edge Detection')
cv2.createTrackbar('Threshold 1', 'Canny Edge Detection', 0, 255, lambda x: None)
cv2.createTrackbar('Threshold 2', 'Canny Edge Detection', 0, 255, lambda x: None)

while True:
    threshold1 = cv2.getTrackbarPos('Threshold 1', 'Canny Edge Detection')
    threshold2 = cv2.getTrackbarPos('Threshold 2', 'Canny Edge Detection')
    canny_edge_detection(threshold1, threshold2)
    if cv2.waitKey(1) == 13:
        break

cv2.destroyAllWindows()
print(threshold1)
print(threshold2)
