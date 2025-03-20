import os
import subprocess

def install_dependencies():
    print("📦 Installing dependencies...")
    subprocess.run(["pip", "install", "requests", "fpdf"], check=True)

def configure_api_key():
    api_key = input("🔑 Enter your AbuseIPDB API key: ")
    config_content = f'ABUSE_IPDB_API_KEY = "{api_key}"\n'
    with open("config.py", "w") as config_file:
        config_file.write(config_content)
    print("✅ API key saved to config.py")

def run_program():
    print("🚀 Running the program...")
    subprocess.run(["python", "main.py"], check=True)

def main():
    install_dependencies()
    configure_api_key()
    run_program()

if __name__ == "__main__":
    main()