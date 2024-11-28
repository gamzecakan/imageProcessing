import cv2 as cv
import numpy as np
import gradio as gr

# Bu fonksiyon, verilen resmi gri tonlamalı hale dönüştürüyor.
def nostalji(image):
    image = np.array(image)  # Resmi numpy dizisine dönüştür
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # Gri tonlamaya çevir
    return gray_image

# Gradio arayüzü oluşturma
with gr.Blocks() as demo:
    gr.Markdown("## Görseli Siyah Beyaza Çevir")  # Başlık ekleyin
    gr.Markdown("Bir resim yükleyin ve gri tonlamalı hale getirilsin.")  # Açıklama

    # Giriş ve çıkış bileşenlerini tanımlayın
    image_input = gr.Image(type='pil', label="Giriş Resmi")
    image_output = gr.Image(type="numpy", label="Sonuç Resmi")

    # Gradio arayüzüne işlevi bağlayın
    submit_button = gr.Button("Dönüştür")  # Buton ekleyin
    cv.waitKey(4000)
    submit_button.click(nostalji, inputs=image_input, outputs=image_output)

# Gradio arayüzünü başlat
if __name__ == "__main__":
    demo.launch(share=True)
