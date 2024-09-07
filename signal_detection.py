import cv2
import numpy as np
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

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
red_target_colors = [
    hex_to_bgr('#EF2848'),  # Kırmızı tonları
    hex_to_bgr('#FA1C49'),
    hex_to_bgr('#C0203E'),
    hex_to_bgr('#E91D49'),
    hex_to_bgr('#971B38'),
    hex_to_bgr('#971E57'),
    hex_to_bgr('#9D1C39')
]

# Yeni yeşil tonlar eklendi
green_target_colors = [
    hex_to_bgr('#47B03B'),  # Yeşil tonları
    hex_to_bgr('#3E8E3E'),
    hex_to_bgr('#68AB40'),
    hex_to_bgr('#42FF3A'),
    hex_to_bgr('#55D74A'),
    hex_to_bgr('#496152'),
    hex_to_bgr('#C7F589'),  # Yeni yeşil tonları
    hex_to_bgr('#A3F471'),
    hex_to_bgr('#9EE76B')
]

# Gereksiz kırmızı renkler (ortası ışıklı olmayanlar)
excluded_red_colors = [
    hex_to_bgr('#782141'), 
    hex_to_bgr('#7F2738'),
    hex_to_bgr('#721F49'),  # Eklenen gereksiz kırmızı tonlar
    hex_to_bgr('#7E204C'),
    hex_to_bgr('#70203E')
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
    red_mask = np.zeros(image.shape[:2], dtype="uint8")  # Başlangıçta boş bir kırmızı maske
    green_mask = np.zeros(image.shape[:2], dtype="uint8")  # Başlangıçta boş bir yeşil maske

    # Kırmızı tonları için maske oluşturma (gereksiz tonları hariç tutma)
    for target_color in red_target_colors:
        if target_color not in excluded_red_colors:
            lower_bound = np.array([max(0, c - 30) for c in target_color], dtype="uint8")  # Alt sınır
            upper_bound = np.array([min(255, c + 30) for c in target_color], dtype="uint8")  # Üst sınır
            mask = cv2.inRange(image, lower_bound, upper_bound)
            red_mask = cv2.bitwise_or(red_mask, mask)  # Maskeleri birleştir

    # Yeşil tonları için maske oluşturma (yeni tonlar dahil)
    for target_color in green_target_colors:
        lower_bound = np.array([max(0, c - 30) for c in target_color], dtype="uint8")  # Alt sınır
        upper_bound = np.array([min(255, c + 30) for c in target_color], dtype="uint8")  # Üst sınır
        mask = cv2.inRange(image, lower_bound, upper_bound)
        green_mask = cv2.bitwise_or(green_mask, mask)  # Maskeleri birleştir

    # Kırmızı sinyallerin yerlerini bulma
    red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    red_signal_count = 0
    for cnt in red_contours:
        area = cv2.contourArea(cnt)
        if area > 5:  # Gürültüyü önlemek için minimum alan kontrolü
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.circle(image, (x + w // 2, y + h // 2), 1, (0, 255, 255), -1)  # Sarı 1 piksel nokta (Kırmızı için)
            red_signal_count += 1

    # Yeşil sinyallerin yerlerini bulma
    green_contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    green_signal_count = 0
    for cnt in green_contours:
        area = cv2.contourArea(cnt)
        if area > 5:  # Gürültüyü önlemek için minimum alan kontrolü
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.circle(image, (x + w // 2, y + h // 2), 1, (255, 0, 0), -1)  # Mavi 1 piksel nokta (Yeşil için)
            green_signal_count += 1

    # Oran hesaplama
    if green_signal_count > 0:
        ratio = red_signal_count / green_signal_count
    else:
        ratio = 0

    # Sonuçları görüntüye yazdırma
    image_height = image.shape[0]
    cv2.putText(image, f'Kirmizi Sinyal: {red_signal_count}', (10, image_height - 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.putText(image, f'Yesil Sinyal: {green_signal_count}', (10, image_height - 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.putText(image, f'Oran (K/Y): {ratio:.2f}', (10, image_height - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Sonuçları yazdırma
    print(f"Kırmızı sinyal sayısı: {red_signal_count}")
    print(f"Yeşil sinyal sayısı: {green_signal_count}")
    print(f"Oran (Kırmızı/Yeşil): {ratio:.2f}")

    # Yeni dosya ismi oluşturma
    output_image_path = os.path.join(image_dir, f"{image_name}_count_output{image_ext}")

    # Resmi dosya olarak kaydetme
    cv2.imwrite(output_image_path, image)
    print(f"İşlenmiş görüntü kaydedildi: {output_image_path}")
