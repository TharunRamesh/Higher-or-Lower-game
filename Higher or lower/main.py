import random
from replit import clear
from art import logo
from art import vs
from game_data import data
acc_a=random.choice(data)
#print(a)
acc_b=random.choice(data)
#print(b)

def compare(a,b):
  """compare who has more followers"""
  if score>=1:
    print(f"you got it right current score: {score}")
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
  print(vs)
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
  c= input("who has more follower? Type 'A' or 'B': ").lower()
  if c=='a':
    if a['follower_count']>b['follower_count']:
      return 1
      
    else:
      return 0
  elif c=='b':
    if b['follower_count']>a['follower_count']:
      a=b
      return 2
    else:
      return 0
check = True
score=0
while check:
  clear()
  print(logo)
  comp= compare(acc_a,acc_b)
  if comp==1:
    score = score+1
  elif comp==2:
    score=score+1
    acc_a=acc_b 
  elif comp==0:
    clear()
    print(f"Sorry, thats wrong final score: {score}")
    check = False
  acc_b=random.choice(data)