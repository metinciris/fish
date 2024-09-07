# Signal Detection Project

Bu Python projesi, görüntülerdeki kırmızı ve yeşil sinyalleri tespit eder, bu sinyalleri renkli noktalarla işaretler ve kırmızı/yeşil sinyal oranını hesaplar. Sinyallerin merkezindeki parlaklığa göre tespit yapılır ve gereksiz renkler hariç tutulur.

## Özellikler
- Kırmızı ve yeşil sinyalleri renk tonlarına göre tespit eder.
- Kırmızı sinyalleri sarı noktalarla, yeşil sinyalleri ise mavi noktalarla işaretler.
- Kırmızı/yeşil sinyal oranını hesaplar ve görüntüye yazar.
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
   python signal_detection.py
   ```

2. **Resim Seçin:**
   Program çalıştığında bir dosya seçim penceresi açılır. Taranacak olan görüntüyü seçin.

3. **Sonuçlar:**
   - Kırmızı ve yeşil sinyaller tespit edilir ve uygun renklerle işaretlenir.
   - Sinyal sayıları ve kırmızı/yeşil oranı görüntü üzerine yazılır.
   - Çıktı dosyası, orijinal resmin bulunduğu klasöre `*_count_output` eklenerek kaydedilir.

## Örnek Çıktı

- Kırmızı sinyaller: 35
- Yeşil sinyaller: 20
- Kırmızı/Yeşil Oranı: 1.75

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için [LICENSE](./LICENSE) dosyasına göz atabilirsiniz.


