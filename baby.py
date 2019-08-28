from random import choice
questions = ["Why are we poor mummy?: ", "Where's Daddy?: ", 
"Why isn't dinner ready?: "]

questions = choice(questions)
answer = input(questions).strip().lower()

while answer != "just because":
  answer = input("why?: ").strip().lower()

print("Oh... Okay")
