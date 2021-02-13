import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samuel L. Jackson",
          "Kalyani Singh"]       

random_bar = random.choice(bars)
random_person = random.choice(people)
random_friends = random.choice(people)

print(f"How about you go to {random_bar} with {random_person} and {random_friends}")
