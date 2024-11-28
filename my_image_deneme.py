import cv2 as cv

import numpy as np
import os

# Görüntüyü yükle
image_path = "images\comlek.jpg"
image = cv.imread(image_path)

scale_percent = 50  # %50 küçültme
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
resized_image = cv.resize(image, (width, height), interpolation=cv.INTER_AREA)

# Yazının bulunduğu alanı seçmek (koordinatları ayarlayın)
# Yeni boyutlara göre koordinatlar yeniden hesaplanır
x, y, w, h = int(200 * scale_percent / 100), int(100 * scale_percent / 100), int(300 * scale_percent / 100), int(100 * scale_percent / 100)

# Yazının bulunduğu alanı bulanıklaştırma veya çevreye benzetme
roi = resized_image[y:y+h, x:x+w]
method = "blur"  # "blur" (bulanıklaştır) veya "inpaint" (çevreyle doldur) seçeneği
if method == "blur":
    blurred_roi = cv.GaussianBlur(roi, (35, 35), 0)
    resized_image[y:y+h, x:x+w] = blurred_roi
elif method == "inpaint":
    mask = np.zeros(resized_image.shape[:2], dtype=np.uint8)
    mask[y:y+h, x:x+w] = 255
    resized_image = cv.inpaint(resized_image, mask, 3, cv.INPAINT_TELEA)

# Sonucu kaydet ve görüntüle
output_path = "images\cleaned_image.jpg"
cv.imwrite(output_path, resized_image)
cv.imshow("Result", resized_image)
cv.waitKey(0)
cv.destroyAllWindows()