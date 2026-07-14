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

if choice == "1":
    current_player = player1
else:
    current_player = player2

print(current_player, "commence la partie.")
print("Il y a", matches, "allumettes.")

while matches > 0:
    print("Il reste", matches, "allumettes.")
    print(current_player, "doit jouer.")

    take = int(input("Combien d'allumettes voulez-vous prendre (1 à 4) ? "))

    while take < 1 or take > 4 or take > matches:
        print("Choix invalide.")
        take = int(input("Choisissez un nombre entre 1 et 4, sans dépasser les allumettes restantes : "))

    matches = matches - take

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1