import random

king = 10
queen = 10
jack = 10
ace_soft = 11
ace_hard = 1
cards = [ace_hard, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ace_soft, jack, queen, king]

def draw():
    card = random.choice(cards)
    return card


def play():
    dealer = 0
    player = 0
    player_money = 50000
    name = input("Please enter your name: ")
    print("Hello " + str(name) + " let's play blackjack")
    print("The rules are fairly simple, you will playing against me, the dealer.")
    print("You will be dealt random card values and by the end of each round the person with a value of exactly 21 or a value closest to 21 will be the winner.")
    print("However if you go over 21 you lose.")
    print("You have a bet cap of " + str(player_money) + ", use it wisley ")
    print("\n")
    while player_money > 10 and dealer <= 21 and player <= 21:
        place_bet = input(name + " Please place or increase your bet,the maximum amount is 500, just type the amount: ")
        if int(place_bet) > 500:
            print( "Maximum Bet: 500")
            invalid_amount = input("invalid input, please place a bet below 500")
        else:
            player_money = player_money - int(place_bet)
            print("You have "  + str(player_money) + " left to bet")
        print("\n")
        player = player + draw()
        print("Your card: " + str(player))
        dealer = dealer + draw()
        print("My card: " + str(dealer))
        player = player + draw()
        print("You again and you're up to: " + str(player))
print(play())


        
                    
                

                    





    
         
       

