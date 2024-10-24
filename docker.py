import os

# Step 1: Install open-vm-tools if it's not already installed
def install_vm_tools():
    os.system("sudo apt-get update")
    os.system("sudo apt-get install -y open-vm-tools open-vm-tools-desktop")

# Step 2: Set the VMware copy-paste and drag-drop options in the .vmx file (as needed)
def set_vmx_file_settings(vmx_file_path):
    try:
        with open(vmx_file_path, 'a') as vmx_file:
            vmx_file.write('\nisolation.tools.copy.disable = "FALSE"')
            vmx_file.write('\nisolation.tools.paste.disable = "FALSE"')
            vmx_file.write('\nisolation.tools.setGUIOptions.enable = "TRUE"')
        print("VMX settings updated successfully!")
    except Exception as e:
        print(f"Failed to update VMX file: {e}")

# Step 3: Install Docker prerequisites and Docker itself
def install_docker():
    os.system("sudo apt-get update")
    os.system("sudo apt-get install -y ca-certificates curl gnupg lsb-release")
    os.system('sudo mkdir -m 0755 -p /etc/apt/keyrings')
    os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo tee /etc/apt/keyrings/docker.gpg > /dev/null')
    os.system('echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
    os.system("sudo apt-get update")
    os.system("sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin")
    print("Docker installed successfully!")

# Step 4: Start networking service (optional, in case networking was disabled)
def restart_networking():
    os.system("sudo systemctl restart networking")
    os.system("sudo ip link set dev ens33 up")

# Call functions in order to execute the required tasks
install_vm_tools()              # Step 1: Install VMware Tools
set_vmx_file_settings("/path/to/your/vmname.vmx")  # Step 2: Update VMX settings
install_docker()                # Step 3: Install Docker
restart_networking()            # Step 4: Restart networking services
