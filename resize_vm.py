
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from datetime import datetime


subscription_id = 'YOUR_SUBSCRIPTION_ID'
resource_group = 'YOUR_RESOURCE_GROUP'
vm_name = 'YOUR_VM_NAME'

night_vm_size = 'Standard_D4s_v3'    # Size for 11 PM
morning_vm_size = 'Standard_D8s_v3'  # Size for 7 AM

current_hour = datetime.now().hour

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)

# 🎯 Decide time-based action
if current_hour == 23:
    selected_size = night_vm_size
    print("🕚 11 PM: Performing stop → resize → start")
elif current_hour == 7:
    selected_size = morning_vm_size
    print(" 7 AM: Performing stop → resize → start")
else:
    print(" Not scheduled time. Exiting.")
    exit()


print("Stopping VM...")
compute_client.virtual_machines.begin_power_off(resource_group, vm_name).result()


print("Deallocating VM...")
compute_client.virtual_machines.begin_deallocate(resource_group, vm_name).result()

print(f"Resizing VM to {selected_size}...")
vm = compute_client.virtual_machines.get(resource_group, vm_name)
vm.hardware_profile.vm_size = selected_size
compute_client.virtual_machines.begin_create_or_update(resource_group, vm_name, vm).result()

print("Starting VM...")
compute_client.virtual_machines.begin_start(resource_group, vm_name).result()

print(" VM resized and restarted successfully.")
