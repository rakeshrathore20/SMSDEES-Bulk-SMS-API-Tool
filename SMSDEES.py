﻿
from botocore.utils import FileWebIdentityTokenLoader
import requests, requests, re, sys, random, time, os, warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
from colorama import *
from colorama import Fore, Back, init, Style
init(autoreset=True)
from random import choice
import webbrowser, subprocess, multiprocessing

bl = Fore.BLACK
wh = Fore.WHITE
yl = Fore.YELLOW
red = Fore.RED
res = Style.RESET_ALL
gr = Fore.GREEN
ble = Fore.BLUE
cy = Fore.CYAN
bwh = Back.WHITE
byl = Back.YELLOW
bred = Back.RED
bgr = Back.GREEN

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)


def main():
    os.system('title SMSDEES')
    os.system('cls')
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = f'''
                                   _____ __  __  _____   _____  ______  ______  _____  
                                   / ____|  \/  |/ ____| |  __ \|  ____|  ____|/ ____| 
                                   | (___ | \  / | (___  | |  | | |__  | |__  | (___   
                                   \___ \| |\/| |\___ \ | |  | |  __| |  __|  \___ \  
                                   ____) | |  | |____) || |__| | |____| |____ ____) | 
                                  |_____/|_|  |_|_____/ |_____/|______|______|_____/         
       
                         
                                  TOOL BY. RAKESH KUMAR
                       ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
              ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
              ┃   [ 1 ] Nexmo Bulk SMS Sender              [ 8 ] Telnyx Bulk SMS Sender          ┃
              ┃   [ 2 ] Twilio Bulk SMS Sender             [ 9  ] Telesign Bulk SMS Sender       ┃
              ┃   [ 3 ] Plivo Bulk SMS Sender              [ 10 ] Amazon SNS Bulk SMS Sender     ┃
              ┃   [ 4 ] Messagebird Bulk SMS Sender        [ 11 ] Phone Number Generator         ┃
              ┃   [ 5 ] Send99 Bulk SMS Sender             [ 12 ] Phone Checker [Live/Die]       ┃
              ┃   [ 6 ] Proovl Bulk SMS Sender             [ 13 ] Phone checker Filter Carrier   ┃
              ┃   [ 7 ] TextBelt Bulk SMS Sender                                                 ┃
              ┃                                                                                  ┃
              ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                          
                            
    '''
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
        time.sleep(0.05)

    xc = int(input(f'SMSDEES@ Select Your SMS API Provider '))
    if xc == 5:

        def send99():
            os.system('title Send99 Bulk SMS Sender')
            os.system('cls')
            checked = open(sent, 'a')
            print(f'''


{gr}
       _____ _______   ______  ____  ____ 
 {red}/ ___// ____/ | / / __ \/ __ \/ __ \
 {yl} \__ \/ __/ /  |/ / / / / /_/ / /_/ /
 {yl}___/ / /___/ /|  / /_/ /\__, /\__, / 
{cy}/____/_____/_/ |_/_____//____//____/  
{res}
            ''')
            print('============= Setup Api ==================')
            f1 = input('Enter Your API ID : ')
            print('=======================================================')
            f2 = input('Enter Your API PASSWORD : ')
            print('=======================================================')
            msg = open('config/message.txt').read()
            
            phone = open('config/phone.txt').read().splitlines()
            
            print('Total Numbers => ' + Fore.GREEN + str(len(phone)))
            
            slowprint('Connecting DataBase .........')
            print('=======================================================')
            
            time.sleep(2)
            for i in phone:
                link = 'http://api2.send99.com/api/SendSMS'
                params = {'api_id':f1, 
                 'api_password':f2, 
                 'sms_type':'P', 
                 'encoding':'T', 
                 'sender_id':'INFO', 
                 'phonenumber':i, 
                 'textmessage':msg}
                resp = requests.get(link, params=params)
                job = resp.text
                search = re.search('"status":"S"', job)
                if search:
                    checked.write('Send Ok => ' + i + '\n')
                    print(f'{bgr}Phone :{res}{yl} {str(i)}  {res} ==> {gr}Send Ok ! {res}')
                    print('=======================================================')
                else:
                    print(f'{bred}Phone :{res} {yl} {str(i)}  {res} ==> {red}Send Failed {res}')
                    print('=======================================================')


        send99()
        input('Click Enter For Exit ...')
    else:
        if xc == 3:
            def plivo():
                os.system('title Plivo Bulk SmS Sender')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''

    ____  __    _____    ______ 
   / __ \/ /   /  _/ |  / / __ \
  / /_/ / /    / / | | / / / / /
 / ____/ /____/ /  | |/ / /_/ / 
/_/   /_____/___/  |___/\____/  
                                

                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                print('=======================================================')
                auth_id = input(f'{gr}Enter Your Auth_ID{res} : ')
                print('=======================================================')
                auth_token = input(f'{cy}Enter Your Auth_Token {res}: ')
                print('=======================================================')
                sender_num = input(f'{red}From Phone {res}:- ')
                print('=======================================================')
                num = open('config/phone.txt','r').read().splitlines()
                
                messege = open('config/message.txt').read()

                headers = {'Content-Type': 'application/json'}
                url = "https://api.plivo.com/v1/Account/"+auth_id+"/Message/"
                for i in num :
                    data = '{"src": "'+sender_num+'","dst": "'+str(i)+'", "text": "'+messege+'"}'
                    send = requests.post(url, data=data, headers=headers, auth=(auth_id, auth_token))
                    if "verify" in str(send.text) or "login" in str(send.text) or "credentials" in str(send.text):
                        print(f'               {red}[!] Your Api Key Invalid [!]')
                        sys.exit()
                        input('Click Enter For Exit ...')
                    else:
                        send_json = send.json()
                        uuid = send_json['message_uuid']
                        msg_u = uuid[0]
                        surl = url+msg_u
                        status = requests.get(surl, headers=headers, auth=(auth_id, auth_token))
                        final = status.json()
                        state = final["message_state"]
                        if state == "sent" or state == "delivered":
                            print(f'Phone : {yl} {str(i)}  {res} ==> {gr}Send Ok ! {res}')
                        elif state == "undelivered" or state == "queued":
                            print(f'Phone : {yl} {str(i)}  {res} ==> {yl}Wait ! {res}')
                        else:
                            print(f'Phone : {yl} {str(i)}  {res} ==> {red}Send Failed {res}')
            plivo()
            input('enter to exit')
        if xc == 7:
            def textbelt():
                os.system('title TexTBelt Sender')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''
  _____________  ____________  ________  ______
 /_  __/ ____/ |/ /_  __/ __ )/ ____/ / /_  __/
  / / / __/  |   / / / / __  / __/ / /   / /   
 / / / /___ /   | / / / /_/ / /___/ /___/ /    
/_/ /_____//_/|_|/_/ /_____/_____/_____/_/     
                                               

                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                print('=======================================================')
                ky = input(f'{gr}Enter Your {yl}TexTBelt Key{res} > ')
                print('=======================================================')
                num = open('config/phone.txt','r').read().splitlines()
                
                msg = open('config/message.txt').read()
                slowprint('Start Send ....!')
                print('Total numbers detected  > ' + Fore.GREEN + str(len(num)))
                for i in num :
                    resp = requests.post('https://textbelt.com/text', {
                        'phone': str(i),
                        'message': msg,
                        'key': ky,
                        
                        })
                        
                    ij = resp.text
                    print('')
                    

                    print(f'{yl}={res}'*40)
                        
                    if ij == 'true':
                        print(f'Number : {gr}{str(i)} {res}=>{gr} SEND !{res}')
                        print(f'{yl}={res}'*40)
                    else:
                        print(f'Number : {red}{str(i)} {res}=>{red} NOT SEND !{res}')
                        print(f'{yl}={res}'*40)
            textbelt()
            input('enter to exit')
        if xc == 8:
            def nexmochecker():
                os.system('title Nexmo checker ')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''

    _   _________  __ __  _______     ________  ________________ __ __________ 
   / | / / ____/ |/ //  |/  / __ \   / ____/ / / / ____/ ____/ //_// ____/ __ \
  /  |/ / __/  |   // /|_/ / / / /  / /   / /_/ / __/ / /   / ,<  / __/ / /_/ /
 / /|  / /___ /   |/ /  / / /_/ /  / /___/ __  / /___/ /___/ /| |/ /___/ _, _/ 
/_/ |_/_____//_/|_/_/  /_/\____/   \____/_/ /_/_____/\____/_/ |_/_____/_/ |_|  
    
                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                import vonage
                link = input(f"\n{gr}Give Me Nexmo_List.txt {res}: ")
                with open(link) as fp:
                    for star in fp:
                        try:
                            check = star.rstrip()
                            ch = check.split('\n')[0].split('|')
                            Key = ch[0]
                            Sec = ch[1]
                            client = vonage.Client(key=Key, secret=Sec)
                            result = client.get_balance()
                            print(f"{yl} {Key}|{Sec} {gr} Working API!{ble} Balance : {result['value']:0.2f} EUR{res}")
                            open("Result_checker_api/Valid_Nexmo.txt", "a").write(f"{Key}|{Sec} Balance: {result['value']:0.2f} EUR\n")
                        except:
                            print(f'{red}{key}|{secret} => BAD {res}')
                            pass
            nexmochecker()
            input('Click Enter For exit.... ')
        if xc == 1:
            def nxx():
                os.system('title Nexmo Sender ')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''
                  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ 
                  ┃           _   _________  __ __  _______        ┃
                  ┃          / | / / ____/ |/ //  |/  / __ \       ┃
                  ┃         /  |/ / __/  |   // /|_/ / / / /       ┃
                  ┃        / /|  / /___ /   |/ /  / / /_/ /        ┃
                  ┃       /_/ |_/_____//_/|_/_/  /_/\____/         ┃
                  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                import vonage
                f1 = input('Enter Your Key : ')
                print('=======================================================')
                f2 = input('Enter Your Secret : ')
                print('=======================================================')
                f3 = input('Enter Your Phone / Name : ')
                msg = open('config/message.txt').read()
                num = open('config/phone.txt','r').read().splitlines()
                client = vonage.Client(key=f1, secret=f2)
                for i in num:
                    responseData = client.send_message(
                        {
                            "from": f3,
                            "to": str(i),
                            "text": msg,
                        }
                        )
                    if responseData["messages"][0]["status"] == "0":
                        print(f'Phone : {yl} {str(i)}  {res} ==> {gr}Send Ok ! {res}')
                        print('=======================================================')
                    else:
                        print(f'Phone : {yl} {str(i)}  {res} ==> {red}Send Failed ! {res}')
                        print('=======================================================')


            nxx()
            input('Click Enter For Exit ..')
        if xc == 2:
            def twilioxxnd():
                os.system('title Twilio Bulk SmS Sender ')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''
                  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ 
                  ┃      _______       ________    ________   ┃
                  ┃     /_  __/ |     / /  _/ /   /  _/ __ \  ┃
                  ┃      / /  | | /| / // // /    / // / / /  ┃
                  ┃     / /   | |/ |/ // // /____/ // /_/ /   ┃
                  ┃    /_/    |__/|__/___/_____/___/\____/    ┃                 
                  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                
                
                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                from twilio.rest import Client
                account_sid = input(f'{cy}Enter Your Account SID {res}: ')
                print('=======================================================')
                auth_token = input(f'{red}Enter Your AUTH TOKEN {res}: ')
                print('=======================================================')
                f2 = input('Enter From Phone : ')
                print('=======================================================')
                msg = open('config/message.txt').read()
                num = open('config/phone.txt','r').read().splitlines()
                client = Client(account_sid, auth_token)
                for i in num:
                    time.sleep(2)
                    message = client.messages \
                        .create(
                            body=msg,
                            from_=f2,
                            to=str(i)
                            )
                    print(f'Phone : {yl} {str(i)}  {res} ==> {gr}Send Ok ! {res}')
                    print('=======================================================')

            twilioxxnd()
            input('Click Enter For Exit ...')
        if xc == 4:
            def msgbird():
                os.system('title MessageBird Bulk SMS Sender ')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ 
┃    __  ___________________ ___   ________________  ________  ____    ┃
┃   /  |/  / ____/ ___/ ___//   | / ____/ ____/ __ )/  _/ __ \/ __ \   ┃
┃  / /|_/ / __/  \__ \\__ \/ /| |/ / __/ __/ / __  |/ // /_/ / / / /   ┃
┃ / /  / / /___ ___/ /__/ / ___ / /_/ / /___/ /_/ // // _, _/ /_/ /    ┃
┃/_/  /_/_____//____/____/_/  |_\____/_____/_____/___/_/ |_/_____/     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                import messagebird
                
                
                f1 = input('Enter Your Api Key : ')
                print('=======================================================')
                f2 = input('Sender ID : ')
                print('=======================================================')
                msg = open('config/message.txt').read()
                num = open('config/phone.txt','r').read().splitlines()
                client = messagebird.Client(f'{f1}')
                for i in num:
                    message = client.message_create(
                        f2,
                        str(i),
                        msg,
                        { 'reference' : 'Foobar' }
                    )
                    print(f'Phone : {yl} {str(i)}  {res} ==> {gr}Send Ok ! {res}')
                    print('=======================================================')
            msgbird()
            input('Click Enter For Exit ...')

        if xc == 9:
            def telnyx():

                os.system('title Telnyx Bulk SMS Sender ')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''
              ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ 
              ┃   ______________    _   ____  ___  __  ┃ 
              ┃  /_  __/ ____/ /   / | / /\ \/ / |/ /  ┃
              ┃   / / / __/ / /   /  |/ /  \  /|   /   ┃
              ┃  / / / /___/ /___/ /|  /   / //   |    ┃
              ┃ /_/ /_____/_____/_/ |_/   /_//_/|_|    ┃
              ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                
                
                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                import telnyx
                f1 = input('Enter Your Api Key : ')
                print('=======================================================')
                telnyx.api_key = f1
                your_telnyx_number = input('Enter Your From Number Telnyx : ')
                print('=======================================================')
                num = open('config/phone.txt','r').read().splitlines()
                msg = open('config/message.txt').read()
                for i in num:
                    telnyx.Message.create(
                        from_=your_telnyx_number,
                        to=str(i),
                        text=msg,
                        )
                   
                    print(f'Phone : {yl} {str(i)}  {res} ==> {gr}Send Ok ! {res}')
                    print('=======================================================')


            telnyx()
            input('Click Enter For Exit ...')
        if xc == 16:
            def twilioch():
                os.system('title Twilio Checker Api')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''

  _______       ________    ________     ________  ________________ __ __________ 
 /_  __/ |     / /  _/ /   /  _/ __ \   / ____/ / / / ____/ ____/ //_// ____/ __ \
  / /  | | /| / // // /    / // / / /  / /   / /_/ / __/ / /   / ,<  / __/ / /_/ /
 / /   | |/ |/ // // /____/ // /_/ /  / /___/ __  / /___/ /___/ /| |/ /___/ _, _/ 
/_/    |__/|__/___/_____/___/\____/   \____/_/ /_/_____/\____/_/ |_/_____/_/ |_|  
                                                                                        
                
                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                from time import strftime
                now = strftime("%Y-%m-%d %H:%M:%S")
                link = input("Give Your Twilio List : ")
                with open(link) as fp:
                    for star in fp:
                        check = star.rstrip()
                        ch = check.split('\n')[0].split('|')
                        account_sid = ch[0]
                        auth_token = ch[1]
                        auth = (account_sid, auth_token)
                        try:
                            curler_balance = requests.get("https://api.twilio.com/2010-04-01/Accounts/"+account_sid+"/Balance.json", auth=auth).text
                            curler_msg = requests.get("https://api.twilio.com/2010-04-01/Accounts/" + account_sid + "/Messages.json", auth=auth).text
                            info_balance = json.loads(curler_balance)
                            info_msg = json.loads(curler_msg)
                            for msg in info_msg["messages"]:
                                if msg["direction"] == "outbound-api":
                                    nope = msg["from"]
                                    break
                                elif msg["direction"] == "inbound-api":
                                    nope = msg["to"]
                                    break
                            print(f"{bgr}{wh}{account_sid}'|'{auth_token} | Work")
                            build = "Account_SID: "+account_sid+'|'+ "Token: "+auth_token+'\n' +"Currency: "+info_balance["currency"]+'\n'+"Balance :"+info_balance["balance"]+'\n'+"Phone number: "+nope+'\n'
                            remover = build.replace('\r', '')
                            save = open('Twilio_Checked.txt', 'a')
                            save.write(remover+'\n')
                            save.close()
                        except:
                             print (f"{bred}{wh}{account_sid}'|'{auth_token}{res} => FAILED: Invalid credentials.")
                             pass



            twilioch()
            input('Click Enter For Exit ...')
        if xc == 6:
            def proovl():
                os.system('title Proovl Bulk Sms Sender')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''
              ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ 
              ┃     ____  ____  ____  ____ _    ____   ┃
              ┃    / __ \/ __ \/ __ \/ __ \ |  / / /   ┃
              ┃   / /_/ / /_/ / / / / / / / | / / /    ┃
              ┃  / ____/ _, _/ /_/ / /_/ /| |/ / /___  ┃
              ┃ /_/   /_/ |_|\____/\____/ |___/_____/  ┃
              ┃                                        ┃
              ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                
                
                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                import urllib
                import urllib.parse
                import urllib.request
                import ssl
                num = open('config/phone.txt','r').read().splitlines()
                msg = open('config/message.txt').read()
                f1 = input('Enter Your User : ')
                print('=======================================================')
                f2 = input('Enter Your Token : ')
                print('=======================================================')
                f3 = input('Enter From Phone : ')
                print('=======================================================')
                for i in num:
                    url = "https://www.proovl.com/api/send.php?"
                    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
                    params = {
                        'user': f1,
                        'token': f2,
                        'from': f3,
                        'to': str(i),
                        'text': msg}
                    try:
                        _create_unverified_https_context = ssl._create_unverified_context
                    except AttributeError:
                        pass
                    else:
                        ssl._create_default_https_context = _create_unverified_https_context
                        query_string = urllib.parse.urlencode(params)
                        http_req = url + query_string
                        req = urllib.request.Request(http_req, headers=hdr)
                        f = urllib.request.urlopen(req)
                        freq = (f.read().decode('utf-8'))
                        x = freq.split(";")
                        g = x[1].replace("\"","")
                        y = x[0].replace("\"","")
                        if x[0] == "Error":
                            print(f'Phone : {yl} {str(i)}  {res} ==> {red}Send Failed ! {res}')
                            print('=======================================================')
                        else:
                            print(f'Phone : {yl} {str(i)}  {res} ==> {gr}Send Ok ! {res}')
                            print('=======================================================')
                        f.close()


            proovl()
            input('Click Enter For Exit..')
        if xc == 11:
            def sns():
                os.system('title Amazon SnS Bulk Sms Sender')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''
    ___    __  ______ _____   ____  _   __   _____ _   _______
   /   |  /  |/  /   /__  /  / __ \/ | / /  / ___// | / / ___/
  / /| | / /|_/ / /| | / /  / / / /  |/ /   \__ \/  |/ /\__ \ 
 / ___ |/ /  / / ___ |/ /__/ /_/ / /|  /   ___/ / /|  /___/ / 
/_/  |_/_/  /_/_/  |_/____/\____/_/ |_/   /____/_/ |_//____/  


                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                import boto3
                num = open('config/phone.txt','r').read().splitlines()
                msg = open('config/message.txt').read()
                print('=======================================================')
                f1 = input('Enter Your ACCESS KEY : ')
                print('=======================================================')
                f2 = input('Enter Your SECRET KEY : ')
                print('=======================================================')
                f3 = input('Enter From Region : ')
                print('=======================================================')
                for i in num:
                    client = boto3.client(
                        "sns",
                        aws_access_key_id=f1,
                        aws_secret_access_key=f2,
                        region_name=f3
                        )
                    client.publish(
                        PhoneNumber=str(i),
                        Message=msg
                        )
                    print(f'Phone : {yl} {str(i)}  {res} ==> {gr}Send Ok ! {res}')
                    print('=======================================================')


            sns()
            input('Click Enter For Exit ....')
        if xc == 10:
            def telesign():

                os.system('title Telesign SnS Bulk Sms Sender')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''

  ______________    ___________ ___________   __
 /_  __/ ____/ /   / ____/ ___//  _/ ____/ | / /
  / / / __/ / /   / __/  \__ \ / // / __/  |/ / 
 / / / /___/ /___/ /___ ___/ // // /_/ / /|  /  
/_/ /_____/_____/_____//____/___/\____/_/ |_/   
                                                
                
                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                
                from telesign.messaging import MessagingClient
                customer_id = input('Enter Customer ID : ')
                print('=======================================================')
                api_key = input('Enter Your API KEY : ')
                print('=======================================================')
                num = open('config/phone.txt','r').read().splitlines()
                msg = open('config/message.txt').read()
                message_type = "ARN"
                messaging = MessagingClient(customer_id, api_key)
                for i in num:
                    response = messaging.message(str(i), msg, message_type)
                    print(f'Phone : {yl} {str(i)}  {res} ==> {gr}Send Ok ! {res}')
                    print('=======================================================')



            telesign()
            input('Click Enter For Exit .....')
        if xc == 12:
            def phgen():
                os.system('title Phone Number Generator')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''


    ____  __  ______  _   ________   _____________   __
   / __ \/ / / / __ \/ | / / ____/  / ____/ ____/ | / /
  / /_/ / /_/ / / / /  |/ / __/    / / __/ __/ /  |/ / 
 / ____/ __  / /_/ / /|  / /___   / /_/ / /___/ /|  /  
/_/   /_/ /_/\____/_/ |_/_____/   \____/_____/_/ |_/   
                                                       

                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                cc = input(str(f'Enter the Country Code{res} : '))
                print('=======================================================')
                sc = input(str(f'Enter the Area Code  : '))
                print('=======================================================')
                n = int(input("Enter Amount of numbers: "))
                print('=======================================================')
                lent = int(input('Length Remaining Digits : '))
                print('=======================================================')
                mow = str('9'*lent)
                def random_phone_num_generator():
                    first = str(random.randint(0,int(mow))).zfill(lent)
                    return (first)
                save = open('Result_Generator/Phone.txt', 'a+')
                for i in range(0,n):
                    rez = cc+sc+random_phone_num_generator()
                    save.write(rez + '\n')
                print(f'{bgr}{wh}Your Phone Numbers Saved On Result_Generator/Phone.txt')


            phgen()
            input('Click Enter For Exit ...')
        if xc == 14:
            def fr():
                os.system('title Phone Number Filter Carrier')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''

  _____  _    _  ____  _   _ ______    _____ _    _ ______ _____ _  ________ _____  
 |  __ \| |  | |/ __ \| \ | |  ____|  / ____| |  | |  ____/ ____| |/ /  ____|  __ \ 
 | |__) | |__| | |  | |  \| | |__    | |    | |__| | |__ | |    | ' /| |__  | |__) |
 |  ___/|  __  | |  | | . ` |  __|   | |    |  __  |  __|| |    |  < |  __| |  _  / 
 | |    | |  | | |__| | |\  | |____  | |____| |  | | |___| |____| . \| |____| | \ \ 
 |_|    |_|  |_|\____/|_| \_|______|  \_____|_|  |_|______\_____|_|\_\______|_|  \_\
                                                                                    
                                                                                    

                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                phone_number = open(input(f'{cy}Enter Phone Number List{res} : '),'r').read().splitlines()
                print('=======================================================')
                access_key = input(f'{gr}Enter Your Access Key {res}: ')
                for i in phone_number :
                    url = 'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + str(i)
                    response = requests.get(url)
                    answer = response.json()
                    if answer["carrier"] :
                        print(f'{gr}{answer["number"]}{res}{yl} => {cy}{answer["carrier"]}{res}')
                        save = open(f'Result_checker_ph/{answer["carrier"]}.txt', 'a+')
                        save.write(str(i) + '\n')
                    else:
                        print(f'{red}{answer["number"]} => Die{res}')

            fr()
            input('Click Enter For Exit ...')
        if xc == 13:
            def fr():
                os.system('title Phone Number Checker [Live/Die]')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''


  _____  _    _  ____  _   _ ______    _____ _    _ ______ _____ _  ________ _____  
 |  __ \| |  | |/ __ \| \ | |  ____|  / ____| |  | |  ____/ ____| |/ /  ____|  __ \ 
 | |__) | |__| | |  | |  \| | |__    | |    | |__| | |__ | |    | ' /| |__  | |__) |
 |  ___/|  __  | |  | | . ` |  __|   | |    |  __  |  __|| |    |  < |  __| |  _  / 
 | |    | |  | | |__| | |\  | |____  | |____| |  | | |___| |____| . \| |____| | \ \ 
 |_|    |_|  |_|\____/|_| \_|______|  \_____|_|  |_|______\_____|_|\_\______|_|  \_\
                                                                                    
                                                                                    

                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                phone_number = open(input(f'{cy}Enter Phone Number List{res} : '),'r').read().splitlines()
                print('=======================================================')
                access_key = input('Enter Your Access Key : ')
                for i in phone_number :
                    url = 'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + str(i)
                    response = requests.get(url)
                    answer = response.json()
                    if answer["carrier"] :
                        print(f'{gr}{answer["number"]} => Live {res}')
                        save = open(f'Result_checker_ph/live_phone.txt', 'a+')
                        save.write(str(i) + '\n')
                    else:
                        print(f'{red}{answer["number"]} => Die')
                        dk = open(f'Result_checker_ph/die_phone.txt', 'a+')
                        dk.write(str(i) + '\n')

            fr()
            input('Click Enter For Exit ...')
        if xc == 15:
            def fw():
                os.system('title Phone Number Checker [Live/Die] + Filter Carrier')
                os.system('cls')
                clear = '\x1b[0m'
                colors = [36, 32, 34, 35, 31, 37]
                x = '''
 

  _____  _    _  ____  _   _ ______    _____ _    _ ______ _____ _  ________ _____  
 |  __ \| |  | |/ __ \| \ | |  ____|  / ____| |  | |  ____/ ____| |/ /  ____|  __ \ 
 | |__) | |__| | |  | |  \| | |__    | |    | |__| | |__ | |    | ' /| |__  | |__) |
 |  ___/|  __  | |  | | . ` |  __|   | |    |  __  |  __|| |    |  < |  __| |  _  / 
 | |    | |  | | |__| | |\  | |____  | |____| |  | | |___| |____| . \| |____| | \ \ 
 |_|    |_|  |_|\____/|_| \_|______|  \_____|_|  |_|______\_____|_|\_\______|_|  \_\
                                                                                    
                                                                                                                                                           
                
                '''
                for N, line in enumerate(x.split('\n')):
                    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
                    time.sleep(0.05)
                phone_number = open(input(f'{cy}Enter Phone Number List{res} : '),'r').read().splitlines()
                print('=======================================================')
                access_key = input(f'{gr}Enter Your Access Key : ')
                for i in phone_number :
                    url = 'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + str(i)
                    response = requests.get(url)
                    answer = response.json()
                    if answer["carrier"] :
                        print(f'{gr}{answer["number"]} => Live {res} | Carrier : {cy}{answer["carrier"]}{res} ')
                        save = open(f'Result_checker_ph/Live - {answer["carrier"]}.txt', 'a+')
                        save.write(str(i) + '\n')
                    else:
                        print(f'{red}{answer["number"]} => Die')
                        dk = open(f'Result_checker_ph/die_phone.txt', 'a+')
                        dk.write(str(i) + '\n')

            fw()
            input('Click Enter For Exit ...')







if __name__ == '__main__':
    main()
