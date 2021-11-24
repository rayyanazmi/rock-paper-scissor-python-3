"""
Author: Rayyan Azmi
Description: Python file for rock paper scissor code.
Package: rock-paper-scissor
Python Version: 3
Version: 1
"""
import random

def main(score_limit):
    """
    This function runs the rock paper scissor game logic.

    Parameters
    ----------
    score_limit : int
        Limit of max score.
    """
    user_score = 0
    pc_score = 0

    my_list = ["rock", "paper", "scissor"]

    while user_score < score_limit and pc_score < score_limit:
        user_guess = input("pls enter your guess, rock/paper/scissor:").lower()

        pc_guess = random.choice(my_list)
        print("the computer chose", pc_guess)

        if pc_guess == "rock" and user_guess == "rock":
            print ("Tie!")

        elif pc_guess == "paper" and user_guess == "paper":
            print ("Tie!")

        elif pc_guess == "scissor" and user_guess == "scissor":
            print ("Tie!")

        elif pc_guess == "rock" and user_guess == "scissor":
            print ("the computer scored")
            pc_score = pc_score +1

        elif pc_guess == "paper" and user_guess == "rock":
            print ("the computer scored")
            pc_guess = pc_score +1

        elif pc_guess == "scissor" and user_guess == "paper":
            print ("the computer scored")
            pc_score = pc_score +1

        elif pc_guess == "rock" and user_guess == "paper":
            print ("you scored")
            user_score = user_score +1

        elif pc_guess == "paper" and user_guess == "scissor":
            print ("you scored")
            user_score = user_score +1

        elif pc_guess == "scissor" and user_guess == "rock":
            print ("you scored")
            user_score = user_score +1

        print ("the user score is: ", user_score)
        print ("the pc score is: ", pc_score)

    if user_score == score_limit:
        print ("congrats you won!")
    elif pc_score == score_limit:
        print ("the computer won, better luck next time")

main(score_limit=5)