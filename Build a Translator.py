"""Giraffe language 
vowels(a, e, i, o, and u,) -> g

-------------------------

dog - dgg 
cat --cgt """

def translate (phrase):
    transalation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                transalation = transalation+"G"
            else:
                transalation = transalation+"g"
         
        else:
            transalation = transalation + letter
    return transalation

print(translate(input("Enter a phrase: ")))
