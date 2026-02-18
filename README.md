# VisionPass
AI-powered biometric payment
# 👁️ VisionPass: Turnikesiz Biyometrik Ödeme Sistemi

Selam! Ben Zeynep Keskin. Ankara Üniversitesi Gıda Mühendisliği 4. sınıf öğrencisiyim. Bu proje, Turkcell "Yarının Teknoloji Liderleri" programı için geliştirdiğim, günlük hayattaki ulaşım çilesine teknolojik bir çözüm arayan vizyon çalışmamdır.

## 🚀 Bu Proje Nereden Çıktı?
Bir mühendis adayı olarak sistemlerdeki verimlilik kayıpları her zaman ilgimi çekmiştir. Toplu taşımadaki turnike sıraları ve kart basma telaşının hem zaman kaybı hem de operasyonel bir yük olduğunu düşünüyorum. VisionPass ile "yüzün senin biletin olsun" diyerek bu süreci tamamen dijitalleştirmeyi hedefledim.

## 💡 Sistem Nasıl Çalışıyor? (Basitçe)
Sistem, istasyon giriş-çıkışlarındaki kameralar üzerinden yolcuları tanıyor. 
* **YOLOv8** ile insanları seçiyor.
* **ArcFace** ile bu kişileri matematiksel bir "imzaya" dönüştürüyor.
* En sonunda gidilen mesafe hesaplanıp **Paycell** üzerinden ödeme alınıyor.

## 🛡️ Gizlilik Hakkında Notlarım (KVKK)
En çok dikkat ettiğim nokta gizlilik oldu. Sistem asla ham fotoğraf saklamıyor. Yüzü görür görmez onu geri döndürülemez bir sayı dizisine çeviriyor. Yani sistemde sadece "matematik" var, fotoğraf yok! Ayrıca bu sistem sadece Paycell üzerinden onay veren kullanıcılar için aktif olacak şekilde kurgulandı.

## 🛠️ Neler Kullandım?
* Python & OpenCV
* Derin Öğrenme Modelleri (YOLOv8, FaceNet)
* Takip Algoritmaları (DeepSORT)
