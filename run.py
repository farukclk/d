f=open("tel.txt","r")
ff=open("yeni.txt","w")
def say(m):
 for i in m:
    if m.count(i) > 4:
       return False
 return True

def artis(m):
  s=0
  tmp=""
  for i in m:
    if i!= s:
      tmp+=i
      s=i
  l=[int(i) for i in tmp]
  k=2
  t=0
  lsayisi=len(l)
  l.append(31)
  if l[0] < l[1]:
      t=1
  for no, i in enumerate(l):
    if no==lsayisi-2:
      break
    elif l[no] < l[no+1] and t==0:
       t=1
       k+=1
    elif l[no] > l[no+1] and t==1: 
       t=0
       k+=1
#  print(tmp,k)
  if k < 4 :
   return False
  return True

def farkli(m):
    a=set()
    for i in m:
      a.add(i)
    if not 4 <= len(a)<= 6:
       return False
    else:
       return True

def toplam(no):
   l=[int(i) for i in no]
   sum=0
   for i in l:
     sum+=i
   if 16 <= sum <=43:
      return True
   else:
      return False

for no, i in enumerate(f):
    i=i.strip()
    if say(i)==False:
       continue
    
    elif toplam(i)==False:
       continue
  
    elif artis(i)==False:
       continue
    
    else:
       print(i)
       ff.write(i+"\n")
ff.close()
f.close()
