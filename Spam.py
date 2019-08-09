from random import shuffle
liste = "amazing exciting gorgeous blazing stunning biggest tremendous greatest best fantastic \
     phenomenal delightful ambitious outstanding massive incredible spectacular magical".upper().split()
shuffle(liste)


for Strophe in range(5):
    for n in range(2):
        for i in range(4):
            print("SPAM ", end='')
        print()
    el1 = liste.pop()
    el2 = liste.pop()
        
    print("{} SPAM, {} SPAM".format(el1, el2))
    print()