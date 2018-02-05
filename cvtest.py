import cv2;

print("--------- Test OpenCV ---------");
src =cv2.imread(r'E:\project\o\feret\1-1.bmp');
cv2.namedWindow("input image",cv2.WINDOW_AUTOSIZE);
cv2.imshow("input image",src);

cv2.waitKey(0);
cv2.destroyAllWindows();
print("--------- End Test ---------");