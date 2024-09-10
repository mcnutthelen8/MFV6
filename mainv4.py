import os
import subprocess

# User inputs
CRD_SSH_Code = input("Enter your Google CRD SSH Code: ")
username = "hello"  # Replace with your desired username
password = "world"  # Replace with your desired password
Pin = 234567  # Replace with your desired PIN
Autostart = True  # Set to True if you want autostart to be enabled

class CRDSetup:
    def __init__(self, user):
        # Initial setup
        self.update_system()
        self.install_crd()
        self.install_desktop_environment()
        self.configure_user(user)
        self.finish_setup(user)

    @staticmethod
    def update_system():
        """Update package lists."""
        subprocess.run(['apt', 'update'], check=True)
    
    @staticmethod
    def install_crd():
        """Install Chrome Remote Desktop."""
        subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'], check=True)
        subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'], check=True)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], check=True)
        print("Chrome Remote Desktop installed successfully!")

    @staticmethod
    def install_desktop_environment():
        """Install XFCE4 desktop environment."""
        subprocess.run(['apt', 'install', '--assume-yes', 'xfce4', 'desktop-base', 'xfce4-terminal'], check=True)
        with open('/etc/chrome-remote-desktop-session', 'w') as f:
            f.write("exec /etc/X11/Xsession /usr/bin/xfce4-session\n")
        subprocess.run(['apt', 'remove', '--assume-yes', 'gnome-terminal'], check=True)
        subprocess.run(['apt', 'install', '--assume-yes', 'xscreensaver'], check=True)
        subprocess.run(['apt', 'purge', '--assume-yes', 'light-locker'], check=True)
        subprocess.run(['apt', 'install', '--reinstall', 'xfce4-screensaver'], check=True)
        subprocess.run(['systemctl', 'disable', 'lightdm.service'], check=True)
        print("XFCE4 Desktop Environment installed successfully!")

    @staticmethod
    def configure_user(user):
        """Create a user and set permissions."""
        subprocess.run(['useradd', '-m', user], check=True)
        subprocess.run(['adduser', user, 'sudo'], check=True)
        subprocess.run(['sh', '-c', f"echo '{user}:{password}' | chpasswd"], check=True)
        subprocess.run(['sed', '-i', 's/\/bin\/sh/\/bin\/bash/g', '/etc/passwd'], check=True)
        print(f"User {user} created and configured successfully!")

    @staticmethod
    def finish_setup(user):
        """Finish setting up Chrome Remote Desktop and autostart."""
        if Autostart:
            autostart_dir = f"/home/{user}/.config/autostart"
            os.makedirs(autostart_dir, exist_ok=True)
            link = "https://www.youtube.com/@The_Disala"
            colab_autostart = f"""[Desktop Entry]
Type=Application
Name=Colab
Exec=sh -c "sensible-browser {link}"
Icon=
Comment=Open a predefined notebook at session sign-in.
X-GNOME-Autostart-enabled=true"""
            autostart_file = f"{autostart_dir}/colab.desktop"
            with open(autostart_file, "w") as f:
                f.write(colab_autostart)
            subprocess.run(['chmod', '+x', autostart_file], check=True)
            subprocess.run(['chown', f"{user}:{user}", '/home/{user}/.config'], check=True)
            print("Autostart configuration completed!")

        subprocess.run(['adduser', user, 'chrome-remote-desktop'], check=True)
        command = f"{CRD_SSH_Code} --pin={Pin}"
        subprocess.run(['su', '-', user, '-c', command], check=True)
        subprocess.run(['service', 'chrome-remote-desktop', 'start'], check=True)

        print(f"Setup completed!\nLog in PIN: {Pin}\nUsername: {username}\nPassword: {password}")

try:
    if not CRD_SSH_Code:
        print("Please enter the auth code from the provided link.")
    elif len(str(Pin)) < 6:
        print("PIN must be at least 6 digits long.")
    else:
        CRDSetup(username)
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
