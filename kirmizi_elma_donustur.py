#kırmızı rengi yeşil yapıcaz
import cv2 as cv

image=cv.imread("images\kirmizi_elma.jpg")

#orijinal elmayı göster
cv.imshow("kirmizi elma",image)

#bu zaten bir pixel dizisi ya parçalayabiliriz yani
b,g,r=cv.split(image)

#kırmızı ve yeşil kanalları birleştir
image_new=cv.merge((b,r,g))#normalde b-g-r idi ya green ile red i yer değiştirdim.

image_blue=cv.merge((r,g,b))#zevkine maviye dönüştürdüm
cv.imshow("mavi elma",image_blue)
          
#yeşil elmayı göster
cv.imshow("Yesil Elma",image_new)

cv.waitKey(0)
cv.destroyAllWindows()
