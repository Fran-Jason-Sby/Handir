__CodeBy__  = "Jason"
__Username__ = "F.R.J"
__Version__  = "2.7"                                                                                 import os
try:                                                                                                     import requests
except ImportError:
    print('\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91m requests is not installed')                       print('\033[1;97m[\033[1;92m*\033[1;97m] Installing requests')
    os.system('pip install requests')                                                                import os, sys, requests, time, json, datetime
def mkdir(z):
    for e in z + '\n':
        sys.stdout.write(e)                                                                                  sys.stdout.flush()
        time.sleep(0.0001)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
question = "\033[1;97m[\033[1;96m?\033[1;97m] "
eror = "\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91m "
ok = "\033[1;97m[\033[1;92m✓\033[1;97m] "
wn = "\033[1;97m[\033[1;92m*\033[1;97m] "
logo = """\033[1;97m  _________ ___ ___    __________________________
 /   _____//   |   \  /  _  \\______   \_   _____/
 \_____  \/    ~    \/  /_\  \|       _/|    __)_
 /        \    Y    /    |    \    |   \|        \
/_______  /\___|_  /\____|__  /____|_  /_______  /
        \/       \/         \/       \/        \/
\033[1;30m[•]AUTHOR   :\33[1;33m JASON
\033[1;30m[•]USERNAME :\33[1;33m F.R.J
\033[1;30m|=================================================|
"""
f= "\033[1;30m==============================================================="
def main():
    clear()
    mkdir(logo)
    input ('[•]masukan token facebook.!! disarankan menggunakan akun tumbal[klik ENTER]')
    token = input(question+'Masukan Token =>')
    mkdir(wn+'Memeriksa Token...')
    try:
        k = requests.get('https://graph.facebook.com/me?access_token='+token)
        kk = json.loads(k.text)
        name = kk['name']
        idfb = kk['id']
        mkdir(ok+'Login Berhasil')
        time.sleep(3)
    except:
        mkdir(eror+'Invalid Token')
        os.sys.exit()
    clear()
    mkdir(logo)
    mkdir(ok+'Name Akun : '+name)
    mkdir(ok+'ID Akum   : '+idfb)
    mkdir(f)
    idpost = input(question+'ID Post:')
    mkdir(f)
    time_delay = int(input(question+'Waktu Share:'))
    clear()
    mkdir(logo)
    kha = 0
    kha = kha + 1
    while True:
        requests.get('https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE>
        print('\033[1;97m[\033[1;92m✓\033[1;97m]--[\033[1;96mBerhasil\033[1;97m]--[\033[1;93m'+str(i>
        time.sleep(time_delay)
main()