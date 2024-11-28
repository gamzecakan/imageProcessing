import cv2 as cv


img=cv.imread("images\satranc3x3.jpg")

b, g, r=cv.split(img)

img_mavi=cv.merge((r,g,b))

cv.imshow("mavi_satranc",img_mavi)

"""
bunu kaydetmek istiyoruzzz bunun için imwrite kullanucaz
"""

cv.imwrite("images\mavi_satranc.jpg" , img_mavi)

#Kanalları böyle tekli şekilde gösterebilrisin
cv.imshow("satranc",img)
cv.imshow("blue kanali",b)
cv.imshow("green kanali",g)
cv.imshow("red kanali",r)

cv.waitKey(0)
cv.destroyAllWindows()