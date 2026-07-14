# Players information
player1 = input("Nom du joueur 1 : ")
player2 = input("Nom du joueur 2 : ")

# Game information
matches = 21

# Choose starting player
print("Qui commence ?")
print("1 -", player1)
print("2 -", player2)

choice = input("Votre choix : ")

while choice != "1" and choice != "2":
    print("Choix invalide.")
    choice = input("Votre choix : ")

if choice == "1":
    current_player = player1
else:
    current_player = player2

print(current_player, "commence la partie.")
print("Il y a", matches, "allumettes.")

while matches > 0:
    if matches == 1:
        print("Il reste 1 allumette.")
    else:
        print("Il reste", matches, "allumettes.")

    print(current_player, "doit jouer.")

#empêcher une erreur si le joueur tape du texte
    while True:
        try:
            take = int(input("Combien d'allumettes voulez-vous prendre (1 à 4) ? "))

            if 1 <= take <= 4 and take <= matches:
                break

            print("Choix invalide.")

        except ValueError:
            print("Veuillez entrer un nombre.")

    matches = matches - take

    if matches == 0:
        print(current_player, "a pris la dernière allumette.")
        print(current_player, "a perdu !")

#Comme il y a un break juste avant, ce changement ne sera pas exécuté quand la partie est terminée, donc y aura plus de changemlent de joueur
        if current_player == player1:
            print(player2, "gagne !")
        else:
            print(player1, "gagne !")

            print("La partie est terminée.")
            print("Merci d'avoir joué !")

        break

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1