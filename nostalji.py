import cv2 as cv
import numpy as np
import gradio as gr

"""
Bu fonksiyon, verilen resmi gri tonlamalı hale dönüştürüyor.
Resim verisi bir numpy dizisi olarak alınıyor ve 
cv2.cvtColor ile gri tonlamalı hale getiriliyor.
COLORBGR2GRAY bgr yi gray e çevir yani
"""

def nostalji(image):
    image = np.array(image)
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return gray_image


"""
gr.Blocks() Kullanıcının bir resim yükleyebileceği 
ve bu resmi siyah-beyaza dönüştürebileceği arayüz oluşturuluyor.
"""
with gr.Blocks() as demo:
    gr.Markdown("Görseli siyah beyaza çevir")  #bunlar siteye başlık olarak geliyor
    gr.Markdown("Bir resim yükleyin ve siyah beyaza çevrilsin")

    image_input = gr.Image(type='pil')
    image_output = gr.Image(type="numpy", label="Sonuç Resmi")

    # fonksiyonu gradio bileşenlerine bağla
    image_input.change(nostalji, inputs=image_input, outputs=image_output)

# Gradio arayüzünü başlat
if __name__ == "__main__":
    demo.launch(share=True)
    # demo.launch(share=True)
