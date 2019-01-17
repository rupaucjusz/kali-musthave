#!/usr/bin/python2
import os, time
print('\033[96m Hello in kali musthave kali rules \033[0m\n\nso first update kali') #really like kali
os.system("echo 'deb http://http.kali.org/kali kali-rolling main non-free contrib\ndeb-src http://http.kali.org/kali kali-rolling main non-free contrib' > /etc/apt/sources.list") #that will remove your actual sources.list
os.system('''dpkg --add-architecture i386
apt update
apt upgrade -y
apt full-upgrade -y
apt dist-upgrade -y
apt autoremove
apt autoclean
apt clean
''') #added 32 bit support and upgrade system
print('ok')
print('now some tools') #and other stuff wich will be useful
os.system('apt install -y git python3 python3-pip build-essential')
os.system('apt install -y sublist3r eyewitness open-vm-tools-desktop fuse exfat-utils exfat-fuse python3-bs4 libreoffice network-manager-openvpn-gnome network-manager-openconnect-gnome wine html2text ntpdate bleachbit preload aircrack-ng mdk3 pyrit alsa-utils cowpatty terminator websploit hydra metasploit-framework armitage routersploit hashcat tor proxychains ncat nmap zenmap lynis debsums debsecan clamav needrestart fail2ban apt-listbugs apt-listchanges debian-goodies')
print('done')
print('some bugs kali have now will be fixed...')
os.system('''echo "
[main]
plugins=ifupdown,keyfile

[ifupdown]
managed=true
" > /etc/NetworkManager/NetworkManager.conf''')
print("done\nscript will enable dark-theme")#your eyes should say "thank u"
os.system("echo '[Settings]' > /root/.config/gtk-3.0/settings.ini\necho 'gtk-application-prefer-dark-theme=1' >> /root/.config/gtk-3.0/settings.ini")
print('some good pip stuff')
os.system('pip install --upgrade pip\npip install whatportis\npip install pinggraph')
print('last thing script will do is adding syntax to vim')#if u know how to exit vim xD
os.system('echo "syntax on" >> /root/.vimrc')
print('now have fun')
