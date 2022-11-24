liste = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

mot = input("Entrez MDP : ")
chaine = str()

def test(chaine,mot):
    if chaine == mot:
        print("MDP cracké : ",chaine)

def brute_force():
    for l in liste:
        chaine = l
        test(chaine,mot)

        for l2 in liste:
            chaine = l + l2
            test(chaine,mot)

            for l3 in liste:
                chaine = l + l2 + l3
                test(chaine,mot)

                for l4 in liste:
                    chaine = l + l2 + l3 + l4
                    test(chaine,mot)

                    for l5 in liste:
                        chaine = l + l2 + l3 + l4 + l5
                        test(chaine, mot)

brute_force()

