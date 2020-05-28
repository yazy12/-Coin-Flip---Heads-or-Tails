from random import randint
a_heads = 0
a_tails = 0
flip = int(input("enter amout of times fliped: "))

for x in range(flip):
    result = randint(0, 1)
    
    if result == 0:
        print("heads")
        a_heads += 1
    if result == 1:
        print("tails")
        a_tails += 1
print("you have " + str(a_heads) + " heads")
print("you have " + str(a_tails) + " tails")
