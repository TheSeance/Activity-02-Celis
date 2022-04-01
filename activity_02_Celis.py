import random

level = int(input("Enter level: "))
power = int(input("Enter power: "))
attack = int(input("Enter attack: "))
defense = int(input("Enter defense: "))

t=input("Enter no. of target: ")
if(t==1):
    target=1
else:
    target=0.5

w=input("1 Against \n2 Beneficial \n3 Normal \nWeather: ")
if(w==1):
    weather=0.5
elif(w==2):
    weather=1.5
else:
    weather=1

b=str(input("Badge holder? y/n: "))
checker="y"
if(b==checker):
    badge=1.25
else:
    badge=1


crit = 1
rfctr = round(random.uniform(0.85,1.0),2)
stab = 1.5
type = 0.5
burn = 1

modifier = target*weather*badge*crit*rfctr*stab*type*burn*1

damage = ((2*level)/5)+2
damage = (damage*power)*(attack/defense)
damage = ((damage/50)+2)*modifier
damage =  round(damage)

print("Damage is: ",damage)
