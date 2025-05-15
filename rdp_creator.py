import os
import subprocess

# === User Config ===
CRD_SSH_Code = input("Google CRD SSH Code: ")
username = os.getlogin()  # current user
password = "your_password"  # optional, used only if setting or resetting
Pin = 123456

# === Basic sanity checks ===
if not CRD_SSH_Code.strip():
    print("Please enter a valid CRD SSH code.")
    exit(1)
if len(str(Pin)) < 6:
    print("PIN must be at least 6 digits.")
    exit(1)

# === Install Chrome Remote Desktop ===
subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'])
subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'])
subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
print("[✓] Chrome Remote Desktop Installed")

# === Install XFCE4 Desktop Environment ===
os.environ["DEBIAN_FRONTEND"] = "noninteractive"
subprocess.run(["apt", "install", "--assume-yes", "xfce4", "desktop-base", "xfce4-terminal", "xscreensaver"])
os.system("echo 'exec /etc/X11/Xsession /usr/bin/xfce4-session' > /etc/chrome-remote-desktop-session")
os.system("apt purge --assume-yes light-locker || true")
os.system("apt install --reinstall -y xfce4-screensaver")
os.system("systemctl disable lightdm.service || true")
print("[✓] XFCE4 Desktop Environment Installed")

# === Add current user to chrome-remote-desktop group ===
os.system(f"adduser {username} chrome-remote-desktop")

# === Authorize CRD with PIN ===
crd_command = f"{CRD_SSH_Code} --pin={Pin}"
os.system(crd_command)
os.system("service chrome-remote-desktop start")

print("\n[✓] CRD setup complete. You can now connect via https://remotedesktop.google.com/")
print(f"[INFO] Username: {username} | PIN: {Pin}")
