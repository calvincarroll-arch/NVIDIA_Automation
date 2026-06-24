🛡️ Iron Logic AI-Infra Toolkit
Sovereign Infrastructure. Localized Iron. Zero Hyperscaler Bloat.
📖 Executive Summary
As macro-economic pressures force enterprise hyperscaler cloud costs and fragmented SaaS subscriptions to bleed budgets dry, the industry is pivoting back to on-premise, sovereign hardware.
The Iron Logic AI-Infra Toolkit is a proprietary suite of automation scripts designed to build, secure, and manage localized, cost-controlled AI data centers that mathematically outperform the cloud. Built by a Senior Optical/AI Infrastructure Architect, this repository bridges 15+ years of Layer 1-3 network transport mastery with the NVIDIA AI software stack (NCA/NCP-AIIO).
This toolkit proves one message: We build and automate local iron, protect data sovereignty, and eliminate recurring software fees.
🏗️ Core Pillars & Architecture
I. High-Speed Fabric & Optical Automation
High-Frequency Trading (HFT) firms and AI factories lose millions if a compute cycle drops a packet. These scripts automate the physical and logical layers of Lossless Ethernet (RoCEv2) and InfiniBand.
nccl_optical_auditor.py: Parses Arista/NVIDIA Quantum switch logs to automatically audit buffer overflows, fiber micro-reflections, and dropped RDMA packets, mathematically guaranteeing line-rate throughput.
bgp_keepalive.py: Ensures SuperPOD Leaf/Spine stability by automating BGP health checks across a Lossless RoCEv2 environment.
ib_symbol_error_watchdog.py: Parses ibqueryerrors to detect physical optical degradation (Symbol Errors) on 400G+ links before they stall parallel distributed training loops.
nccl_topo_automapper.py: Leverages lspci and ibstat to automatically generate NCCL_TOPO_FILE XMLs, mapping the physical server layout to bypass CPU bottlenecks for GPU-to-GPU data paths.
II. Sovereign Data & Air-Gapped Security
Targeting law firms, healthcare, and defense requiring absolute data sovereignty.
secure_vault_ingest.py: Automates the secure transfer of massive datasets (e.g., 10TB of legal discovery) onto local NAS via 10G Twinax. Verifies SHA256 hashes, organizes data, and ensures the environment remains physically air-gapped from the public internet.
sovereign_ngc_sync.py: Securely packages NVIDIA NGC containers (Triton/TensorRT) into verified tarballs for SCP transfer into locked-down, air-gapped private registries.
III. AI FinOps & "Day 2" Operations
Maximizing the ROI of high-density hardware (Hopper/Blackwell).
gpu_finops_tracker.py: Pings dcgmi stats, grabs exact Joules/Watts consumed per Slurm Job ID, calculates local grid electrical costs, and generates an automated AI FinOps receipt.
xid_anomaly_detector.py: Tails /var/log/syslog with Regex to hunt for fatal, silicon-level NVIDIA XID errors (e.g., XID 43, 62) and fires automated webhooks.
dynamic_mig_provisioner.sh: Safely checks idle states and dynamically carves physical GPUs into secure Multi-Instance GPU (MIG) hardware slices for multi-tenant isolation.
vram_zombie_killer.py: Parses nvidia-smi -q -d PIDS to hunt down and elegantly terminate memory-leaking processes consuming VRAM with 0% compute utilization.
triton_ttft_probe.py: Acts as a synthetic user, firing gRPC requests to Triton Inference Server to log Time-To-First-Token (TTFT) latency, flagging QoS queue delays.
IV. Agentic Edge & Sovereign SaaS
Replacing fragmented monthly SaaS fees with localized, autonomous execution.
local_agentic_harvester.py: A localized Python agent designed to run autonomously on an RTX edge workstation. Scrapes social metrics, aggregates streams, and updates local databases—granting the client 100% data ownership.
prop_trade_api_connector.py: A local API bridge securely connecting an "In-House Oracle" with live external data streams, handling authentication locally without exposing proprietary logic to cloud vendors.
Built by Iron Logic LLC.
