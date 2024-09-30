player_1=input("\n enter the player_1 name:")
player_2=input("\n enter the player_2 name:")
position1=0
position2=0
while (position1<=100)  or (position2<=100):
     for i in range(100,0,-1):
          print(i,end="|")
          if i==11 or i==21 or i==31 or i==41 or i==51 or i==61 or i==71 or i==81 or i==91:
               print("\n")
     print("\n snack-1:56 to 29 \n snack-2:98 to 8 \n snack-3:74 to 43 \n snack-4:21 to 2")
     print("ladder-1:9 to 34 \n ladder-2:38 to 64 \n ladder-3:25 to 76 \n ladder-4:54 to 91")
     if position1>100 or position2>100:
          print("try again")
     else:
          import random as rd
          random=rd.randint(1,6)
          roll=int(input("player_1 type-1 player_2 type-2: "))
          if roll==1:
                print("dice value is ",random)
                position1=position1+random
                print(player_1,"position is ",position1)
          elif roll==2:
                print("dice value is ",random)
                position2=position2+random
                print(player_2,"position is ",position2)
          else:
                print("enter 1 or 2")
          if position1==56:
                position1=29
          elif position1==98:
                position1=8
          elif position1==74:
                position1=43
          elif position1==21:
                position1=2
          elif position1==9:
                position1=34
          elif position1==38:
                position1=64
          elif position1==25:
                position1=76
          elif position1==54:
                position1=91
          if position2==56:
                position2=29
          elif position2==98:
                position2=8
          elif position2==74:
                position2=43
          elif position2==21:
                position2=2
          elif position2==9:
                position2=34
          elif position2==38:
                position2=64
          elif position2==25:
                position2=76
          elif position2==54:
                position2=91
if (player_1 or player_2)==100:
     print("you win the game",player_1 or player_2)

