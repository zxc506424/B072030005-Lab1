#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


i=0;    #初始值為0，未猜拳
r=0;    #用0代表rock
p=1;    #用1代表paper
s=2;    #用2代表scissors
tie=0;  #平手數目初始值
loss=0; #輸的次數初始值
game_way=['ROCK','PAPER','SCISSORS'] 

print('Welcome to ROCK, PAPER, SCISSORS game!')
while i==0:
    #玩家出拳
    player = input("Enter your move: (r)ock (p)aper (s)cissors:")
    #電腦出拳
    random_number = random.randint(0,2)
    
    #如果電腦出石頭
    if player =='r':
        print('ROCK versus...')
        print(game_way[random_number])
        
        #電腦出paper，表示玩家勝利
        if random_number==1:
            print('You are loss')
            loss=loss+1
        
        #電腦出rock，表示兩方平手  
        elif random_number==0:
            print('It is tie!')
            tie=tie+1
        #電腦出scissors，表示玩家失敗      
        else:
            print('You are win!')
            i=i+1 #i不為零結束迴圈
              
            
    elif player =='p':
        print('PAPER versus...')
        print(game_way[random_number])
        if random_number==1:
            print('It is tie!')
            tie=tie+1
        elif random_number==0:
            print('You are win')
            i=i+1      
        else:
            print('You are loss!')
            loss=loss+1
           
    else:
        print('SCICCORS versus...')
        print(game_way[random_number])
        if random_number==1:
            print('You are win')
            i=i+1
            
        elif random_number==0:
            print('You are loss!')
            loss=loss+1
            
        else:
            print('It is tie!')
            tie=tie+1 
         
        
print('You have', tie, 'ties and', loss, 'losses before your first win')

