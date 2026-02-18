# VisionPass
### Consent-Based Autonomous Mobility Identity Protocol

VisionPass is a vision project developed for the **Turkcell Yarının Teknoloji Liderleri Programı** by Zeynep Keskin, a Food Engineering student at Ankara University and a system architecture candidate.

## 🚀 Vision
VisionPass aims to eliminate physical turnstiles and hardware dependencies in public transportation by introducing a **fully digital, consent-driven mobility identity layer** integrated into the Paycell ecosystem.

## ❗ Problem Definition
Current urban transportation systems rely on physical cards, QR scans, or turnstiles, causing:
- Bottlenecks during peak hours
- High operational and maintenance costs
- Hardware dependency and scalability limits

## 💡 Solution
VisionPass enables **free-flow public transportation** using existing camera infrastructure and edge AI technologies, operating only with explicit user consent through Paycell.

## 🧠 System Architecture
The system operates in three main stages:

### 1. Detection
Real-time human detection using YOLOv8 for millisecond-level accuracy in crowded environments.

### 2. Identity Verification
Face embeddings are generated using ArcFace and immediately converted into irreversible encrypted vectors.  
⚠️ No raw images are stored or transmitted.

### 3. Autonomous Fare Collection
Entry and exit points are matched, travel distance is calculated, and fare collection is executed automatically via Paycell APIs in the background.

## 🔐 Privacy by Design
- No video storage
- No facial image storage
- On-device processing
- Encrypted, non-reversible identity vectors
- Explicit user consent via Paycell application

## 🛠 Technology Stack
- Python
- OpenCV
- YOLOv8
- ArcFace
- DeepSORT

## 📦 Installation (PoC)
```bash
pip install -r requirements.txt
