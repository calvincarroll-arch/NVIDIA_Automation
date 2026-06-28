# 🛡️ Iron Logic AI-Infra Toolkit
**Sovereign Infrastructure. Localized Iron. Zero Hyperscaler Bloat.**

### 📖 Executive Summary
As macro-economic pressures force enterprise hyperscaler cloud costs to bleed budgets dry, the industry is pivoting back to on-premise, sovereign hardware. The **Iron Logic AI-Infra Toolkit** is a proprietary suite of Python automation scripts designed to build, secure, and manage localized, cost-controlled AI data centers that mathematically outperform the cloud. 

Built by a Senior Optical/AI Infrastructure Architect, this repository bridges 15+ years of Layer 1-3 network transport mastery with the NVIDIA AI software stack.

**The Mission:** Automate local iron, protect data sovereignty, and eliminate recurring SaaS fees.

---

### 🏗️ Core Operational Pillars

#### I. High-Speed Fabric & Optical Automation
Scripts to automate the physical and logical layers of Lossless Ethernet (RoCEv2) and InfiniBand.
* `production/bgp_keepalive.py`: A deterministic BGP state-machine daemon that monitors SuperPOD Leaf/Spine stability.
* `production/nccl_optical_auditor.py`: Parses Arista/NVIDIA switch logs via Regex to audit buffer overflows and RDMA packet drops.

#### II. AI FinOps & "Day 2" Operations
Maximizing the ROI of high-density hardware (Hopper/Blackwell).
* `production/vram_zombie_killer.py`: Parses `nvidia-smi` to hunt down and elegantly terminate memory-leaking processes consuming VRAM with 0% compute utilization.

---
*Built by Iron Logic LLC. Executing the Sovereign AI Roadmap.*
