import random


NOMBRE_QUESTIONS = 4

def niveau_de_difficulte():
    print("""1. Facile
2. Moyen
3. Difficile""")
    niveau_str = ""
    while niveau_str == "":
        niveau_str = input("Choisir votre niveau de difficulté: ")
        try:
            niveau_int = int(niveau_str)
            if niveau_int == 1:
                print("")
                print("Vous avez choisi le niveau facile bon courage:")
            elif niveau_int == 2:
                print("")
                print("Vous avez choisi le niveau moyen bon courage:")
            elif niveau_int == 3:
                print("")
                print("Vous avez choisi le niveau difficile bon courage:")
            else:
                niveau_str = ""
        except:
            print("Faire un choix valide !")
            niveau_str = ""
    return niveau_int


def definir_nb_max(niveau):
    if niveau == 1:
        NOMBRE_MAX = 10
    elif niveau == 2:
        NOMBRE_MAX = 50
    elif niveau == 3:
        NOMBRE_MAX = 100
    return NOMBRE_MAX

def definir_nb_min(niveau):
    if niveau == 1:
        NOMBRE_MIN = 1
    elif niveau == 2:
        NOMBRE_MIN = 10
    elif niveau == 3:
        NOMBRE_MIN = 50
    return NOMBRE_MIN
def poser_question(NOMBRE_MIN, NOMBRE_MAX):
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 3)
    operateur_str = "+"
    if o == 1:
        operateur_str = "*"
    elif o == 2:
        operateur_str = "-"
    elif o == 3:
        operateur_str = "/"
    rep_str = ""
    while rep_str == "":
        rep_str = input(f"Calculer {a} {operateur_str} {b} = ")
        try:
            rep_int = float(rep_str)
        except:
            print("Entrer un nombre, attention !")
            rep_str = ""
    calcul = a+b
    if o == 1:
        calcul = a*b
    elif o == 2:
        calcul = a-b
    elif o == 3:
        calcul = a/b
    if rep_int == calcul:
        print("Réponse correcte.")
        return True
    else:
        print("Réponse incorrecte.")
        return False


niveau = niveau_de_difficulte()
NOMBRE_MAX = definir_nb_max(niveau)
NOMBRE_MIN = definir_nb_min(niveau)
nb_point = 0
for i in range(NOMBRE_QUESTIONS):
    print("")
    print("Question n°", i+1, "sur", NOMBRE_QUESTIONS, ":")
    test = poser_question(NOMBRE_MIN, NOMBRE_MAX)
    if test == True:
        nb_point += 1
    print("")
print(f"Votre note est: {nb_point} / {NOMBRE_QUESTIONS}")
MOYENNE = int(NOMBRE_QUESTIONS/2)
if nb_point == NOMBRE_QUESTIONS:
    print("Excelent !")
elif nb_point == 0:
    print("Révisez vos maths !")
elif nb_point < MOYENNE:
    print("Peut faire mieux !")
elif nb_point >= MOYENNE:
    print("Pas mal !")