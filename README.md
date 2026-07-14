This project is a Python implementation of the Nim game.

The program acts as an **arbiter** between two human players. It manages the game rules, checks the validity of each move, keeps track of the remaining matches, and determines the winner.

The game starts with a pile of **21 matches**.

During their turn, each player can remove between **1 and 4 matches** from the pile.

The particularity of this version of the game is that the player who removes the **last match loses**.

---

## Game Rules

- The game starts with 21 matches.
- Two players compete against each other.
- Players play one after another.
- On each turn, a player must remove:
  - at least 1 match;
  - at most 4 matches.
- A player cannot remove more matches than the number remaining in the pile.
- The player who removes the last match loses the game.
- The other player is declared the winner.

---

## Features

The program includes the following features:

- Ask the names of the two players.
- Allow players to choose who starts the game.
- Display the number of remaining matches.
- Manage alternating turns between players.
- Check that each move respects the rules.
- Prevent invalid inputs:
  - numbers outside the range 1-4;
  - numbers greater than the remaining matches;
  - non-numeric inputs.
- Detect the end of the game.
- Display the loser and the winner.