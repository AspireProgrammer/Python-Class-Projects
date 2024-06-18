# Final Project
# Rebekah Shi
# 4/18/24
import random
import sqlite3

# initialize
counter = 0
card = ''
#hit or stand value
hit_or_stand = ''
# initialize the player
player_hand_score = 0
player = []
# initialize the dealer
dealer = []
dealer_hand_score = 0
# initialize the card deck with array for ease of shuffling and indexing
card_deck = ['2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds',
             '8 of Diamonds', '9 of Diamonds', '10 of Diamonds',
             'jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds', '2 of Spades',
             '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades',
             '10 of Spades',
             'jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades', '2 of Clubs', '3 of Clubs',
             '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs',
             'jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs', '2 of Hearts', '3 of Hearts',
             '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts',
             'jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Hearts']
# initialize card scores
card_score = {'2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
              '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9, '10 of Diamonds': 10,
              'jack of Diamonds': 10, 'Queen of Diamonds': 10, 'King of Diamonds': 10, 'Ace of Diamonds': 11,
              '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
              '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10,
              'jack of Spades': 10, 'Queen of Spades': 10, 'King of Spades': 10, 'Ace of Spades': 11, '2 of Clubs': 2,
              '3 of Clubs': 3, '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8,
              '9 of Clubs': 9, '10 of Clubs': 10,
              'jack of Clubs': 10, 'Queen of Clubs': 10, 'King of Clubs': 10, 'Ace of Clubs': 11, '2 of Hearts': 2,
              '3 of Hearts': 3, '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts': 7,
              '8 of Hearts': 8, '9 of Hearts': 9, '10 of Hearts': 10,
              'jack of Hearts': 10, 'Queen of Hearts': 10, 'King of Hearts': 10, 'Ace of Hearts': 11}


# shuffle the cards function
def shuffle():
    # generate random number to deal the card and append card to the hand
    number = random.randint(1, 51)
    card = card_deck[number]
    player.append(card)
    dealer.append(card)


# calculate the hand score
def calculate_player_hand_score(player_hand):
    global player_hand_score
    #for each card in the player's hand, get the key value and add to the score
    for card in player:
        player_hand_score = card_score[card] + player_hand_score
    return player_hand_score


def calculate_dealer_hand_score(dealer_hand):
    global dealer_hand_score
    # for each card in the player's hand, get the key value and add to the score
    for card in dealer:
        dealer_hand_score = card_score[card] + dealer_hand_score
    return dealer_hand_score

# hit function take a card randomly and return the card
def hit():
    global card
    number = random.randint(1, 51)
    card = card_deck[number]
    return card


# stand function
def stand():
    print('Player chose to stand')


# if dealer hand is <= 16, must hit. if hit, append the card to the hand if not, stand
def dealer_play():
    if dealer_hand_score <= 16:
        hit()
        dealer.append(card)
        calculate_dealer_hand_score(dealer)
    if 16 < dealer_hand_score < 20:
        stand()
    return dealer_hand_score


# if hand is <= 17, must hit, if hit, append the card to the hand if not, stand
def player_play():
    global hit_or_stand
    hit_or_stand_random = random.randint(1, 2)
    if hit_or_stand_random == 1:
        hit()
        player.append(card)
        calculate_player_hand_score(player)
        hit_or_stand = 'Hit'
    if hit_or_stand_random == 2:
        stand()
        hit_or_stand = 'Stand'
    return player_hand_score


# main game
# welcome the player
print("Welcome to the card game Blackjack! \n Here are the rules:")
# explain the rules
print(
    'The point of the game is to get your hand as close to 21 without exceeding. If your hand exceeds 21, you automatically lose\n Aces counted as 11\n Face cards count as 10 points \n All other cards count as face value e.g 2 of Spades is = 2 points')
print('You can choose to play (request another card) of stop (keep a hold on your cards)')
bet = input('What is the amount you would like to place?')
blackjack = int(bet) * 1.5
# Make a table using sql
#connect to database and create the file
conn = sqlite3.connect('plays.sqlite')
cur = conn.cursor()
#if the table exists, drop and create new to write new table
cur.execute('DROP TABLE IF EXISTS Plays')
sql_command = """CREATE TABLE Plays (
                                      Starting INTEGER, 
                                      Play CHAR, 
                                      Result CHAR);"""
cur.execute(sql_command)
#while the game is less than 100,000 keep the game going,
while counter <= 100000:
    #every time the hand is played, discard the cards, rest the score, and shuffle new cards.
    dealer = []
    player = []
    player_hand_score = 0
    dealer_hand_score = 0
    shuffle()
    #if the first is blackjack declare blackjack and print payout.
    if player_hand_score == 21:
        print('Player Blackjack! Payout ' + str(blackjack))
        cur.execute("INSERT INTO Plays VALUES (?, ?, ?)", (player_hand_score, 'Blackjack', 'Win'))
        conn.commit()
    #if player loses, declare nothing and loss
    if dealer_hand_score == 21:
        print('Dealer Wins. Player loses. Payout ' + bet)
        cur.execute("INSERT INTO Plays VALUES (?, ?, ?)", (player_hand_score, 'N/A', 'Lose'))
        conn.commit()
    dealer_play()
    player_play()
    # check winner
    # if player loses, declare the play made and loss or win depending on the condition, commit to table, and then add the counter
    #if the player is a bust
    if player_hand_score > 21:
        print('Player loses. Pay ' + bet)
        cur.execute("INSERT INTO Plays VALUES (?, ?, ?)", (player_hand_score, hit_or_stand, 'Lose'))
        conn.commit()
        counter = counter + 1
    #if the dealer is a bust
    if dealer_hand_score > 21:
        print("Player Wins. Payout " + bet)
        cur.execute("INSERT INTO Plays VALUES (?, ?, ?)", (player_hand_score, hit_or_stand, 'Win'))
        conn.commit()
        counter = counter + 1
    #if the hand is 21
    if player_hand_score == 21:
        print('Player Wins! Payout ' + bet)
        cur.execute("INSERT INTO Plays VALUES (?, ?, ?)", (player_hand_score, hit_or_stand, 'Win'))
        conn.commit()
        counter = counter + 1
    #if the hand of the dealer is equal to 21
    if dealer_hand_score == 21:
        print('Dealer Wins. Player loses. Pay ' + bet)
        cur.execute("INSERT INTO Plays VALUES (?, ?, ?)", (player_hand_score, hit_or_stand, 'Lose'))
        conn.commit()
        counter = counter + 1
    #if they draw
    if dealer_hand_score == player_hand_score:
        cur.execute("INSERT INTO Plays VALUES (?, ?, ?)", (player_hand_score, hit_or_stand, 'Draw'))
        conn.commit()
        counter = counter + 1
        print('Draw')
    #if one hand is closer to one
    if (21 - player_hand_score) > (21 - dealer_hand_score):
        print('Dealer wins. Player loses. Pay ' + bet)
        cur.execute("INSERT INTO Plays VALUES (?, ?, ?)", (player_hand_score, hit_or_stand, 'Lose'))
        conn.commit()
        counter = counter + 1
    #if the player's hand is closer to 21
    if (21 - player_hand_score) < (21 - dealer_hand_score):
        print('Player wins. Dealer loses. Payout ' + bet)
        cur.execute("INSERT INTO Plays VALUES (?, ?, ?)", (player_hand_score, hit_or_stand, 'Win'))
        conn.commit()
        counter = counter + 1

#display the table
print('Plays:')
cur.execute('SELECT Starting, Play, Result FROM Plays')
for row in cur:
    print(row)
conn.close()
