# VisionPass
## Autonomous & Contactless Biometric Mobility Ecosystem

VisionPass is a Proof-of-Concept (PoC) project developed by Zeynep Keskin for the Turkcell "Yarının Teknoloji Liderleri 10" program.

The project aims to transform urban mobility by eliminating hardware dependency and enabling a seamless, biometric-based transit experience powered by AI and edge computing.

---

## 🚩 Problem Statement

Current public transportation systems rely on:

- Physical turnstiles
- Plastic transportation cards
- Manual QR scanning

These systems create:
- Congestion during peak hours
- High maintenance and operational costs
- Hardware dependency
- Inefficient passenger flow

VisionPass introduces a hybrid biometric fast-pass model integrated with Paycell.

---

## 🧠 System Architecture

The system consists of three core AI-driven layers:

### 1️⃣ Detection (Computer Vision)
- YOLOv8 is used for real-time person detection in crowded environments.
- Millisecond-level inference on edge devices.

### 2️⃣ Biometric Verification
- ArcFace converts facial data into encrypted mathematical embeddings.
- No raw image is stored.
- Privacy-by-design architecture.

### 3️⃣ Autonomous Payment
- Entry and exit stations are detected.
- Distance-based fare is calculated.
- Payment is automatically processed via Paycell API (with user consent).

---

## 🔐 Privacy & Security

VisionPass operates only for users who provide explicit consent within the Paycell application.

- No raw facial images are stored.
- Biometric embeddings are encrypted.
- Users can delete their biometric data at any time.
- System follows KVKK & GDPR principles.

---

## 🛠 Tech Stack

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- ArcFace
- DeepSORT
- PyTorch

---

## ⚙ Installation

Install dependencies:

pip install -r requirements.txt

Run demo:

python main.py

---

## 🧪 Current Status

This project is currently in Proof-of-Concept stage.

The demo version performs:
- Real-time person detection
- Bounding box tracking
- AI-based infrastructure simulation

---

## 🚀 Future Roadmap

Phase 1: Turkcell internal pilot (Plaza access control)  
Phase 2: Campus or AVM pilot integration  
Phase 3: Public transportation hybrid fast-pass deployment  

Long-term goal: Establish VisionPass protocol as a standard digital mobility layer in Türkiye.

---

## 📊 Business Model

- Micro transaction commission via Paycell
- B2B infrastructure licensing
- Hardware reduction savings
- API-based smart mobility integration

---

## 📎 Pitch Deck

See VisionPass_PitchDeck.pdf inside this repository.

---

## 👩‍💻 Project Owner

Zeynep Keskin  
Ankara University – Food Engineering  
System Architecture Candidate  
Turkcell "Yarının Teknoloji Liderleri 10" Applicant
