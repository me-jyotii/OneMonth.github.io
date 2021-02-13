# states = ["NY", "PA", "CA"]  # list
#states = ["New York", "Pennsylvania", "California"] # list
States = ["New York", "NY", "Pennsylvania", "PA", "California", "CA"]  # list

states ={'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}  #dictonary

print(states['NY'])

# A value that does not exist in the dict

# print(states['FL'])

print(states.get('FL')) # A better option
print(states.get('FL', 'Does not exist!'))

print(states.get('NY'))
print(states.get('NY', 'Does not exist!'))

print("Type of States :: ",type(States))
print("Type of states :: ",type(states))

# print all the keys

print(states.keys())

# print all the values

print(states.values())

# append dictonary

states['FL'] = 'Florida'

print(states.values())

# used to store id of an object
