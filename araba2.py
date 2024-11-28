import cv2 as cv

img=cv.imread("images\kirmizi_togg.jpg")

b,g,r=cv.split(img)

img_blue=cv.merge((r,g,b))

img_green=cv.merge((g,r,b))

img_pink=cv.merge((r,g,r))

img_turkuaz=cv.merge((r,r,b))

img_siyahbeyaz=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("orijinal hali", img)
cv.imshow("mavi",img_blue)
cv.imshow("green",img_green)
cv.imshow("pink",img_pink)
cv.imshow("turkuaz",img_turkuaz)
cv.imshow("nostaljik",img_siyahbeyaz)

cv.waitKey(0)
cv.destroyAllWindows()