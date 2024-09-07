# HER2 Signal Detection Project

Bu Python projesi, HER2 sinyallerini ve referans sinyallerini görüntülerde tespit eder, bu sinyalleri renkli noktalarla işaretler ve HER2 oranını hesaplar. Bu araç manuel sayım ile kontrol edilmeli ve **tanı amacıyla kullanılmamalıdır**.

## Özellikler
- HER2 ve referans sinyalleri renk tonlarına göre tespit eder.
- HER2 sinyallerini sarı noktalarla, referans sinyalleri ise mavi noktalarla işaretler.
- HER2/Referans sinyal oranını hesaplar ve görüntüye yazar.
- Gereksiz renkler hariç tutularak tespit hassasiyeti arttırılır.
- Çıktı görüntü dosyası, orijinal görüntüyle aynı klasöre, orijinal dosya adının yanına `_count_output` eklenerek kaydedilir.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız var:

```bash
opencv-python
numpy
tkinter (Python ile birlikte gelir)
```

### Kütüphaneleri kurmak için:
```bash
pip install opencv-python numpy
```

## Nasıl Çalıştırılır

1. **Python Dosyasını Çalıştırın:**
   Proje dizininde Python dosyasını çalıştırın:

   ```bash
   python her2_signal_detection.py
   ```

2. **Resim Seçin:**
   Program çalıştığında bir dosya seçim penceresi açılır. Taranacak olan HER2 sinyallerini içeren görüntüyü seçin.

3. **Sonuçlar:**
   - HER2 ve referans sinyalleri tespit edilir ve uygun renklerle işaretlenir.
   - HER2 sinyalleri sarı, referans sinyalleri mavi noktalarla gösterilir.
   - Sinyal sayıları ve HER2/Referans oranı görüntü üzerine yazılır.
   - Çıktı dosyası, orijinal resmin bulunduğu klasöre `*_count_output` eklenerek kaydedilir.

4. **Manuel Kontrol:**
   Sonuçlar **manuel sayma ile doğrulanmalıdır**. Bu araç yalnızca sayım kolaylığı sağlamak için geliştirilmiştir ve **tanı amaçlı kullanılmamalıdır**.

## Örnek Çıktı

- HER2 sinyalleri: 35
- Referans sinyalleri: 20
- HER2/Referans Oranı: 1.75

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için [LICENSE](./LICENSE) dosyasına göz atabilirsiniz.
