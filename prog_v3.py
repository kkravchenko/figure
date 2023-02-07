import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

class figes:
	def __init__(self, image):
        	self.image = image

    def findfige(self):
		img = cv2.imread(self.image)

		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
		contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		i = 0
		for contour in contours:
			if i == 0:
				i = 1
				continue

			approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
	
			M = cv2.moments(contour)
			if M['m00'] != 0.0:
				x = int(M['m10']/M['m00'])
				y = int(M['m01']/M['m00'])

			if len(approx) == 3:
				print('Треугольник')

			elif len(approx) == 4:
				print('Квадрат')

			elif len(approx) > 5:
				print('Многоугольник')

			else:
				print('Круг')

			break


if sys.argv[1]:
	img = sys.argv[1]
	f = figes(img)
	f.findfige()
else:
	raise Exception('Incorrect data')


