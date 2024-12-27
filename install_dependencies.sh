#!/bin/bash

# Update package list
echo "Updating package list..."
sudo apt-get update

# Fix broken dependencies
echo "Fixing broken dependencies..."
sudo apt-get --fix-broken install -y

# Install Python core dependencies
echo "Installing Python core dependencies..."
sudo apt-get install -y fonts-liberation libgbm1 libnspr4 libnss3 libu2f-udev libvulkan1 xdg-utils xprintidle
sudo apt-get --fix-broken install -y
# Install Google Chrome
echo "Installing Google Chrome..."
#wget --no-check-certificate 'https://drive.usercontent.google.com/download?id=1GbKsnazR8h3xTrUN5TrKWdXaBO3nudQ5&export=download&authuser=0&confirm=t&uuid=670b57f0-98b1-4df0-b37a-3715e9fc2a31&at=AENtkXZITd_FNy6jafHDjzeJ76lk%3A1731453427695' -O google-chrome-stable_current_amd64.deb
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

# Fix any dependency issues caused by Google Chrome installation
sudo apt-get --fix-broken install -y

# Install pip and Python packages
echo "Installing pip and Python packages..."
sudo apt-get install -y python3-pip
pip3 install requests beautifulsoup4 selenium clipboard pyautogui opencv-python numpy seleniumbase pillow Levenshtein paddlepaddle paddleocr pymongo pyperclip albumentations
sudo apt-get --fix-broken install -y
# Install additional tools
echo "Installing additional tools..."
sudo apt-get install -y gnome-screenshot python3-tk python3-dev xdotool nano xclip unzip
sudo apt-get --fix-broken install -y
# Set screen resolution (adjust VNC-0 if necessary)
echo "Setting screen resolution..."
xrandr --output VNC-0 --mode 1920x1080




# Update package list
echo "Updating package list..."
sudo apt-get update

# Fix broken dependencies
echo "Fixing broken dependencies..."
sudo apt-get --fix-broken install -y

# Install Python core dependencies
echo "Installing Python core dependencies..."
sudo apt-get install -y fonts-liberation libgbm1 libnspr4 libnss3 libu2f-udev libvulkan1 xdg-utils xprintidle


sudo apt-get --fix-broken install -y
# Install Google Chrome
echo "Installing Google Chrome..."
#wget --no-check-certificate 'https://drive.usercontent.google.com/download?id=1GbKsnazR8h3xTrUN5TrKWdXaBO3nudQ5&export=download&authuser=0&confirm=t&uuid=670b57f0-98b1-4df0-b37a-3715e9fc2a31&at=AENtkXZITd_FNy6jafHDjzeJ76lk%3A1731453427695' -O google-chrome-stable_current_amd64.deb
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

# Fix any dependency issues caused by Google Chrome installation
sudo apt-get --fix-broken install -y

# Install pip and Python packages
echo "Installing pip and Python packages..."
sudo apt-get install -y python3-pip
pip3 install requests beautifulsoup4 selenium clipboard pyautogui opencv-python numpy seleniumbase pillow Levenshtein paddlepaddle paddleocr pymongo pyperclip albumentations
sudo apt-get --fix-broken install -y
# Install additional tools
echo "Installing additional tools..."
sudo apt-get install -y gnome-screenshot python3-tk python3-dev xdotool nano xclip unzip
sudo apt-get --fix-broken install -y
# Set screen resolution (adjust VNC-0 if necessary)
echo "Setting screen resolution..."
xrandr --output VNC-0 --mode 1920x1080

# Download and unzip Mysterium extension
echo "Downloading and unzipping Mysterium extension..."
wget "https://clients2.googleusercontent.com/crx/blobs/AVsOOGhXta8-UhRWEUcB2CckwYwwFI6WMiZ8b-CxyBlFaRSv-8wsJGQEG3lL_ILVoKOmDEowQmnAnB2cwNoa3h3lbPBUsTP376PSoi8nM_fjkQSkoiDkoTx0-5M5j9WIdrlaAMZSmuUvAQiNCBMqU-HcXaveN1nJlDMohw/DCLJFNHBJPILFPMIMIPCIJGAALCABFHD_0_0_1_0.crx" -O mysterium.crx
unzip mysterium.crx -d /root/Desktop/MFV6/mysterium

echo "Installation completed successfully!"


echo "Installation completed successfully!"
