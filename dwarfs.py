import random

dwarfs = []
dwarfs_guesses = []

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
    
def tell_ogre(dwarf_hat, guess_color):
    print("guess = ", guess_color)
    if dwarf_hat == guess_color :
        print("< Go!!! > ")
    else:
        print("< om-nom-nom!!! >")

#------------------------------------------

d_num = random.randint(5,31)
put_on_hats(dwarfs, d_num)
print(dwarfs)

CRC = calc_CRC(dwarfs, 1, len(dwarfs)-1)
tell_ogre(dwarfs[0], CRC)

d_curr = 1
while d_curr < d_num :
    elements = []
    
    guess_color = 1
    dwarfs_guesses.append(guess_color)
    elements = dwarfs_guesses[0:] + dwarfs[(d_curr + 1):] 
    guess_CRC = calc_CRC(elements, 0, len(elements)-1)
    
    if guess_CRC != CRC:
        guess_color = 0
        dwarfs_guesses.pop(len(dwarfs_guesses)-1)
        dwarfs_guesses.append(guess_color)

    tell_ogre(dwarfs[d_curr], guess_color)
    d_curr += 1
