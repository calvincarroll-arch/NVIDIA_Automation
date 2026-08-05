# 🛡️ Iron Logic: AI Infrastructure & Lossless Fabric Toolkit
*Automated Sovereign AI Operations, Event-Driven CI/CD & Day 0–2 Fabric Management* ⚙️

## 📖 Executive Summary
This repository contains an enterprise-grade suite of network automation tools engineered to provision, trigger, validate, and bootstrap high-density GPU/AI clusters. It addresses the critical requirements of modern infrastructure: **Event-Driven CI/CD Automation**, **Lossless RoCEv2 Fabric Integrity**, **Air-Gapped Data Governance**, and **AI Resource Optimization (FinOps)**.

---

## 🏗️ Core Technical Pillars

### 1. ⚡ Event-Driven CI/CD & Fabric Automation (`webhook_listener.py` & `push_roce_config.py`)
Links NetBox directly to a local Flask receiver to eliminate manual terminal execution. Modifying switch configurations, port parameters, or IP allocations inside the NetBox Source of Truth (SoT) fires an instant HTTP POST webhook, automatically triggering Nornir to compile and push lossless RoCEv2 and BGP underlay Jinja2 templates across the fabric.
* ⚡ **Impact:** Enforces zero-click continuous deployment—intended state in NetBox becomes actual network state in real time.

### 2. 🔍 Continuous Pre/Post-Change Compliance Auditing (`audit_compliance.py`)
Uses `DeepDiff` and Nornir to parse live running switch configurations against golden Jinja2 baselines. Mathematically compares host structures to flag out-of-spec parameters before traffic is impacted.
* 🛑 **Impact:** Prevents configuration drift by instantly detecting shifts in BGP timers, interface MTUs, or PFC/ECN buffer thresholds (`ecn_max_th`).

### 3. 🚀 Automated "Day 0" Bare-Metal ZTP Provisioning (`day0_ztp_provisioner.py`)
Automates bare-metal rack onboarding for new GPU leaf switches and compute nodes. Queries NetBox using hardware serial numbers/MAC addresses to look up rack assignments, IP subnets, and ASNs, then dynamically stages executable Cumulus Linux Zero Touch Provisioning (ZTP) shell scripts.
* 🛠️ **Impact:** Eliminates manual console cabling during colocation rack deployments through automated PXE/HTTP boot handoffs.

### 4. 🌐 Fabric Intelligence (`production/bgp_keepalive.py` & `production/nccl_optical_auditor.py`)
Automates the audit of BGP network daemons and optical switch linkages. Ingests raw operational logs, calculates protocol stability, and flags micro-reflections or buffer overflows.
* ⚡ **Impact:** Reduced mean-time-to-detection (MTTD) for network fabric degradation across RoCEv2/InfiniBand environments.

### 5. 🔐 Security Governance (`production/secure_vault_ingest.py`)
Implements an air-gapped ingestion gatekeeper enforcing strict data provenance by verifying the SHA-256 integrity of incoming payloads before authorizing deployment into training pipelines.
* 🛑 **Impact:** Prevents unauthorized or corrupted model weight injection at entry points.

### 6. 💰 AI FinOps (`production/vram_zombie_killer.py`)
An automated audit engine designed to hunt "zombie processes" consuming VRAM with 0% compute utilization.
* 💡 **Impact:** Enables data-driven cost recovery by terminating inefficient GPU footprint allocations and dynamically logging reclaimed VRAM monetary metrics.

### 7. 🔌 Metro Transport & AI Infrastructure BOM Engineering (`iron-logic-bom/`)
Parses shelf/slot/port (`sh/sl/pt`) optical telemetry, validates power attenuation (dBm), and dynamically models hardware bills of materials for localized computing fabrics.
* 🛠️ **Impact:** Eliminates manual spreadsheet errors, prevents optical link attenuation failures, and automates end-to-end component scaling.

---

## 📐 Event-Driven Pipeline Topology

```text
                  +--------------------------------+
                  | NetBox Source of Truth (SoT)   |
                  +---------------+----------------+
                                  |
                                  | (Webhook POST Trigger)
                                  v
                  +--------------------------------+
                  | Flask Receiver Listener (5000) |
                  +---------------+----------------+
                                  |
                                  v
                  +--------------------------------+
                  | Nornir Automation Controller   |
                  +---------------+----------------+
                                  |
      +---------------------------+---------------------------+
      |                           |                           |
      v                           v                           v
+---------------+           +---------------+           +---------------+
| atl-ept-lf-05 |           | hou-spk-lf-04 |           | smr-qb-lf-02  |
|  (AI Leaf 5)  |           |  (AI Leaf 4)  |           |  (AI Leaf 2)  |
+---------------+           +---------------+           +---------------+
```

## 🛠 Deployment & Orchestration

```bash
# Start the event-driven webhook listener
python3 webhook_listener.py

# Run continuous compliance audit across the fabric
python3 audit_compliance.py

# Generate Day 0 ZTP boot manifests for new hardware
python3 day0_ztp_provisioner.py
```

* **Provisioning (Terraform):** Automated creation of virtualized compute nodes, network interfaces, and storage volumes.
* **Configuration & Hardening (Ansible):** Enforces system-level banners, system access controls, and `chrony` time synchronization for microsecond cluster accuracy.

---

## 🧠 Technical Discipline
- 📡 **Observability:** All modules generate persistent, structured audit logs (`logs/`) for headless operational tracking.
- 📂 **Environment:** Production-hardened structure with strictly isolated deployment logic.