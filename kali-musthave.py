#!/usr/bin/python2
import os, time
print('\033[96m Hello in kali musthave kali rules \033[0m\n\nso first update kali')
version = raw_input('but before update do you have the newest kali ? y/n')
def repofix():
    os.system(''' # Regular repositories
deb http://http.kali.org/kali sana main non-free contrib
deb http://security.kali.org/kali-security sana/updates main contrib non-free
# Source repositories
deb-src http://http.kali.org/kali sana main non-free contrib
deb-src http://security.kali.org/kali-security sana/updates main contrib non-free > /etc/apt/sources.list''')
if version == "y":
    repofix()
elif version == "n":
    repos = raw_input('so tell me if you have 2.x or 1.x kali (check at kali download page if higher then 2.x type 2.x)')
    if repos == "2.x":
        repofix()
    elif repos == "1.x":
        os.system("""echo '## Regular repositories
deb http://http.kali.org/kali kali main non-free contrib
deb http://security.kali.org/kali-security kali/updates main contrib non-free
## Source repositories
deb-src http://http.kali.org/kali kali main non-free contrib
deb-src http://security.kali.org/kali-security kali/updates main contrib non-free' > /etc/apt/sources.list""")

print('ignore apt warnings')
time.sleep(5)
os.system('apt update > /dev/null && apt upgrade -y > /dev/null && apt dist-upgrade -y > /dev/null && apt autoremove -y > /dev/null && apt autoclean && apt clean')
print('ok')
print('now some tools')
os.system('apt install -y git python3 python3-pip build-essential > /dev/null')
os.system('git clone https://github.com/arismelachroinos/lscript && cd lscript && chmod +x install.sh && ./install.sh')
os.system('apt install -y bleachbit preload aircrack-ng mdk3 pyrit alsa-utils cowpatty terminator websploit hydra metasploit-framework armitage routersploit hashcat tor proxychains ncat nmap zenmap lynis debsums debsecan clamav needrestart fail2ban apt-listbugs apt-listchanges debian-goodies')
print('done')
print('now this script will create a function to your system\nwhichupdates kali')
os.system("""function apt-updater {
	apt-get update &&
	apt-get dist-upgrade -Vy &&
	apt-get autoremove -y &&
	apt-get autoclean &&
	apt-get clean &&
	reboot
	}""")
print('type "apt-updater" any time to check and update system')
print('some bugs kali have now will be fixed...')
os.system('''echo "
[main]
plugins=ifupdown,keyfile

[ifupdown]
managed=true
"> /etc/NetworkManager/NetworkManager.conf''')
print('now have fun')
