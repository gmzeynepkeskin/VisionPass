# VisionPass  
## Otonom ve Açık Rızaya Dayalı Dijital Mobilite Kimlik Protokolü

VisionPass, toplu taşıma sistemlerinde fiziksel turnike ve kart bağımlılığını azaltmayı hedefleyen, açık rızaya dayalı dijital bir mobilite kimlik altyapısıdır.

Proje, Turkcell “Yarının Teknoloji Liderleri” programı kapsamında geliştirilmiştir.

Amaç; mevcut ulaşım altyapısını tamamen değiştirmek yerine, var olan kamera sistemleri ve yapay zekâ teknolojileri üzerinden serbest akış (free-flow) prensibine dayalı daha verimli ve ölçeklenebilir bir model önermektir.

---

## Problem Tanımı

Günümüzde toplu taşıma sistemleri:

- Fiziksel ulaşım kartlarına  
- QR kod okutma süreçlerine  
- Turnike donanımına  

bağımlıdır.

Bu yapı özellikle yoğun saatlerde:

- Kapasite kaybına  
- Yüksek operasyon ve bakım maliyetlerine  
- Donanım temelli darboğazlara  

neden olmaktadır.

---

## Çözüm Yaklaşımı

VisionPass, açık rıza vermiş kullanıcılar için çalışan dijital bir mobilite kimlik protokolü sunar.

Sistem:

- Gerçek zamanlı insan tespiti yapar  
- Kişiyi takip eder ve benzersiz ID üretir  
- Yüz bilgisini matematiksel embedding vektörüne dönüştürür  
- Giriş ve çıkış noktalarını eşleştirir  
- Mesafeye dayalı ücret hesaplar  
- Ödemeyi Paycell altyapısı üzerinden arka planda gerçekleştirir  

Bu sayede fiziksel kart taşıma veya turnike temasına ihtiyaç duyulmaz.

---

## Sistem Mimarisi

### Algılama Katmanı  
YOLOv8 modeli kullanılarak kalabalık ortamlarda gerçek zamanlı insan tespiti yapılır.

### Takip Katmanı  
DeepSORT ile tespit edilen her kişi için benzersiz bir takip kimliği oluşturulur.

### Kimlik Vektörleştirme  
ArcFace algoritması ile yüz verisi embedding vektörüne dönüştürülür. Ham görüntü saklanmaz.

### Otonom Ücret Motoru  
Giriş ve çıkış noktaları eşleştirilir, mesafe hesaplanır ve ücret otomatik olarak tahsil edilir.

---

## Sistem Akışı
Kamera / Video
↓
YOLOv8 (İnsan Tespiti)
↓
DeepSORT (Takip)
↓
ArcFace (Yüz Embedding)
↓
Giriş-Çıkış Eşleştirme
↓
Ücret Hesaplama
↓
Paycell / Veritabanı
---

## Gizlilik ve Güvenlik

Sistem “Privacy by Design” prensibiyle tasarlanmıştır.

- Video kaydı tutulmaz  
- Ham yüz görüntüsü saklanmaz  
- İşlemler mümkün olduğunca uçta (edge) gerçekleştirilir  
- Şifrelenmiş ve geri döndürülemez kimlik vektörleri kullanılır  
- Sistem yalnızca açık rıza vermiş kullanıcılar için aktiftir  

VisionPass bir gözetim sistemi değil, açık rızaya dayalı bir mobilite kimlik altyapısı önerisidir.

---

## Kullanılan Teknolojiler

- Python  
- OpenCV  
- YOLOv8  
- DeepSORT  
- ArcFace  
- PyTorch  

---

## Kurulum
pip install -r requirements.txt
---

## Çalıştırma

Kamera ile çalıştırmak için:
python main.py –camera 0
Video dosyası ile test etmek için:
python main.py –video test.mp4
---

## Yol Haritası

**Kısa Vadede:**  
Paycell QR entegrasyonu ile hibrit bir geçiş modeli.

**Orta Vadede:**  
Metro, otobüs ve tramvay sistemleriyle entegrasyon.

**Uzun Vadede:**  
Akıllı şehirlerde standart mobilite kimlik protokolü haline gelmek.
