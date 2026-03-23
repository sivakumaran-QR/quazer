# Quazer
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  [![GitHub stars](https://img.shields.io/github/stars/sivakumaran-QR/Quazer?style=flat-square)](https://github.com/sivakumaran-QR/Quazer/stargazers)

Shadow Key Detector With Inbuilt Commit Blocker

Stop committing secrets. Automatically.

This project is licensed under **MIT**.

**you may modify with the permission of author allows**

# Usage

Quazer- Detects and blocks API keys, tokens, and sensitive data before they hit Git. 

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


