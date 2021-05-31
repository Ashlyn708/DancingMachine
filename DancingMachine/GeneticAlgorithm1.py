#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random


# In[9]:


## step sequence accuracy
def stepRules(step1,step2,step3,step4):
    marks=1
    if step1 == step2 and step1 == step3 and step1 == step4:
        marks= .01
    if step1==2 and step2==3:
        marks+=-.1
    if step2==2 and step3==3:
        marks+=-.1
    if step3==2 and step4==3:
        marks+=-.1
    if step1>1 and step1==step2:
        marks+=-.1
    if step2>1 and step2==step3:
        marks+=-.1
    if step3>1 and step4==step3:
        marks+=-.1
    if step1==0 and step1==step2 and step1==step3:
        marks+=-.1
    if step2==0 and step2==step3 and step2==step4:
        marks+=-.1
    return marks;  


# In[10]:


def fitness(step1,step2,step3,step4):
    ans=stepRules(step1,step2,step3,step4)
    
    if ans == 1:
        return 1 
    else:
        return ans
           


    
# In[11]:


def GA():
    solutions=[]
    for s in range(500):
        solutions.append((random.randrange(5),random.randrange(5),random.randrange(5),random.randrange(5)))
    
    for i in range(50):
#getting the fittnes value and appending tuple as well    
        rankedsolutions = []
        for s in solutions:
            rankedsolutions.append((fitness(s[0],s[1],s[2],s[3]),s))
        rankedsolutions.sort()
        rankedsolutions.reverse()
    
        ##print(f"======== Gen {i} best solutions======")
        ##print(rankedsolutions[0]) 
    
        bestsolutions = rankedsolutions[:10]

        finalsolution=random.choice(bestsolutions)
        if finalsolution[0]>=1:
            return finalsolution[1]
            break;
    
        elements=[]
        for s in bestsolutions:
            elements.append(s[1][0])
            elements.append(s[1][1])
            elements.append(s[1][2])
            elements.append(s[1][3])
  #crossover and mutating      
        newGen= []
        for i in range(100):
            e1 = round(random.choice(elements)*random.randrange(100)%5)
            e2 = round(random.choice(elements)*random.randrange(100)%5)
            e3 = round(random.choice(elements)*random.randrange(100)%5)
            e4 = round(random.choice(elements)*random.randrange(100)%5)
        
            newGen.append((e1,e2,e3,e4))
        
        solutions = newGen


# In[ ]:





# In[ ]:





# In[ ]:




