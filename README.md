# Rock Paper Scissors Game

The Rock Paper Scissors Game is a simple Python script that allows users to play the classic game against the computer. It implements the basic rules of Rock Paper Scissors and keeps track of the user and computer scores until one player reaches the specified score limit.

## How to Play

1. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/rock-paper-scissors-game.git
   ```

2. **Navigate to the Project Directory:**
   ```
   cd rock-paper-scissors-game
   ```

3. **Run the Script:**
   ```
   python rock_paper_scissors.py
   ```

4. **Enter Your Guess:**
   - When prompted, enter your guess: rock, paper, or scissors.
   - The computer will randomly select its guess.

5. **Game Logic:**
   - The game will determine the winner based on the classic Rock Paper Scissors rules.
   - Scores for both the user and computer will be displayed after each round.

6. **Winning the Game:**
   - The first player to reach the specified score limit wins the game.

## Code Explanation

The script is built on a simple game loop and conditional statements to evaluate each round. Here's a snippet of the code:

```
import random

def main(score_limit):
    # Game logic here...

main(score_limit=5)
```

The `main` function initializes the game with the specified score limit. Players take turns entering their guesses, and the winner is determined based on the classic Rock Paper Scissors rules.

## Features and Benefits

- **User vs. Computer:** Play against the computer in a classic Rock Paper Scissors matchup.
- **Score Tracking:** Keep track of the user and computer scores throughout the game.
- **Customizable Score Limit:** Set your own score limit to determine the duration of the game.

Feel free to modify the script or integrate it into your projects. Have fun playing Rock Paper Scissors!
