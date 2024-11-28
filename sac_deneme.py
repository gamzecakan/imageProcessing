import cv2 as cv

img=cv.imread("images\kizil_sac.jpg")

b,g,r=cv.split(img)

img_mavi=cv.merge((r,g,b))


#sarı saç yapıcaz
img_sari=cv.merge((b,r,r))

cv.imshow('orijinal sac',img)
cv.imshow('mavi sac',img_mavi)
cv.imshow('sari sac',img_sari)
cv.waitKey(0)
cv.destroyAllWindows()