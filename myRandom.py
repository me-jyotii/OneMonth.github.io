import random

bars = ["Rice",
		"Pulaw",
		"Puri",
		"Kheer",
		"Biryani",
		"Chicken lolipop",
		"Momos"]

people = ["Fish",
		  "Tadka",
		  "Halwa",
		  "Puwa",
		  "Souce",
		  "Chawal",
		  "Red Chilli Souce"]       

random_dish1 = random.choice(bars)
random_dish2 = random.choice(people)
# random_friends = random.choice(people)

print(f"Would you like to eat {random_dish1} with {random_dish2} ")
