#strings concatenation (aka how to put strings together)
#suppose we want to creat a string that says "subcribe to_________"
# youtuber = "Snehal" # some string variable 


# # a few ways to do this 
# print ("subscribe to"  + youtuber)
# print("subscribe  to {}".format (youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjectives: ")
Verb1 = input("Verb: ")
Verb2 =  input("verb: ")
famous_person = input("famous person: ")
madlib = f"Computer programming is so {adj}! It makes me so exicited all the\
    time beacuse I love to {Verb1}. Stay hydrated and {Verb2} like you are {famous_person}! "

print(madlib)