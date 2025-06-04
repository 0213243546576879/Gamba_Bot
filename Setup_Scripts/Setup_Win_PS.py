import os

os.system('echo "Setting up Venv..."')
os.system('python -m venv "..\\.venv"')
os.system('echo "Updating pip"')
os.system('..\\.venv\\Scripts\\python.exe -m pip install --upgrade pip')
os.system('echo "Installing Packages..."')
os.system('..\\.venv\\Scripts\\pip3.13.exe install -r ..\\requirements.txt')
os.system('echo "Complete"')
