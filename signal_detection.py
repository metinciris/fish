import cv2
import numpy as np
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import ImageFont, ImageDraw, Image

# Resim seçme fonksiyonu
def select_image():
    Tk().withdraw()  # Tkinter pencereyi gizler
    image_path = askopenfilename(title="Bir resim seçin", filetypes=[("Image files", "*.jpeg;*.jpg;*.png;*.bmp")])
    return image_path

# RGB renk kodlarını BGR formatına çevirme fonksiyonu
def hex_to_bgr(hex_color):
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return (rgb[2], rgb[1], rgb[0])  # BGR formatına çevirme

# Kırmızı ve yeşil renkler için hedef tonlar (BGR formatında)
her2_target_colors = [
    hex_to_bgr('#EF2848'),  # HER2 sinyalleri için kırmızı tonları
    hex_to_bgr('#FA1C49'),
    hex_to_bgr('#C0203E'),
    hex_to_bgr('#E91D49')
]

cep17_target_colors = [
    hex_to_bgr('#47B03B'),  # CEP17 sinyalleri için yeşil tonları
    hex_to_bgr('#3E8E3E'),
    hex_to_bgr('#68AB40'),
    hex_to_bgr('#42FF3A'),
    hex_to_bgr('#55D74A')
]

# Resmi yükleme
image_path = select_image()
if not image_path:
    print("Resim seçilmedi.")
else:
    image = cv2.imread(image_path)
    
    # Dosya ismini ve dizinini ayırma
    image_dir, image_filename = os.path.split(image_path)
    image_name, image_ext = os.path.splitext(image_filename)

    # Maske oluşturma
    her2_mask = np.zeros(image.shape[:2], dtype="uint8")  # Başlangıçta boş bir HER2 maske
    cep17_mask = np.zeros(image.shape[:2], dtype="uint8")  # Başlangıçta boş bir CEP17 maske

    # HER2 tonları için maske oluşturma
    for target_color in her2_target_colors:
        lower_bound = np.array([max(0, c - 30) for c in target_color], dtype="uint8")  # Alt sınır
        upper_bound = np.array([min(255, c + 30) for c in target_color], dtype="uint8")  # Üst sınır
        mask = cv2.inRange(image, lower_bound, upper_bound)
        her2_mask = cv2.bitwise_or(her2_mask, mask)  # Maskeleri birleştir

    # CEP17 tonları için maske oluşturma
    for target_color in cep17_target_colors:
        lower_bound = np.array([max(0, c - 30) for c in target_color], dtype="uint8")  # Alt sınır
        upper_bound = np.array([min(255, c + 30) for c in target_color], dtype="uint8")  # Üst sınır
        mask = cv2.inRange(image, lower_bound, upper_bound)
        cep17_mask = cv2.bitwise_or(cep17_mask, mask)  # Maskeleri birleştir

    # HER2 sinyallerinin yerlerini bulma
    her2_contours, _ = cv2.findContours(her2_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    her2_signal_count = 0
    for cnt in her2_contours:
        area = cv2.contourArea(cnt)
        if area > 5:  # Gürültüyü önlemek için minimum alan kontrolü
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.circle(image, (x + w // 2, y + h // 2), 1, (0, 255, 255), -1)  # Sarı 1 piksel nokta (HER2 için)
            her2_signal_count += 1

    # CEP17 sinyallerinin yerlerini bulma
    cep17_contours, _ = cv2.findContours(cep17_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cep17_signal_count = 0
    for cnt in cep17_contours:
        area = cv2.contourArea(cnt)
        if area > 5:  # Gürültüyü önlemek için minimum alan kontrolü
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.circle(image, (x + w // 2, y + h // 2), 1, (255, 0, 0), -1)  # Mavi 1 piksel nokta (CEP17 için)
            cep17_signal_count += 1

    # Oran hesaplama
    if cep17_signal_count > 0:
        ratio = her2_signal_count / cep17_signal_count
    else:
        ratio = 0

    # Grup belirleme
    if ratio >= 2.0 and her2_signal_count >= 4.0:
        group = "Grup 1: HER2/CEP17 oranı ≥ 2.0; ≥ 4.0 HER2 sinyali/hücre"
    elif ratio >= 2.0 and her2_signal_count < 4.0:
        group = "Grup 2: HER2/CEP17 oranı ≥ 2.0; < 4.0 HER2 sinyali/hücre"
    elif ratio < 2.0 and her2_signal_count >= 6.0:
        group = "Grup 3: HER2/CEP17 oranı < 2.0; ≥ 6.0 HER2 sinyali/hücre"
    elif ratio < 2.0 and 4.0 <= her2_signal_count < 6.0:
        group = "Grup 4: HER2/CEP17 oranı < 2.0; ≥ 4.0 ve < 6.0 HER2 sinyali/hücre"
    else:
        group = "Grup 5: HER2/CEP17 oranı < 2.0; < 4.0 HER2 sinyali/hücre"

    # Görüntüyü Pillow ile işlemek
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image_pil)
    font = ImageFont.truetype("arial.ttf", 20)  # Türkçe karakter desteği için Arial yazı tipi

    # Metinlerin üst üste binmemesi için konumları ayarlayın
    text_padding = 30

    # Sonuçları görüntüye yazdırma
    draw.text((10, image.shape[0] - 4 * text_padding), f'HER2 Sinyal: {her2_signal_count}', font=font, fill=(0, 255, 0))
    draw.text((10, image.shape[0] - 3 * text_padding), f'CEP17 Sinyal: {cep17_signal_count}', font=font, fill=(0, 255, 0))
    draw.text((10, image.shape[0] - 2 * text_padding), f'Oran (HER2/CEP17): {ratio:.2f}', font=font, fill=(0, 255, 0))
    draw.text((10, image.shape[0] - text_padding), group, font=font, fill=(0, 255, 0))

    # PIL görüntüsünü OpenCV formatına çevir
    image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)

    # Sonuçları yazdırma
    print(f"Hücre başına HER2 sinyal sayısı: {her2_signal_count}")
    print(f"Hücre başına CEP17 sinyal sayısı: {cep17_signal_count}")
    print(f"Hücre başına HER2/CEP17 oranı: {ratio:.2f}")
    print(f"Grup: {group}")

    # Yeni dosya ismi oluşturma
    output_image_path = os.path.join(image_dir, f"{image_name}_count_output{image_ext}")

    # Resmi dosya olarak kaydetme
    cv2.imwrite(output_image_path, image)
    print(f"İşlenmiş görüntü kaydedildi: {output_image_path}")
