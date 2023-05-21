import tkinter as tk
import random


def blackjack():
    global deck, player_hand, dealer_hand, values
    deck = create_deck()
    random.shuffle(deck)
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    values = {"Ace": 11,
              "2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9,
              "10": 10,
              "Jack": 10,
              "Queen": 10,
              "King": 10
              }

    canvas.delete("all")
    canvas.create_text(100, 50, text="Let's play Blackjack!")
    print_hand("Player", player_hand)
    canvas.create_text(100, 150, text=f"Dealer's face-up card: {dealer_hand[0]}")


def create_deck():
    deck = []
    suits = ["hearts", "diamonds", "clubs", "spades"]

    for suit in suits:

        for value in values:
            deck.append(f"{value} of {suit}")
    return deck


values = {"Ace",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7",
          "8",
          "9",
          "10",
          "Jack",
          "Queen",
          "King"
          }


def deal_card():
    return random.choice(list(values))


def get_hand_value(hand, values):
    value = sum([values[card.split()[0]] for card in hand])

    if value > 21 and "Ace" in hand:
        value -= 10
    return value


def print_hand(name, hand):
    y = 150
    canvas.create_text(230, y, text=f"{name}'s hand:", anchor="nw")
    y += 20

    for card in hand:
        canvas.create_text(230, y, text=card, anchor="nw")
        y += 20
    canvas.create_text(230, y, text=f"Value: {get_hand_value(hand, values)}", anchor="nw")


def add_card_to_hand(hand):
    hand.append(deal_card())


def new_game():
    global hit_button, stand_button
    blackjack()
    hit_button.configure(state="active")
    stand_button.configure(state="active")


def close_window():
    window.destroy()


def hit():
    canvas.create_rectangle(0, 0, 450, 350, fill="green")
    add_card_to_hand(player_hand)
    card_value = get_hand_value(player_hand, values)
    canvas.delete("player_draw")
    canvas.create_text(180, 320,
                       text=f"You drew {player_hand[-1]}. (Value: {card_value})", fill="white", tags="player_draw")

    print_hand("Player", player_hand)

    if card_value > 21:
        canvas.create_text(150, 300,
                           text=f"You bust! Dealer wins. (Value: {card_value})", fill="white")

        hit_button.configure(state="disabled")
        stand_button.configure(state="disabled")


def stand():
    canvas.create_rectangle(0, 0, 500, 400, fill="green")

    while get_hand_value(dealer_hand, values) < 17:
        add_card_to_hand(dealer_hand)
    dealer_value = get_hand_value(dealer_hand, values)
    player_value = get_hand_value(player_hand, values)
    print_hand("Dealer", dealer_hand)
    canvas.delete("dealer_result")
    canvas.create_text(110, 340,
                       text=f"Dealer busts! You win. (Value: {player_value})", fill="white", tags="dealer_result")

    if dealer_value > 21:
        canvas.create_text(130, 360,
                           text=f"Dealer busts! You win. (Value: {player_value})", fill="white")

    elif dealer_value == player_value:
        canvas.create_text(200, 320,
                           text=f"It's a tie! (Value: {player_value})", fill="white")

    elif dealer_value > player_value:
        canvas.create_text(160, 270,
                           text=f"Dealer wins! (Value: {player_value})", fill="white")

    else:
        canvas.create_text(230, 300,
                           text=f"You win! (Value: {player_value})", fill="white")

    print_hand("Dealer", dealer_hand)
    hit_button.configure(state="disabled")
    stand_button.configure(state="disabled")


window = tk.Tk()
window.title("Blackjack")


new_game_button = tk.Button(window, text="New Game", command=new_game)
new_game_button.pack()


close_button = tk.Button(window, text="Close", command=close_window)
close_button.pack()

hit_button = tk.Button(window, text="Hit", command=hit, state="disabled")
hit_button.pack(side="left")


stand_button = tk.Button(window, text="Stand", command=stand, state="disabled")
stand_button.pack(side="left")


canvas = tk.Canvas(window, width=500, height=400, bg="green")
canvas.pack()


window.mainloop()
