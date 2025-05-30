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
# pip3 install requests beautifulsoup4 selenium clipboard pyautogui opencv-python numpy seleniumbase pillow Levenshtein paddlepaddle paddleocr pymongo pyperclip albumentations protobuf==3.19.6 numpy==1.23
pip3 install requests beautifulsoup4 selenium clipboard pyautogui opencv-python pillow pymongo pyperclip albumentations seleniumbase protobuf==3.19.6 numpy==1.23 tensorflow==2.10

sudo apt-get --fix-broken install -y
# Install additional tools
echo "Installing additional tools..."
sudo apt-get install -y gnome-screenshot python3-tk python3-dev xdotool nano xclip unzip
sudo apt-get --fix-broken install -y
# Set screen resolution (adjust VNC-0 if necessary)
echo "Setting screen resolution..."
#Docker VNC
xrandr --output VNC-0 --mode 1920x1080
#Nomachine
xrandr --output nxoutput0 --mode 1920x1080
#CRD 
#cvt 1920 1080 | grep Modeline | sed 's/Modeline //' | xargs -I{} bash -c 'xrandr --newmode {}; xrandr --addmode DUMMY0 1920x1080_60.00; xrandr --output DUMMY0 --mode 1920x1080_60.00'




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
# pip3 install requests beautifulsoup4 selenium clipboard pyautogui opencv-python numpy seleniumbase pillow Levenshtein paddlepaddle paddleocr pymongo pyperclip albumentations

pip3 install requests beautifulsoup4 selenium clipboard pyautogui opencv-python pillow pymongo pyperclip albumentations seleniumbase protobuf==3.19.6 numpy==1.23 tensorflow==2.10
sudo apt-get --fix-broken install -y
# Install additional tools
echo "Installing additional tools..."
sudo apt-get install -y gnome-screenshot python3-tk python3-dev xdotool nano xclip unzip
sudo apt-get --fix-broken install -y
# Set screen resolution (adjust VNC-0 if necessary)
echo "Setting screen resolution..."
#Docker VNC
#Nomachine
xrandr --output nxoutput0 --mode 1920x1080
#CRD 
#cvt 1920 1080 | grep Modeline | sed 's/Modeline //' | xargs -I{} bash -c 'xrandr --newmode {}; xrandr --addmode DUMMY0 1920x1080_60.00; xrandr --output DUMMY0 --mode 1920x1080_60.00'


# Download and unzip Mysterium extension
echo "Downloading and unzipping Mysterium extension..."
wget "https://clients2.googleusercontent.com/crx/blobs/AR5vvTqubtVV5aVepSABGlBG3y7lsxqE1_eZ9CC1AW2HJIros4Z6vxBZeicez6ODrI5S6G9akqmKxINYfSxFCvLJK-qwgRrhUFkYfAm0_6G4YfOgO-P6PfMspiS1zOv-30c4AMZSmuVj573y_tqmiWcnYlmz-GmfpizZvA/DCLJFNHBJPILFPMIMIPCIJGAALCABFHD_0_1_0_0.crx" -O mysterium.crx
unzip mysterium.crx -d /root/Desktop/MFV6/mysterium

echo "Downloading and unzipping Nopecha extension..."
#wget "https://clients2.googleusercontent.com/crx/blobs/AcmIXbrz5n5n20GheS_lg8yGIViuaI00kaUGYG1ZVDsBnlYmSGluVOL6eSBuNAQIykyXskweoJkFzIFatZ2QEXptjD0yYTrdd9D1OTaOuMoMbwx-YCXo82Xa2OvgBBtJWlYAxlKa5aVDHDIJjtACXFP2BUTteh5yUFO5/DKNLFMJAANFBLGFDFEBHIJALFMHMJJJO_0_4_13_0.crx" -O nopecha.crx
#unzip nopecha.crx -d /root/Desktop/MFV6/nopecha
wget "https://clients2.googleusercontent.com/crx/blobs/ASuc5ohGlp7ofDsduxHtqPH1uRkA_M55xHyVGoJ4GFY5GDEiSXJCvW_VHNlkAeOyuHiWcmrpa0IQUVrk9ZoFFGXxH8CbualwmLRlw4_swsm286afNdBDQkhhk5qzKViQdzcAxlKa5ecqpB4LS_8m_Qaz0chfTFrHzQ5C/FCALILBNPKFIKDPPPPPPCHMKDIPIBALB_1_0_2_0.crx" -O nopecha.crx
unzip nopecha.crx -d /root/Desktop/MFV6/nopecha
wget "https://clients2.googleusercontent.com/crx/blobs/ASuc5ojOrckBacBROw2WjBg0y2rCSlEmnTGYSbv43ai7PG35Yxp168oIkvwaFbQyWZjnAUYMM-Yom6dIBZbNKazKoq7maAa6YuAEKdvxb3sa0alz6Scrv2N2AcUTogHfvY8AxlKa5XDlU02UakYNR2jSctFX-tue5dvt/BKMMLBLLPJDPGCGDOHBAGHFAECNDDHNI_0_2_4_0.crx" -O fingerprint.crx
unzip fingerprint.crx -d /root/Desktop/MFV6/fingerprint
echo "Installation completed successfully!"


echo "Installation completed successfully!"
