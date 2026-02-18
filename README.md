# VisionPass
## Otonom ve Açık Rızaya Dayalı Dijital Mobilite Kimlik Protokolü

VisionPass, toplu taşıma sistemlerinde fiziksel turnike ve kart bağımlılığını azaltmayı hedefleyen, açık rızaya dayalı dijital bir mobilite kimlik altyapısıdır. Proje, Turkcell “Yarının Teknoloji Liderleri” programı kapsamında geliştirilmiştir.

Amaç, mevcut ulaşım altyapısını tamamen değiştirmek yerine, var olan kamera sistemleri ve yapay zekâ teknolojileri üzerinden serbest akış prensibine dayalı daha verimli bir model önermektir.

---

## Problem Tanımı

Günümüzde toplu taşıma sistemleri:

- Fiziksel ulaşım kartlarına
- QR kod okutma süreçlerine
- Turnike donanımına

bağımlıdır.

Bu yapı özellikle yoğun saatlerde kapasite kaybına, yüksek operasyon ve bakım maliyetlerine ve donanım temelli darboğazlara neden olmaktadır.

---

## Çözüm Yaklaşımı

VisionPass, açık rıza vermiş kullanıcılar için çalışan dijital bir mobilite kimlik protokolü sunar.

Sistem:

- Gerçek zamanlı insan tespiti yapar
- Kimliği matematiksel vektörlere dönüştürür
- Giriş ve çıkış noktalarını eşleştirir
- Mesafeye dayalı ücret hesaplar
- Ödemeyi Paycell altyapısı üzerinden arka planda gerçekleştirir

Bu sayede fiziksel kart taşıma veya turnike temasına ihtiyaç duyulmaz.

---

## Sistem Mimarisi

Algılama Katmanı:  
YOLOv8 modeli kullanılarak kalabalık ortamlarda gerçek zamanlı insan tespiti yapılır.

Kimlik Vektörleştirme:  
ArcFace algoritması ile yüz verisi embedding vektörüne dönüştürülür. Ham görüntü saklanmaz.

Otonom Ücret Motoru:  
Giriş ve çıkış noktaları eşleştirilir, mesafe hesaplanır ve ücret otomatik olarak tahsil edilir.

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
- ArcFace
- DeepSORT
- PyTorch

---

## Kurulum (PoC)

