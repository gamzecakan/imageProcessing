import cv2 as cv

resim_dosyası="images\satranc3x3.jpg"
elma="images\yesilElma.jpg"

"""
cv.IMREAD_COLOR kullanmak daha iyidir, çünkü bu şekilde kodunuz daha anlaşılır hale gelir. 
cv.IMREAD_COLOR ifadesi, imread fonksiyonunun resmi renkli olarak yüklemek için ayarlandığını doğrudan ifade eder. 
Başka bir geliştirici (veya siz kendiniz) kodu okurken parametrenin amacını hemen anlayabilir.
1 parametresini kullanmak ise daha kısa olabilir, ancak 1 sayısının anlamını bilmeyen birinin kodu anlamasını zorlaştırabilir. 
Bu tür sayılar, programlamada "sihirli sayılar" olarak bilinir ve kod okunabilirliğini azaltır.
Bu nedenle, genel olarak tavsiye edilen yaklaşım cv.IMREAD_COLOR gibi açıklayıcı sabitleri kullanmaktır.
"""

"""
RENKLİ OLARAK BASTIRMAK İÇİN
"""
# img_color=cv.imread(resim_dosyası,cv.IMREAD_COLOR) 
img_color=cv.imread(resim_dosyası,1) #şuan bu daha kısa old. için bunu kullandık

cv.imshow("Renkli", img_color)
cv.waitKey(0) #0 yazıyorsak herhangi bir tuşu bekle demiş oluyoruz ama misal (1000)yazsaydık 1sn bekleyecek sonra kapanacaktı
cv.destroyAllWindows() #tüm pencereli kapat

"""
SİYAH & BEYAZ OLARAK BASTIRMAK İÇİN
"""
# img_gray=cv.imread(resim_dosyası,cv.IMREAD_GRAYSCALE)
img_gray=cv.imread(elma,0)
cv.imshow("Siyah&Beyaz", img_gray)
cv.waitKey(0)
cv.destroyAllWindows()