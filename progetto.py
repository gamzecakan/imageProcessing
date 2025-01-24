import cv2 as cv

# Görseli yükle
image = cv.imread("images/image.png")

if image is None:
    print("Resim yüklenemedi. Lütfen dosya yolunu kontrol edin.")
else:
    print("Resim başarıyla yüklendi!")

# Yatay dolguyu hesapla (sol ve sağ boşluklar)
desired_width = 1920  # İstediğiniz genişlik
desired_height = 432
current_width = image.shape[1]
padding = (desired_width - current_width) // 2

# Kenar tekrarı ile dolgu ekle
padded_image = cv.copyMakeBorder(image, 0, 0, padding, padding, cv.BORDER_REPLICATE)

# Yeni resmi kaydet
cv.imwrite("images/padded_image5.png", padded_image)
print("Düzenlenmiş resim kaydedildi!")
