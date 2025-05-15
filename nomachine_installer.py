#!/bin/bash

# Ensure the script is run as root
if [[ $EUID -ne 0 ]]; then
   echo "❌ This script must be run as root" 
   exit 1
fi

echo "🛠️ Updating and installing XFCE desktop environment..."
apt update && apt upgrade -y
DEBIAN_FRONTEND=noninteractive apt install -y xfce4 xfce4-goodies xterm

echo "🖥️ Installing NoMachine..."
wget https://www.nomachine.com/free/linux/64/deb -O nomachine.deb
dpkg -i nomachine.deb || apt -f install -y

# Check if installation succeeded
if systemctl is-active --quiet nxserver; then
    echo "✅ NoMachine service is active."
else
    echo "❌ NoMachine failed to start. Trying to start it manually..."
    systemctl start nxserver
fi

# Allow NoMachine port
echo "🌐 Allowing NoMachine port (4000)..."
ufw allow 4000/tcp || echo "⚠️ UFW not active or not installed. Skipping firewall config."

# Display VPS IP address
IP=$(curl -s ifconfig.me)
echo -e "\n✅ Installation Complete!"
echo "🌐 Connect via NoMachine using this IP: $IP"
echo "👤 Username: root (or any user you prefer)"
echo "🔑 Use the password you set for root login"
