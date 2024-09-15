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
pip install requests 
pip install beautifulsoup4
pip install selenium 
pip install clipboard 
pip install pyautogui 
pip install opencv-python 
pip install numpy 
pip install seleniumbase 
pip install pillow 
pip install Levenshtein 
pip install paddlepaddle 
pip install paddleocr 
pip install pymongo 
pip install pyperclip
#pip install mysql-connector-python

# Install additional tools
echo "Installing additional tools..."
sudo apt install -y gnome-screenshot
sudo apt-get install -y python3-tk python3-dev
sudo apt install -y xdotool
sudo apt install -y nano
sudo apt-get install xclip
sudo apt-get update
xrandr --output VNC-0 --mode 1920x1080
sudo apt install unzip
wget "https://clients2.googleusercontent.com/crx/blobs/AVsOOGhXta8-UhRWEUcB2CckwYwwFI6WMiZ8b-CxyBlFaRSv-8wsJGQEG3lL_ILVoKOmDEowQmnAnB2cwNoa3h3lbPBUsTP376PSoi8nM_fjkQSkoiDkoTx0-5M5j9WIdrlaAMZSmuUvAQiNCBMqU-HcXaveN1nJlDMohw/DCLJFNHBJPILFPMIMIPCIJGAALCABFHD_0_0_1_0.crx" -O mysterium.crx
#wget "https://clients2.googleusercontent.com/crx/blobs/AVsOOGj770VyacuboorG752M_MoplMXpBqv27gaGClAoAPeW92og_XcYErayPTq6isteFYXVGH-1-3b2N0R1CqL_2W1il76ss8wS5mm3w7ZLiHXE93yBpXDSXVZoznOZBPEAxlKa5bvVqk7IzuoqSHwWklCswZPR2Hsg/HLKENNDEDNHFKEKHGCDICDFDDNKALMDM_1_13_0_0.crx" -O cookie.crx
#wget "https://clients2.googleusercontent.com/crx/blobs/AVsOOGjQdui7oibybsnwnagZ_gz6_Zu_CSxKFbJpSbPGQSjDvf5FQBwps0BbXAAISoLmOfERqxVo_sGsBxUIAqX3N52hc5TZ4WXLPVNRnq6hp2Mjrb6FAMZSmuVHB-8YWXsgMMqOWnMm_jDpP5G-qw/MEOJNMFHJKAHLFCECPDCDGJCLCILMAIJ_1_0_5_0.crx" -O fingerprint.crx
#wget "https://clients2.googleusercontent.com/crx/blobs/AVsOOGhiVwWZyTfRn1a8tz5BGGIwjYMKxyrBvu_w00IgX7TjhJ-wiNAFbK_Use5iSp-upY6IKcIOi6jHcokx9kWzZmvxh4NmcKVVezMq81m9LqFP5NIuaTLugxHck9UHYvQAxlKa5V1Z0fOQGbAyy2lS51SFYNnB33uU/DKNLFMJAANFBLGFDFEBHIJALFMHMJJJO_0_4_12_0.crx" -O nopecha.crx

unzip mysterium.crx -d /root/Desktop/MFV6/mysterium
#unzip cookie.crx -d /root/Desktop/MFV6/cookie
#unzip fingerprint.crx -d /root/Desktop/MFV6/fingerprint
#unzip nopecha.crx -d /root/Desktop/MFV6/nopecha

echo "Installation completed successfully!"
