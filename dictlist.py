animal_sounds = {

   "cat": ["meow", "purr"],

   "dog": ["woof", "bark"],

   "fox": []

}

mattan = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}

chris = {'name': 'Chris', 'height': 68, 'shoe size': 10, 'hair': 'Brown', 'eyes': 'Brown'}

sarah = {'name': 'Sarah', 'height': 72, 'shoe size': 8, 'hair': 'Brown', 'eyes': 'Brown'}

people = [mattan, chris, sarah]

print(people)

for person in people:
	print(person['height'])

for person in people:
	print(person.get('height'))

