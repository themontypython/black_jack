# Welcome to Black Jack! H = hearts, C = Clubs, S = Spades, D = diamonds. Just press play. Have fun and good luck!!!

# This Class handles the bank roll, betting, wins, and losses
class Player(object):
    def __init__(self, name, bank_roll=0.0):
        self.name = name
        self.bank_roll = bank_roll

    def win(self, amount):
        self.bank_roll += amount
        return self.bank_roll

    def lose(self, amount):
        self.bank_roll -= amount
        return self.bank_roll

# ----------------------------------------------------------------------
# this is the card deck. outputs cards at random
def deck():
    import random
    cards = {'H2': 2, 'H3': 3, 'H4': 4, 'H5': 5, 'H6': 6, 'H7': 7, 'H8': 8, 'H9': 9, 'H10': 10, 'HJ': 10, 'HQ': 10, 'HK': 10, 'HA': 1,
             'C2': 2, 'C3': 3, 'C4': 4, 'C5': 5, 'C6': 6, 'C7': 7, 'C8': 8, 'C9': 9, 'C10': 10, 'CJ': 10, 'CQ': 10, 'CK': 10, 'CA': 1,
             'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10, 'SJ': 10, 'SQ': 10, 'SK': 10, 'SA': 1,
             'D2': 2, 'D3': 3, 'D4': 4, 'D5': 5, 'D6': 6, 'D7': 7, 'D8': 8, 'D9': 9, 'D10': 10, 'DJ': 10, 'DQ': 10, 'DK': 10, 'DA': 1}

    return random.choice(cards.keys())


# ----------------------------------------------------------------------
# ind is locating the index of key within the 'cards' dict. ind returns an integer value
# player_val appends the values of the respective key with in the dict
# to the player_val list. Note: that the 'ind' has to be called to access
#  the key values in the dict, not the key i.e. 'H3'...
def player_sum():
    player_val = []
    for i in player:
        ind = cards.keys().index(i)
        player_val.append(cards.values()[ind])
        player_tot = sum(player_val)
    return player_tot  # note: return needs to be outside of the for loop to avoid ending the loop after one pass
# ----------------------------------------------------------------------
# player_val appends the values of the respective key with in the dict
# ind is locating the index of key within the 'cards' dict. ind returns an integer value
# to the player_val list. Note: that the 'ind' has to be called to access
#  the key values in the dict, not the key i.e. 'H3'...
def dealer_sum():
    dealer_val = []
    for i in dealer:
        ind = cards.keys().index(i)
        dealer_val.append(cards.values()[ind])
        dealer_tot = sum(dealer_val)
    return dealer_tot
# ----------------------------------------------------------------------
# This deals a unique card to the dealer and appends it to the dealer list
def dealer_append():
    x = deck()
    while True:
        if x in test:
            x = deck()
        else:
            test.append(x)
            dealer.append(x)
            break
# ----------------------------------------------------------------------
# initializing the Player from Class
name = raw_input('Please enter your name: ')
money = float(raw_input('Please enter your bank roll amount: '))
ready_player = Player(name, money)
print 'hi -', ready_player.name
# ----------------------------------------------------------------------
var = 'y'
while var == 'y':
    print '----------------------------------------------------------------------'
    print 'Black Jack =)'
    print '----------------------------------------------------------------------'
    print 'bank roll is: ', ready_player.bank_roll
    amount = float(raw_input('Place bet: '))
    if amount > ready_player.bank_roll:
        #raise RuntimeError('You tried to cheat! You now have to bet your entire bank roll or else the pit boss will break you fingers! ')
        print 'No one likes cheaters! Pit Boss makes you pay the price!!!'
        amount = ready_player.bank_roll
        print 'Look at your bet amount and bank roll... Better win!'
    elif amount < 0.0:
        print 'Nice try asshole!'
        amount = amount*(-1.0)
    else:
        pass
    print 'You have bet: ', amount
    # ----------------------------------------------------------------------
    # Lists for player, dealer, and test. Card dict for storing keys (cards shown)
    # and values (summed for winner loser)
    # Test list will keep track of all cards dealt
    cards = {'H2': 2, 'H3': 3, 'H4': 4, 'H5': 5, 'H6': 6, 'H7': 7, 'H8': 8, 'H9': 9, 'H10': 10, 'HJ': 10, 'HQ': 10, 'HK': 10, 'HA': 1,
             'C2': 2, 'C3': 3, 'C4': 4, 'C5': 5, 'C6': 6, 'C7': 7, 'C8': 8, 'C9': 9, 'C10': 10, 'CJ': 10, 'CQ': 10, 'CK': 10, 'CA': 1,
             'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10, 'SJ': 10, 'SQ': 10, 'SK': 10, 'SA': 1,
             'D2': 2, 'D3': 3, 'D4': 4, 'D5': 5, 'D6': 6, 'D7': 7, 'D8': 8, 'D9': 9, 'D10': 10, 'DJ': 10, 'DQ': 10, 'DK': 10, 'DA': 1}
    test = []  # test list is used to store cards dealt and is a check list for uniqness
    dealer = []  # stores dealers cards
    player = []  # storse players cards
    # ----------------------------------------------------------------------
    # This is the initial deal: two cards to dealer, two cards to player
    # The the test list is populated with unique cards at random from deck()
    i = 0
    for i in range(0, 4):
        i += 1
        x = deck()
        while True:
            if x in test:
                x = deck()
            else:
                test.append(x)
                break
    # ----------------------------------------------------------------------
    # The player and dealer lists are populated from the test list
    # so that only unique cards are delt for the first hand.
    player.append(test[0])
    player.append(test[1])
    dealer.append(test[2])
    dealer.append(test[3])
    # ----------------------------------------------------------------------
    #print 'Test', test
    print 'Player: ', player
    print 'Dealer: ', dealer
    # ----------------------------------------------------------------------
    # The player is asked to hit or stay after the initial deal
    # The while loop appends the player list with a single unique card from deck()
    # when 'hit' is entered.
    var = raw_input('hit or Stay?')
    while var == 'hit':
        x = deck()
        while True:
            if x in test:
                x = deck()
            else:
                test.append(x)
                player.append(x)
                print 'Player: ', player
                break


        # breaks out of the loop for amount > 21
        if player_sum() > 21:
            print 'BUST!'
            print 'lose money 147'
            #ready_player.lose(amount)
            var = 'stay'
            break

        # Note: this elif statement will allow the player to break out of the loop if they get 21
        # However, it is the architects decision to make the player keep track of the amount they have
        #elif player_sum() == 21:
         #   var = 'stay'
         #   break
        else:
            pass

        var = raw_input('hit or stay:')
    # ----------------------------------------------------------------------
    # Once the PLAYER decides to stay, the while loop is called to append cards to the dealer to try and beat the player
    if var == 'stay':
        while dealer_sum() <= player_sum():
            if player_sum() >= 21:
                break
            else:
                dealer_append()
    # ----------------------------------------------------------------------
    # if PLAYER is dealt an Ace this line of code wil choose a value of 1 or 11 (inside while loop)
    for i in player:
        if i == 'HA' or i == 'CA' or i == 'SA' or i == 'DA':
            cards[i] = 1
            if player_sum() <= 11:
                cards[i] = 11
                pass
            elif player_sum() > 11:
                cards[i] = 1
                pass
            else:
                pass
    # ----------------------------------------------------------------------
    # if DEALER is dealt an Ace this line of code wil choose a value of 1 or 11
    for i in dealer:
        if i == 'HA' or i == 'CA' or i == 'SA' or i == 'DA':
            cards[i] = 1
            if dealer_sum() <= 11:
                cards[i] = 11
            elif dealer_sum() > 11:
                cards[i] = 1
            else:
                pass
    # ----------------------------------------------------------------------
    # this line handles the 21/black Jack outside the while loop
    if player_sum() > 21:
        print 'player Busts, dealer Wins!!!!!!'
        print 'lose money 195'
        ready_player.lose(amount)
    elif player_sum() == 21:
        print 'player Wins!!! 21 =)'
        print 'win money 199'
        ready_player.win(amount)
    else:
        pass
    # ----------------------------------------------------------------------
    # Handels the dealers hands
    if dealer_sum() > 21:
        print 'dealer Busts!, Player Wins!!!'
        print 'win money 207'
        ready_player.win(amount)
    elif dealer_sum() == 21 and player_sum() != 21:
        print 'dealer hit 21! dealer Wins!!!'
        print 'lose money 211'
        ready_player.lose(amount)
    elif dealer_sum() > player_sum() and player_sum() <= 21:
        print 'dealer Wins!'
        print 'lose money 215'
        ready_player.lose(amount)
    else:
        pass

    print 'player: ', player, 'tot: ', player_sum()
    print 'dealer: ', dealer, 'tot: ', dealer_sum()
    print 'player bank roll: ', ready_player.bank_roll
    # ----------------------------------------------------------------------
    # Ends the game if player runs out of money or invites the player to play again
    if ready_player.bank_roll == 0.0:
        break
    elif ready_player.bank_roll < 0.0:
        break
    else:
        print '----------------------------------------------------------------------'
        var = raw_input('Would you like to play again? y/n: ')
        print '----------------------------------------------------------------------'
# ----------------------------------------------------------------------
# End Game
print 'Thanks for playing +)'

