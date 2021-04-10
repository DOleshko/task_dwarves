import random

dwarves = []
dwarves_guesses = []

def put_on_hats(dw_list,num):
    i = 0
    while i < d_num :
        random.seed()
        d = random.randint(0,1)
        dw_list.append(d)
        i += 1

def calc_CRC(elements, begin, end):
    CRC = elements[end] ^ elements[end-1]
    i = end - 2
    
    while i >= begin:
        CRC = CRC ^ elements[i]
        i -= 1
    
    return CRC
    
def tell_ogre(dwarve_hat, guess_color):
    print("guess = ", guess_color)
    if dwarve_hat == guess_color :
        print("< Go!!! > ")
    else:
        print("< om-nom-nom!!! >")

#------------------------------------------

d_num = random.randint(5,31)
put_on_hats(dwarves, d_num)
print(dwarves)

CRC = calc_CRC(dwarves, 1, len(dwarves)-1)
tell_ogre(dwarves[0], CRC)

d_curr = 1
while d_curr < d_num :
    elements = []
    
    guess_color = 1
    dwarves_guesses.append(guess_color)
    elements = dwarves_guesses[0:] + dwarves[(d_curr + 1):] 
    guess_CRC = calc_CRC(elements, 0, len(elements)-1)
    
    if guess_CRC != CRC:
        guess_color = 0
        dwarves_guesses.pop(len(dwarves_guesses)-1)
        dwarves_guesses.append(guess_color)

    tell_ogre(dwarves[d_curr], guess_color)
    d_curr += 1
