#!/bin/bash

# Must run as root
if [[ $EUID -ne 0 ]]; then
    echo "❌ Run as root."
    exit 1
fi

echo "🛠️ Updating system..."
apt update && apt upgrade -y

echo "📦 Installing XFCE desktop..."
DEBIAN_FRONTEND=noninteractive apt install -y xfce4 xfce4-goodies xterm

echo "🌐 Installing NoMachine..."
wget https://www.nomachine.com/free/linux/64/deb -O nomachine.deb
dpkg -i nomachine.deb || apt install -f -y

echo "🧯 Disabling lightdm (if exists)..."
systemctl disable lightdm || true

echo "🌐 Opening NoMachine port (4000)..."
ufw allow 4000/tcp || echo "⚠️ UFW not active, skipping firewall rules."

IP=$(curl -s ifconfig.me)
echo -e "\n✅ Done! Connect using NoMachine to: $IP"
echo "🔑 Login as: root (or other user you set)"
