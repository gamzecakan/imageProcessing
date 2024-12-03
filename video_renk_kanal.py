import cv2 as cv
import numpy as np


#üzerinde işlem yapılacak girşi ve çıkış videoları
input_video=("images/araba_video.mp4")
output_video=("images/araba_output.mp4")

#video yakalama
cap=cv.VideoCapture(input_video)

#video özelliklerine bak
fourcc=cv.VideoWriter_fourcc(*'mp4v') #Kodek yani video içeriğini çözmemizi sağlar ki görüntü olsun
"""
kodeği de yükseklik ve genişlik gibi otomatik olarak alabiliz aslında
kodek = cap.get(cv.CAP_PROP_FOURCC) fonksiyonunu kullanabliriz...
bir video kodeği bir video dosyasını sıkıştırmak ve sonra onu çözmek için kullanılan yazılım aracı
"""
fps=int(cap.get(cv.CAP_PROP_FPS)) #saniyedeki frame sayısı yani bir snd e kaç görüntü->fps
width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH))#genislik
height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))#yukseklik

#videomuzu belirtilen özelliklerde oluşturalım
out=cv.VideoWriter(output_video,fourcc,fps,(width,height)) 

"""
burada ret okumanın başarılı olup olmadığını
frame ise kare verisini içerir
"""
while cap.isOpened(): #video kaynağı açık old. sürece döngü devam eder
    ret,frame=cap.read()
    
    if not ret: #okuma başarısız ise döngüyü bitircez
        break
    
    #renk kanallarını ayarlayalım
    b,g,r=cv.split(frame)
    
    rgb_frame=cv.merge((r,g,b))
    cv.imshow("Mavi video",rgb_frame)
    
    rgb_frame2=cv.merge((b,r,r))
    cv.imshow("Sari video",rgb_frame2)
    
    out.write(rgb_frame)#videoya yaz
    if cv.waitKey(1) & 0xFF == ord("q"): #q tuşuna basıldığında
        break
    
cap.release()
out.release()
cv.destroyAllWindows()