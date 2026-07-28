# Iron Logic BOM Generator 🛠️

## Overview
The Iron Logic BOM (Bill of Materials) Generator is an automated Python pipeline designed to calculate, structure, and output hardware requirements for localized high-performance compute fabrics and AI agent environments. 

Instead of manual spreadsheet calculations, this tool intakes core architectural requirements (Compute, Memory, Networking, Power) and generates a structured, standardized BOM ready for client quoting and procurement.

## Core Features
*   **Automated Calculation:** Dynamically calculates total power draw and rack space based on component inputs.
*   **Structured Output:** Exports the final BOM to both a human-readable format (CSV/PDF) and a machine-readable payload (JSON) for API integration.
*   **Error Handling:** Enforces strict hardware compatibility checks (e.g., ensuring GPU thermal limits match chassis capabilities) before generating the report.

## Prerequisites
*   Python 3.8+
*   `requests` (for pulling live hardware pricing via API - planned)
*   `reportlab` (for generating the final PDF deliverable)

## Usage
1. Clone the repository to your local management node.
2. Ensure your input constraints are defined in `config.json`.
3. Execute the generator: `python3 generate_bom.py`