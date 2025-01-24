#kırmızı rengi yeşil yapıcaz
import cv2 as cv

image=cv.imread("images\contact.png")

#orijinal elmayı göster
cv.imshow("orijinal",image)

#bu zaten bir pixel dizisi ya parçalayabiliriz yani
b,g,r=cv.split(image)

#kırmızı ve yeşil kanalları birleştir
image_new=cv.merge((r,r,b))#normalde b-g-r idi ya green ile red i yer değiştirdim.
          
#yeşil elmayı göster
cv.imshow("Kirmizi hali",image_new)

cv.imwrite("images\contact.png",image_new)
cv.waitKey(0)
cv.destroyAllWindows()
