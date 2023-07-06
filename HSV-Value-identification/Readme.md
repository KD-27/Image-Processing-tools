1. Import the necessary libraries: `cv2` for OpenCV and `numpy` for numerical operations.

2. Read an image called "colours.jpg" using `cv2.imread()` and store it in the variable `img`.

3. Convert the image from BGR color space to HSV color space using `cv2.cvtColor()` and store it in the variable `hsv`.

4. Define a function called `nothing()` which does nothing. This function will be used as a callback for the trackbars.

5. Create a named window called "Tracking" using `cv2.namedWindow()`.

6. Create trackbars using `cv2.createTrackbar()` to adjust the lower and upper HSV values for color detection. The trackbars are for adjusting the lower hue (LH), lower saturation (LS), lower value (LV), upper hue (UH), upper saturation (US), and upper value (UV).

7. Enter a while loop to continuously process the image and update the trackbar values.

8. Inside the loop, read the current values of the trackbars using `cv2.getTrackbarPos()` and store them in variables.

9. Define the lower and upper bounds for color detection using `np.array()` based on the trackbar values.

10. Create a binary image mask using `cv2.inRange()` to extract the pixels within the specified color range.

11. Apply the mask to the original image using `cv2.bitwise_and()` to obtain the result of color filtering.

12. Display the resulting image using `cv2.imshow()`.

13. If the Enter key (key code 13) is pressed, break out of the while loop and exit the program.

14. Destroy all created windows using `cv2.destroyAllWindows()`.

15. Print the final lower and upper HSV values for color detection.

IMPORTANT

* locate the image file in a folder named "images".
* This folder must be placed in the same directory of this code
