import cv2 as cv

#resmi oku
img=cv.imread("images\yesilElma.jpg")

#goruntunun boyutlarını alalım (yuksellik ve genislik)
#shape bir touple döndürür burada bir yukseklik bir genişlik ve bir de renk kodları bgr şeklinde 3 olduğu için
#(yukseklik,genisşlik,3) şeklinde gösterir. 3'e gerek yok :2 ye kadar yazdırsın diyorum.

height,width=img.shape[:2]
channels=img.shape[2]  #görüntünğn kanal sayısı 0 1 2
print("yukseklik: ",height,"genislik: ",width)

print(f'Görüntü yüksekliği:{img.shape[0]}')
print(f'Görüntü genişliği: {img.shape[1]}')
print(f'Görüntünün kanal sayısı: {channels}')
print(f'Veri Tipi: {img.dtype}')

#isteğe bağlı
cv.imshow("Yesil Elma",img) #penceerenin açıklaması, görüntülenecek resmin kod
cv.waitKey(0)
cv.destroyAllWindows()




