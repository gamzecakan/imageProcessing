import cv2 as cv

img=cv.imread("images\kirmizi_ferrari.jpg")

img_siyah_beyaz=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

b,g,r=cv.split(img)

img_mavi=cv.merge((r,g,b))

img_yesil=cv.merge((g,r,b))

img_turkuaz=cv.merge((r,r,b))

img_pembe=cv.merge((r,g,r))

cv.imshow("orijinal ferrari",img)
cv.imshow("mavi ferrari", img_mavi)
cv.imshow("yesil ferrari", img_yesil)
cv.imshow("turkuaz ferrari", img_turkuaz)
cv.imshow("pembe ferrari", img_pembe)
cv.imshow("siyah&beyaz",img_siyah_beyaz)
cv.waitKey(0)
cv.destroyAllWindows()