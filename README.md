# Quazer

Shadow Key Detector With Inbuild Commit Blocker 
Stop Committing Secrets Before Attackers Harvest Now Decrypt Later

# Usage

CLI-tool For Detect  Shadow Keys and Block Commit If Shadow Key Exist With Low False Rate

# Installation  Steps
pip install git+https://github.com/sivakumaran-QR/quazer.git

(Go to your project folder)
cd your-project-folder

Initsalize Git (if not already)
git init

Enable Quazer
python -m quazer init
This installs a Git pre-commit hook to protect your project.

(Usage)
Scan your project manually
python -m quazer run
Automatic protection (recommended)

Once initialized, Quazer runs automatically on every commit:
git add .
git commit -m "your message"

# Demo (How Quazer Works)
C:\Users\siva>cd desktop

C:\Users\siva\Desktop>cd test

C:\Users\siva\Desktop\test>git init

Reinitialized existing Git repository in C:/Users/siva/Desktop/test/.git/

C:\Users\siva\Desktop\test>python -m quazer init

✅ Quazer hook installed

C:\Users\siva\Desktop\test>python -m quazer run

❌ Secrets detected! Commit blocked.
AWS Key in .\text.py.txt:1
Private Key in .\text.py.txt:2
Structured Secret in .\keys\keymin.py.txt:1
AWS Key in .\keys\keymin.py.txt:3

# What Quazer Detects
AWS Access Keys , 
Private Keys  , 
Generic API Keys  ,
Structured Secrets (custom patterns)  ,
High-entropy secrets

# Risk Of Not Using Quazer 
Attackers Can Harvest Now Decrypt Later
Total Number Of Shadow keys apporx in world are 1.1B KEYS 



