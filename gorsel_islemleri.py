import cv2 as cv

#imread yani görseli oku olarak düşün görseli bir sayı dizisine çeviriyor
#opencv bgr olarak alıyor
img=cv.imread("images\satranc3x3.jpg")
print(img)
#print(img[300:400, :]) yaparsan renkli kısımların vs de pixel bgr lerini görebilrisin.sonuçta bu bi pixel matrisi

#sayı dizisiin tekrar görsel olarak gösterelim
cv.imshow("satranc 3x3 @TechIst", img)


#herhangi bi işlem yapılmazsa biz göremeden görseli açıp kapatıyor olacağından bekle ve klavyede bir tuşa basıldığında çık yapıcaz
cv.waitKey(0)
cv.destroyAllWindows() #tüm pencereleri kapat