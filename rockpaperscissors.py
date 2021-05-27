# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:03:57 2021

@author: Aahan Birla
"""
import random
score = 0
def start_game():
    user_name = input("Enter your name:-\n")
    global score
    print("Welcome to the game {}\n".format(user_name))
    print("Your score is",score)
    choice = input("Do you want to start the game?(yes/no)\n")
    while str.lower(choice) != "no":
        choices = ['R','P','S']
        comp_choice = random.choice(choices)
        print("Rock = R\nPaper = P\nScissors = S\n")
        user_choice = input("Enter your move:- ")
        final_user_choice = str.upper(user_choice)
        print("The computer chooses:- {}".format(comp_choice))
        if final_user_choice == comp_choice:
            print("Its a tie!, try again\n")
        elif final_user_choice == "R" and comp_choice == str("P"):
            print("The computer has won!, Score shall be reduced\n")
            score -= 1
        elif final_user_choice == "P" and comp_choice == str("S"):
            print("The computer has won!, Score shall be reduced\n")
            score -= 1
        elif final_user_choice == "S" and comp_choice == str("R"):
            print("The computer has won!, Score shall be reduced\n")
            score -= 1
        else:
            print("You WIN! CONGRATULATIONS")
            score += 1
        choice = input("Do you wish to play more?(yes/no)\n")

start_game()
print("Your score is {}".format(score))
print("\nHope to see you again, Come back soon")