films={"End Game":[15,5], "Toy Story 4":[3,2], "Lion King":[3,12], "Yesterday":[12,20]}

while True:
  watch = input("What film do you want to watch?: ").strip().title()

  if watch in films:
    age = int(input("How old are you?: ").strip())

    if age >= films[watch][0]:

      num_seats = films[watch][1]
      if num_seats > 0:
        print("Enjoy the film!")
        films[watch][1] = films[watch][1] - 1
      else:
        print("Sorry we're sold out!")
    else:
      print("You're too young to see this film")
  else:
    print("We don't have that film...")
