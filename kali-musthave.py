#!/usr/bin/python2
import os, time
print('\033[96m Hello in kali musthave kali rules \033[0m\n\nso first update to latest kali')
print('ignore apt warnings')
time.sleep(5)
os.system('apt update > /dev/null && apt upgrade -y > /dev/null && apt dist-upgrade -y > /dev/null && apt autoremove -y > /dev/null && apt autoclean && apt clean')
print('ok')
print('now some tools')
os.system('apt install -y git python3 python3-pip build-essential > /dev/null')
os.system('git clone https://github.com/arismelachroinos/lscript && cd lscript && chmod +x install.sh && ./install.sh')
os.system('apt install -y aircrack-ng websploit routersploit hashcat ncat nmap zenmap lynis debsums debsecan clamav needrestart fail2ban apt-listbugs apt-listchanges debian-goodies')
print('done\nok have fun')
