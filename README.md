# 🛡️ Iron Logic: AI Infrastructure Toolkit
*Automated Sovereign AI Operations & Day 2 Fabric Management* ⚙️

## 📖 Executive Summary
This repository contains a suite of automation tools engineered to manage high-density GPU/AI clusters. It addresses the critical requirements of modern infrastructure: **Network Fabric Stability**, **Air-Gapped Data Integrity**, and **AI Resource Optimization (FinOps)**.

## 🏗️ Core Technical Pillars

### 1. 🌐 Fabric Intelligence (`production/bgp_keepalive.py` & `production/nccl_optical_auditor.py`)
Automates the audit of BGP network daemons and optical switch linkages. Instead of manual log review, this toolset ingests raw operational logs, calculates protocol stability, and flags micro-reflections or buffer overflows.
* ⚡ **Impact:** Reduced mean-time-to-detection (MTTD) for network fabric degradation across RoCEv2/InfiniBand environments.

### 2. 🔐 Security Governance (`production/secure_vault_ingest.py`)
Implements an air-gapped ingestion gatekeeper. It enforces strict data provenance by verifying the SHA-256 integrity of all incoming payloads before they are authorized for deployment into the training pipeline.
* 🛑 **Impact:** Prevents unauthorized or corrupted model weight injection at the entry point.

### 3. 💰 AI FinOps (`production/vram_zombie_killer.py`)
An automated audit engine designed to hunt "zombie processes"—applications consuming VRAM with 0% compute utilization.
* 📉 **Impact:** Enables data-driven cost recovery by identifying and terminating inefficient GPU footprint allocations.

## 🛠 Deployment & Orchestration
*Our infrastructure is managed as code to ensure repeatability and security across isolated GPU clusters.*

*   **Provisioning (Terraform):** Automated creation of virtualized compute nodes, network interfaces, and storage volumes.
*   **Configuration & Hardening (Ansible):** 
    *   **Security:** Enforces system-level banners and access controls.
    *   **Time Synchronization:** Managed via `chrony` to ensure microsecond accuracy across the cluster.
    *   **Baseline:** Standardizes environment packages for Sovereign AI operations.

## 🧠 Technical Discipline
- 📡 **Observability:** All modules generate persistent, structured audit logs (`logs/`) for headless operational tracking.
- 📂 **Environment:** Production-hardened structure with strictly isolated deployment logic.
