import os
import sys
from tabnanny import check
import time

def animation(string):
    os.system('cls')

    i = 0
    while i < 3:
        print(string + '.')
        i += 1
        time.sleep(1)
        os.system('cls')

        print(string + '..')
        i += 1
        time.sleep(1)
        os.system('cls')

        print(string + '...')
        i += 1
        time.sleep(1)

def check_input(command):
    if command.lower() == "e" or command.lower() == "exit":
        animation("LOADING MAIN MENU")
        main()
    if command.lower() == "q" or command.lower() == "quit":
        print("EXITING TERMINAL SCREEN")
        time.sleep(0.5)
        sys.exit()


def user_menu(username):
    def refresh_user_menu():
        os.system('cls')
        print("-------------------------------------------------------")
        print("------------ WELCOME VALUED CUSTOMER ^.^ --------------")
        print("-------------------------------------------------------")
        print(" _____________________________________________________ ")
        print("|                                                     |")
        print("| <E> ABORT LOGIN                                     |")
        print("| <Q> EXIT                                            |")
        print("|_____________________________________________________|")
        print("\n")
    
    refresh_user_menu


def login_menu(usernames):
    def refresh_login():
        os.system('cls')
        print("-------------------------------------------------------")
        print("-------------------- LOGIN SCREEN ---------------------")
        print("-------------------------------------------------------")
        print(" _____________________________________________________ ")
        print("|                                                     |")
        print("| <E> ABORT LOGIN                                     |")
        print("| <Q> EXIT                                            |")
        print("|_____________________________________________________|")
        print("\n")
        
    refresh_login()
    username = input("ENTER IN USERNAME: ")
    os.system('cls')
    check_input(username)

    refresh_login()
    password = input("ENTER IN PASSWORD: ")
    os.system('cls')
    check_input(password)

    user_menu(username)


def signup_menu(usernames):
    file = open("usernames.txt", "r")

    def refresh_signup():
        os.system('cls')
        print("-------------------------------------------------------")
        print("------------------- SIGN UP SCREEN --------------------")
        print("-------------------------------------------------------")
        print(" _____________________________________________________ ")
        print("|                                                     |")
        print("| <E> ABORT LOGIN                                     |")
        print("| <Q> EXIT                                            |")
        print("|_____________________________________________________|")
        print("\n")
        
    refresh_signup()
    username = input("ENTER IN USERNAME: ")
    check_input(username)
    if username.lower() in usernames:
        animation("USERNAME ALREADY EXISTS, RETURNING TO SIGN IN SCREEN")
        signup_menu(usernames)
    
    def pw_step() -> str:
        refresh_signup()
        password = input("ENTER IN PASSWORD: ")
        check_input(password)
        if len(password) < 5:
            animation("PASSWORD IS TOO SHORT, MUST BE LONGER THAN 5 CHARACTERS\nRETURNING TO SIGN UP SCREEN")
            pw_step()

        return password

    password = pw_step()

    refresh_signup()
    person = input("ENTER IN FULL NAME: ")
    check_input(person)

    refresh_signup()
    person = input("ENTER IN PHONE NUMBER: ")
    check_input(person)

    refresh_signup()
    person = input("ENTER IN PERSONAL ADDRESS: ")
    check_input(person)   

def card_faq_menu():        
    os.system('cls')
    print("-------------------------------------------------------")
    print("------------------- CARD FAQ MENU ---------------------")
    print("-------------------------------------------------------")
    print(" _____________________________________________________ ")
    print("|                                                     |")
    print("|         SUPPORTED CARDS AND TRANSACTION FEES        |")
    print("|                                                     |")
    print("|  AMEX --------------------------------------- 0.8%  |")
    print("|  VISA --------------------------------------- 1.0%  |")
    print("|  DISCOVER ----------------------------------- 0.5%  |")
    print("|  CONVENIENCE FEE ---------------------------- 0.2%  |")
    print("|                                                     |")
    print("| <E> BACK TO MAIN MENU                               |")
    print("| <Q> EXIT                                            |")
    print("|_____________________________________________________|")
    print("\n")
    command = input("WHAT WOULD YOU LIKE TO DO? ")
    os.system('cls')
    check_input(command)
    


def main():
    running = True
    while running:
        os.system('cls')
        print("-------------------------------------------------------")
        print("----------- WELCOME TO OUR PAYMENT PLATFORM -----------")
        print("-------------------------------------------------------")
        print(" _____________________________________________________ ")
        print("|                                                     |")
        print("| <1> LOGIN                                           |")
        print("| <2> SIGN UP                                         |")
        print("| <3> VIEW SUPPORTED CARDS                            |")
        print("| <Q> EXIT                                            |")
        print("|_____________________________________________________|")
        print("\n")
        command = input("WHAT WOULD YOU LIKE TO DO? ")
        os.system('cls')

        if command == "1":
            file = open("usernames.txt", "r")
            usernames = file.readlines()
            file.close()
            if len(usernames) < 1:
                animation("NO EXISTING USERS, RETURNING TO MAIN MENU")
            else:
                animation("LOADING LOGIN SCREEN")
                login_menu(usernames)
        
        elif command == "2":
            file = open("usernames.txt", "r")
            usernames = file.readlines()
            file.close()
            animation("LOADING SIGN UP SCREEN")
            signup_menu(usernames)
        
        elif command == "3":
            animation("LISTING SUPPORTED CARDS")
            card_faq_menu()

        elif command.lower() == "q" or command.lower() == "quit":
            print("EXITING TERMINAL SCREEN")
            time.sleep(0.5)
            sys.exit()
        else:
            animation("INVALID COMMAND")

if __name__ == "__main__":
    main()