#  Azure VM Scheduler Resize Script

This Python script automatically resizes an Azure Virtual Machine (VM) based on the time of day. It uses Azure's Python SDK (`azure-mgmt-compute`) and `DefaultAzureCredential` for secure, automated authentication.

##  Features

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

## Python Dependencies

Install required packages:

```bash
pip install azure-identity azure-mgmt-compute
 Configuration
Edit the script to match your Azure settings:

subscription_id = 'YOUR_SUBSCRIPTION_ID'
resource_group = 'YOUR_RESOURCE_GROUP'
vm_name = 'YOUR_VM_NAME'
Also customize the desired VM sizes:

night_vm_size = 'Standard_D4s_v3'    # Size at 11 PM
morning_vm_size = 'Standard_D8s_v3'  # Size at 7 AM
 How It Works
The script:

Checks the current hour.

If it’s 11 PM or 7 AM, it:

Stops the VM

Deallocates the VM (required before resizing)

Resizes the VM to the target size

Starts the VM again

⏱ Scheduling
You can schedule this script to run using:

 Linux cron job
Edit your crontab:


crontab -e
Add:

0 23 * * * /usr/bin/python3 /path/to/your/script.py  # At 11 PM
0 7 * * * /usr/bin/python3 /path/to/your/script.py   # At 7 AM
 Azure Automation / Azure Function
You can also package this script inside an Azure Function App or Azure Automation Runbook for a serverless solution.

🛡 Authentication Notes
This script uses:

from azure.identity import DefaultAzureCredential
Make sure one of the following authentication methods is configured:

Azure CLI login (az login)

Managed Identity (when running on Azure services)

Environment variables for Service Principal credentials

See Azure Identity Docs for more.

 License
MIT License

Contributions
Pull requests welcome. For major changes, open an issue first to discuss what you would like to change.


---

## File Structure

azure-vm-scheduler-resize/
├── README.md
├── resize_vm.py
├── requirements.txt


 requirements.txt
sql

azure-identity
azure-mgmt-compute
 Final Step: Push to GitHub
1. Initialize repo


git init
git add .
git commit -m "Initial commit: Azure VM time-based auto-resize script"
2. Create GitHub repository (e.g., via GitHub UI or CLI)
bash

gh repo create azure-vm-scheduler-resize --public --source=. --remote=origin
git push -u origin main
