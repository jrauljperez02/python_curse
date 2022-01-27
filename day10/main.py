from gameData import data
from logos import *
import random
import os


def get_random_account(data):
    '''Get random account from data list'''
    return random.choice(data)


def showData(account):
    '''Lets use this function to be to print all my information '''
    name = account['name']
    description = account['description']
    country = account['country']

    return f'{name}, a {description}, from {country}'

def check_answer(guess,a_followers,b_followers):
    """Function to ckeck followers against user's guess and returns
    True if they got it right or False if we got a mistake"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def game():
    print(logo)

    game_should_continue = True
    account_a = get_random_account(data)
    account_b = get_random_account(data)
    score = 0

    while game_should_continue:
        
        account_a = account_b
        account_b = get_random_account(data)

        while account_a == account_b:
            account_b = get_random_account(data)
        
        print(f"Compare A: {showData(account_a)}")
        print(vs)
        print(f"Compare B: {showData(account_b)}")

        guess = input('Who has more followers? Type "A" or "B": ').lower()


        #lets validate followers
        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']
        result = check_answer(guess,a_followers,b_followers)
        os.system('clear')


        #if result == True, that means you were right
        # lets modify the score value
        if result:
            score += 1
            print(f'You were right! Your current score is {score}')

        elif not result:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score {score}")

game()