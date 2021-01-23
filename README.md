# Introduction 
The MMP DAO models

# Installation
1. Setup Environment
    ```powershell
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    choco install git -y
    choco install python --version=3.7.6 -y
    ```

2. Install packages
    ```cmd
    python -m venv venv
    venv\Scripts\Activate.bat
    pip install wheel
    pip install -r requirements.txt
    ```

# Getting Started
1. Build wheel
   ```shell
   python setup.py bdist_wheel
   ```
2. Go to your project which install this project
3. `pip install [target project path]/dist/daomodel-0.1.0-py3-none-any.whl` 此處的[target project path]指的是從git下下來的wimmp-backend project
