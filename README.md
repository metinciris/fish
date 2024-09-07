# HER2 Signal Detection Project

Bu Python projesi, HER2 ve CEP17 sinyallerini görüntülerde tespit eder, bu sinyalleri renkli noktalarla işaretler ve HER2/CEP17 oranını hesaplar. Proje, tanı amacıyla kullanılmamakla birlikte, manuel doğrulama ile kontrol edilmesi önerilir.

## Özellikler
- HER2 ve CEP17 sinyallerini renk tonlarına göre tespit eder.
- HER2 sinyallerini sarı, CEP17 sinyallerini mavi noktalarla işaretler.
- HER2/CEP17 sinyal oranını hesaplar ve sonuçları resim üzerine Türkçe karakterlerle yazdırır.
- Gereksiz renkler hariç tutularak tespit hassasiyeti arttırılır.
- Çıktı görüntü dosyası, orijinal görüntüyle aynı klasöre, orijinal dosya adının yanına `_count_output` eklenerek kaydedilir.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız var:

```bash
opencv-python
numpy
pillow
tkinter (Python ile birlikte gelir)
```

### Kütüphaneleri kurmak için:
```bash
pip install opencv-python numpy pillow
```

## Nasıl Çalıştırılır

1. **Python Dosyasını Çalıştırın:**
   Proje dizininde Python dosyasını çalıştırın:

   ```bash
   python her2_signal_detection.py
   ```

2. **Resim Seçin:**
   Program çalıştığında bir dosya seçim penceresi açılır. HER2 ve CEP17 sinyallerini içeren görüntüyü seçin.

3. **Sonuçlar:**
   - HER2 ve CEP17 sinyalleri tespit edilir ve uygun renklerle işaretlenir.
   - HER2 sinyalleri sarı, referans sinyalleri mavi noktalarla gösterilir.
   - Sinyal sayıları ve HER2/CEP17 oranı görüntü üzerine yazılır.
   - Sonuç olarak, görüntü dosyası orijinal dosya isminin yanına `_count_output` eklenerek kaydedilir.

4. **Gruplama:**
   Sonuçlar, HER2/CEP17 oranına ve HER2 sinyallerine göre 5 gruba ayrılır:
   - **Grup 1:** HER2/CEP17 oranı ≥ 2.0 ve ≥ 4.0 HER2 sinyali/hücre
   - **Grup 2:** HER2/CEP17 oranı ≥ 2.0 ve < 4.0 HER2 sinyali/hücre
   - **Grup 3:** HER2/CEP17 oranı < 2.0 ve ≥ 6.0 HER2 sinyali/hücre
   - **Grup 4:** HER2/CEP17 oranı < 2.0 ve ≥ 4.0 ve < 6.0 HER2 sinyali/hücre
   - **Grup 5:** HER2/CEP17 oranı < 2.0 ve < 4.0 HER2 sinyali/hücre

## Örnek Çıktı

- **HER2 sinyalleri:** 35
- **CEP17 sinyalleri:** 20
- **HER2/CEP17 Oranı:** 1.75
- **Grup:** Grup 2: HER2/CEP17 oranı ≥ 2.0; < 4.0 HER2 sinyali/hücre

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için [LICENSE](./LICENSE) dosyasına göz atabilirsiniz.

- **Lisans:** Proje MIT lisansı ile lisanslanmıştır.
