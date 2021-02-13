# way-1

# choice = input("Do You Want To Hear A Joke? ")
# if choice == "yes" :
# 	print("Which playing cards are best dancers??\n The King and Queen of Clubs...hahaha")
# elif choice == "no":
# 	print("Okay, Fine.")
# else:
# 	print("I cannot get your answer!!")


# way-2

# choice = input("Do You Want To Hear A Joke? ")
# if choice == "yes" or choice == "Yes" or choice == "y" or choice == "Y":
# 	print("Which playing cards are best dancers??\n The King and Queen of Clubs...hahaha")
# elif choice == "no" or choice == "No" or choice == "n" or choice == "N":
# 	print("Okay, Fine.")
# else:
# 	print("I cannot get your answer!!")

# way-2

# choice = input("Do You Want To Hear A Joke? ")
# yes_list = ["yes",
# 			"Yes",
# 			"Y",
# 			"y"]
# no_list = ["No",
# 		   "no",
# 		   "n",
# 		   "N"]			
# if choice in yes_list:
# 	print("Which playing cards are best dancers??\n The King and Queen of Clubs...hahaha")
# elif choice in no_list:
# 	print("Okay, Fine.")
# else:
# 	print("I cannot get your answer!!")

# way-3

# choice = input("Do You Want To Hear A Joke? ")
# if "y" in choice.lower() :
# 	print("Which playing cards are best dancers??\n The King and Queen of Clubs...hahaha")
# elif "n" in choice.lower():
# 	print("Okay, Fine.")
# else:
# 	print("I cannot get your answer!!")

# way-5

choice = input("Do You Want To Hear A Joke? ")
yes_list = ["yes",
			"Y"]
no_list = ["no",
		   "n"]			
if choice.lower() in yes_list:
	print("Which playing cards are best dancers??\n The King and Queen of Clubs...hahaha")
elif choice.lower() in no_list:
	print("Okay, Fine.")
else:
	print("I cannot get your answer!!")
