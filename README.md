# VisionPass
## Autonomous Consent-Based Mobility Identity Protocol

> Built as a vision project for Turkcell's "Yarının Teknoloji Liderleri" Program.

VisionPass is a consent-based digital mobility identity protocol designed to eliminate physical turnstiles and hardware dependency in public transportation systems.

Developed by Zeynep Keskin, Ankara University Food Engineering student and system architecture candidate, the project combines computer vision, edge AI, and telecom ecosystem integration to enable frictionless urban mobility.

---

## 🚀 Problem

Urban transportation systems still rely on:
- Physical transportation cards
- QR code scanning
- Hardware-based turnstiles

These create:
- Bottlenecks during peak hours
- High operational costs
- Maintenance dependency
- Scalability limitations

---

## 💡 Solution

VisionPass introduces a **free-flow transportation model** powered by:

- Real-time human detection
- Consent-based biometric identity verification
- Autonomous fare calculation
- Background digital payment integration via Paycell

The system operates only for users who provide explicit consent within the Paycell ecosystem.

---

## 🧠 System Architecture

### 1️⃣ Detection Layer  
Real-time person detection using YOLOv8 in high-density environments.

### 2️⃣ Identity Vectorization  
Face embeddings generated using ArcFace are immediately converted into encrypted, non-reversible identity vectors.  
No raw images are stored.

### 3️⃣ Autonomous Fare Engine  
Entry and exit stations are matched, distance is calculated, and fare is automatically charged via Paycell APIs.

---

## 🔐 Privacy & Security (Privacy by Design)

- No video storage  
- No facial image storage  
- On-device processing  
- Encrypted identity vectors  
- Explicit user consent required  

VisionPass is not a surveillance system.  
It is a **consent-driven mobility identity infrastructure**.

---

## 🛠 Technology Stack

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- ArcFace
- DeepSORT
- PyTorch

---

## 📦 Installation (PoC)

```bash
pip install -r requirements.txt
