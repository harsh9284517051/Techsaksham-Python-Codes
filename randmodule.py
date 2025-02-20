import random as rand

toss=rand.randint(1,2)
 
if toss==1:
    print("head")
else:
    print("tails")
    
names=["perl1","perl2","perl3"] 
rand.choice(names)