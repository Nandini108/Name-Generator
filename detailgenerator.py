from random import randint
import itertools,random

rn = open('name.txt','r')
namelist=list(rn)




#Social Ids Generator

def phone():
    
    ph=''.join(["{}".format(randint(7, 9)) for num in range(0, 1)])+''.join(["{}".format(randint(0, 9)) for num in range(0, 9)])
    return ph
    

def uniqID():
    
    ad=''.join(["{}".format(randint(0, 9)) for num in range(0, 12)])
    return ad



def dob():

    day=''.join(["{}".format(randint(1,30)) for num in range(0, 1)])
    month=''.join(["{}".format(randint(1,12)) for num in range(0, 1)])
    year=''.join(["{}".format(randint(1999, 2002)) for num in range(0, 1)])
    return day , month , year



def insta_and_fb(nam):

    
    firstname = nam.split()[0]
    lastname = nam.split()[-1]
    userid_fb=[]
    userid_insta=['.','_']


    userid_insta.append(g[2])
    userid_insta.append(firstname)
    userid_insta.append(lastname)
    permutations=itertools.permutations(userid_insta,4)
    final_list_insta=[]
    for permutation in permutations:
        final_list_insta.append(permutation[0]+permutation[1]+permutation[2]+permutation[3])



    userid_fb.append(g[0])
    userid_fb.append(firstname)
    userid_fb.append(g[2])
    userid_fb.append(lastname)
    permutations=itertools.permutations(userid_fb,3)
    final_list_fb=[]
    for permutation in permutations:
        final_list_fb.append(permutation[0]+permutation[1]+permutation[2])

    return random.choice(final_list_insta),  random.choice(final_list_fb)  






####################################################################################################################

for name in namelist:
    details=[]
    g=dob()
    details.append(name.strip())
    details.append(g)
    details.append(phone())
    details.append(uniqID())
    details.append(insta_and_fb(name))
    print(details)
