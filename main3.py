import subprocess
import sys

def install_selenium():
    print("--- Starting Selenium Setup ---")
    
    try:
        # Step 1: Install the selenium package using pip
        print("Installing Selenium library...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium"])
        print("Successfully installed Selenium.")

        # Step 2: Verify the installation
        import selenium
        print(f"Verification successful! Selenium version: {selenium.__version__}")
        
        print("\nNote: Make sure you have Google Chrome (or Firefox) installed.")
        print("Modern Selenium (v4.6+) handles drivers automatically—no manual download needed!")

    except Exception as e:
        print(f"An error occurred during installation: {e}")

if __name__ == "__main__":
    install_selenium()
