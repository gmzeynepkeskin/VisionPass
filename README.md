# VisionPass
AI-powered biometric payment system
# 👁️ VisionPass: AI-Powered Biometric Payment System
![AI](https://img.shields.io/badge/Tech-YOLOv8%20%7C%20ArcFace-blue.svg)
![Partner](https://img.shields.io/badge/Integration-Paycell-orange.svg)
![Privacy](https://img.shields.io/badge/Security-KVKK%20Compliant-green.svg)

**VisionPass**, toplu taşımada turnikeleri ve fiziksel kartları ortadan kaldıran, yapay zeka destekli bir "yüzün senin biletindir" projesidir.

## 🚀 Proje Vizyonu (Project Vision)
Bu proje, istasyonlardaki yığılmaları önlemek ve yolculara kesintisiz bir seyahat deneyimi sunmak için geliştirilmiştir. Yolcuların giriş ve çıkış noktaları kameralar aracılığıyla tespit edilir ve gidilen mesafe kadar ücret, **Paycell** dijital cüzdanından otomatik olarak tahsil edilir.

## 🛡️ Gizlilik ve KVKK Uyumu (Privacy & GDPR)
Sistem, "Tasarım Yoluyla Gizlilik" (Privacy by Design) prensibiyle kurgulanmıştır:
- **Veri Anonimleştirme:** Gerçek yüz görüntüleri saklanmaz; anlık olarak geri döndürülemez matematiksel vektörlere (hash) dönüştürülür.
- **Rıza Bazlı Geçiş:** Sadece Paycell üzerinden onay veren kullanıcılar sistemi kullanabilir.
- **Yerinde İşleme (Edge AI):** Veriler merkeze taşınmadan istasyon bazında işlenerek güvenlik riski minimize edilir.

## ⚙️ Teknolojik Altyapı (Tech Stack)
- **Nesne Tespiti:** YOLOv8 (Yolcuların tespiti için).
- **Yüz Tanıma:** ArcFace / FaceNet (Biyometrik doğrulama için).
- **Takip Algoritması:** DeepSORT / Person Re-ID (Kalabalık içinde takip için).
- **Yazılım:** Python & OpenCV.

---
**Developer:** Zeynep Keskin  
*Ankara Üniversitesi - Gıda Mühendisliği Adayı*
