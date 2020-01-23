hand_rank = {
    'High Card': 1,
    'Pair': 2,
    'Two Pair': 3,
    'Three of a Kind': 4,
    'Straight': 5,
    'Flush': 6,
    'Full House': 7,
    'Four of a Kind': 8,
    'Straight Flush': 9,
    'Royal Flush': 10,

}

with open("poker.txt") as f:
    # parse line
        # get player 1 hand
        # get player 2 hand

    # Rank Player 1 hand
        # get all possible plays
        # choose best play, determine score
        # sum value of cards in play
        # sort all cards in hand by

    # Rank Player 2 hand
        # same steps as player 1

    # Compare hands
        # compare rank of plays
            # If win/lose: return
            # If tie:
                #compare sum of card values in play
                    # If win/lose: return
                    # If tie:
                        # for cards in hands:
                            # compare high card value
                            # If higher card exists: return win/lose
                            # If tie, move to next card.