import cv2 as cv
import numpy as np

#########################################################################
# ملاحظة: يرجى تنفيذ كل طلب على حدى حتى لا يتم تطبيق جميع النتائج على نفس الصورة

##############################################################################


image = cv.imread('C:\\Users\\CEC\\Desktop\\image.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 70, 250, apertureSize=3)
lines = cv.HoughLines(edges, 1, np.pi/180, 200)
for r_theta in lines:
	arr = np.array(r_theta[0], dtype=np.float64)
	r, theta = arr
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a*r
	y0 = b*r
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv.imshow("linesDetected", image)
cv.waitKey()
######################################################################################

edges = cv.Canny(gray, 60, 220, apertureSize=3)
linesP = cv.HoughLinesP(edges, 1, np.pi / 180, 50, None, 50, 10)
if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(image, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
cv.imshow("linesDetected Probabilistic Transform", image)   
cv.waitKey()