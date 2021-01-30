f=open("tel.txt","r")
ff=open("yeni.txt","w")
def say(m):
 for i in m:
    if m.count(i) >= 5: # 5
       return False
 return True


def fark2(m):
   l=[int(i) for i in m]
   l.sort()
   x=l[-1]+ l[-2] - l[0] -l[1]
   if not 7 <= x <= 17: # 7 .17
     return True
   return False

def fark3(m):
   l=[int(i) for i in m]
   l.sort()
   x=l[-1]+ l[-2] + l[-3]- l[0] -l[1] - l[2]
   if not 10 <= x <= 18: # 10. 18
     return True
   return False
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
  if not 4 <= k <= 7 : # 4 7
   return False
  return True

def farkli(m):
    a=set()
    for i in m:
      a.add(i)
    if not 4 <= len(a) <= 7 : # 4 7
       return True
    else:
       return False

def toplam(no):
   l=[int(i) for i in no]
   sum=0
   for i in l:
     sum+=i
   if not 11 <= sum <=43: # 11.   43
      return True
   else:
      return False

for no, i in enumerate(f):
    i=i.strip()
    if say(i)==False:
       continue
    elif fark2(i):
       continue

    elif fark3(i):
      continue

    elif toplam(i):
       continue
  
    elif artis(i)==False:
       continue
    elif farkli(i):
       continue
    
    else:
       print(i)
       ff.write(i+"\n")
ff.close()
f.close()
