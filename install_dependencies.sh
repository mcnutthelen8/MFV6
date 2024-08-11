#!/bin/bash

# Update package list
echo "Updating package list..."
sudo apt-get update

# Install Python core dependencies
echo "Installing Python core dependencies..."
sudo apt-get -f install -y --force-yes
sudo apt-get install -y fonts-liberation libgbm1 libnspr4 libnss3 libu2f-udev libvulkan1 xdg-utils

# Install Google Chrome
echo "Installing Google Chrome..."
cd /tmp
sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get -f install -y --force-yes
sudo dpkg -i google-chrome-stable_current_amd64.deb

# Install pip and Python packages
echo "Installing pip and Python packages..."
sudo apt install -y python3-pip
pip install requests beautifulsoup4 selenium clipboard pyautogui opencv-python numpy seleniumbase pillow

# Install additional tools
echo "Installing additional tools..."
sudo apt install -y gnome-screenshot
sudo apt-get install -y python3-tk python3-dev
sudo apt install -y xdotool
sudo apt install -y nano

echo "Installation completed successfully!"
