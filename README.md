# ⏱️ Azure VM Scheduler Resize Script

This Python script automatically resizes an Azure Virtual Machine (VM) based on the time of day. It uses Azure's Python SDK (`azure-mgmt-compute`) and `DefaultAzureCredential` for secure, automated authentication.

## 📌 Features

- Automatically checks current time and triggers resize:
  - At **11 PM** → Resizes VM to a smaller size (e.g., `Standard_D4s_v3`)
  - At **7 AM** → Resizes VM to a larger size (e.g., `Standard_D8s_v3`)
- Uses Azure best practices:
  - Deallocates VM before resizing
  - Resizes using Azure Compute Management client
  - Starts the VM after resizing
- Fully automated — designed to be run via a cron job, Azure Function, or scheduled workflow.

## 🔧 Requirements

- Python 3.7+
- Azure CLI logged in OR environment configured for `DefaultAzureCredential`
- Azure subscription with permissions to manage the VM

## 📦 Python Dependencies

Install required packages:

```bash
pip install azure-identity azure-mgmt-compute
