#!/usr/bin/python2
import os, time
print('\033[96m Hello in kali musthave kali rules \033[0m\n\nso first update kali')
os.system("echo 'deb http://http.kali.org/kali kali-rolling main non-free contrib\ndeb-src http://http.kali.org/kali kali-rolling main non-free contrib' > /etc/apt/sources.list")
os.system('apt update && apt upgrade -y && apt dist-upgrade -y && apt autoremove -y && apt autoclean && apt clean')
print('ok')
print('now some tools')
os.system('apt install -y git python3 python3-pip build-essential')
os.system('apt install -y bleachbit preload aircrack-ng mdk3 pyrit alsa-utils cowpatty terminator websploit hydra metasploit-framework armitage routersploit hashcat tor proxychains ncat nmap zenmap lynis debsums debsecan clamav needrestart fail2ban apt-listbugs apt-listchanges debian-goodies')
print('done')
print('some bugs kali have now will be fixed...')
os.system('''echo "
[main]
plugins=ifupdown,keyfile

[ifupdown]
managed=true
" > /etc/NetworkManager/NetworkManager.conf''')
print('now have fun')
