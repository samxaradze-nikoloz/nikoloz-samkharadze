#1 dan 18 amde ro datvalos
a=0
while a<18:
   a+=1
   print(a)
else:
   print("the count reached 18")
#arcevnebis programa
age=int(input("input your age : "))
while a>=18 and a<=75:
  print("arcevnebsi monawileobis migeba segidzlia")
  break
if age>75 or age<18:
    print("ar segidzlia arcevnebsi miigo monawileoba")
    
#jeirani(infinite loopi ver gavakete ro tavidan dawkebuliko)(NO CHAT GTP USED!)
import random
options=["rock", "paper", "scissors"]
user_pick=input("typer rock, paper or scissors to continiue :")
computer_pick=random.choice(options)
user_points=0
computer_points=0
while user_pick=="stop":
     break
while user_pick=="rock" and computer_pick=="scissors":
     user_points+=1
     computer_points+=0
     print(f"compuer picked scissors you won. your points {user_points} computer points {computer_points}")
     break
while user_pick=="paper" and computer_pick=="rock":
     user_points+=1
     computer_points+=0
     print(f"compuer picked rock you won. your points {user_points} computer points {computer_points}")
     break
while user_pick=="scissors" and computer_pick=="paper":
     user_points+=1
     computer_points+=0
     print(f"compuer picked paper you won. your points {user_points} computer points {computer_points}")
     break
while user_pick=="rock" and computer_pick=="paper":
     user_points+=0
     computer_points+=1
     print(f"compuer picked paper you lost. your points {user_points} computer points {computer_points}")
     break
while user_pick=="paper" and computer_pick=="scissors":
     user_points+=0
     computer_points+=1
     print(f"compuer picked scissors you lost. your points {user_points} computer points {computer_points}")
     break
while user_pick=="scissors" and computer_pick=="rock":
     user_points+=0
     computer_points+=1
     print(f"compuer picked rock you lost. your points {user_points} computer points {computer_points}")
     break
while user_pick=="rock" and computer_pick=="rock":
     user_points+=0
     computer_points+=0
     print(f"compuer picked rock tie. your points {user_points} computer points {computer_points}")
     break
while user_pick=="rock" and computer_pick=="rock":
     user_points+=0
     computer_points+=0
     print(f"compuer picked rock tie. your points {user_points} computer points {computer_points}")
     break
while user_pick=="paper" and computer_pick=="paper":
     user_points+=0
     computer_points+=0
     print(f"compuer picked paper tie. your points {user_points} computer points {computer_points}")
     break
while user_pick=="scissors" and computer_pick=="scissors":
     user_points+=0
     computer_points+=0
     print(f"compuer picked scissors tie. your points {user_points} computer points {computer_points}")
     break
