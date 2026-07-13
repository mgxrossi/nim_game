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