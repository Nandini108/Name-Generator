import itertools,pyautogui,time
bn = open("boyname.txt", "r")
gn = open("girlname.txt", "r")
sn = open('sirname.txt', "r")
rn = open('random.txt','w')

srn=list(sn)
brn=list(bn)

for n in srn :
    for b in brn :
        print(b.strip(),'',n.strip())
  
