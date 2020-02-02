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

card_values = {
            '8': 8,
    '2': 2, '9': 9,
    '3': 3, 'T': 10,
    '4': 4, 'J': 11,
    '5': 5, 'Q': 12,
    '6': 6, 'K': 13,
    '7': 7, 'A': 14
}


def getValues(hand):
    """
    Returns a list of the card values found in a hand,

    Example: [2H, 3S, KC, JS, AD] ---> [2, 3, K, J, A]
    :param hand:
    :return:
    """
    return [card[0] for card in hand][::-1]


def play(file):
    p1_wins = 0
    p2_wins = 0
    with open(file) as f:
        for line in f.readlines():
            hands = line.rstrip('\n').split()
            p1_hand = hands[0:5]
            p2_hand = hands[5:]
            winner = compare_hands(p1_hand, p2_hand)
            if winner == 'Player 1':
                p1_wins += 1
            if winner == 'Player 2':
                p2_wins += 1
            print("WINNER: ", winner, "\n ---------------------")

    print("Player 1 wins: ", p1_wins)
    print("Player 2 wins: ", p2_wins)



def getPairs(hand: list):
    value_list = getValues(hand)
    pairs = []
    counted = []
    for value in value_list:
        if value_list.count(value) == 2 and value not in counted:
            pairs.append(value)
            counted.append(value)

    return pairs


def getPair(hand: list):
    return getPairs(hand)[0]


def isPair(hand: list):
    pairs = getPairs(hand)
    if len(pairs) > 0:
        return True
    return False


def isThree(hand):
    value_list = getValues(hand)
    for value in value_list:
        if value_list.count(value) == 3:
            return True
    return False


def getThree(hand):
    value_list = getValues(hand)
    for value in value_list:
        if value_list.count(value) == 3:
            return value


def isFour(hand):
    value_list = getValues(hand)
    for value in value_list:
        if value_list.count(value) == 4:
            return True
    return False


def getFour(hand):
    value_list = getValues(hand)
    for value in value_list:
        if value_list.count(value) == 4:
            return value


def isTwoPair(hand: list):
    pairs = getPairs(hand)
    if len(pairs) == 2:
        return True
    return False


def isFullHouse(hand):
    if isPair(hand) and isThree(hand):
        print("Pair: ", getPair(hand))
        print("Three:", getThree(hand))
        if getPair(hand) != getThree(hand):
            return True
    return False


def isFlush(hand: list):
    first = hand[0][1]
    return all([x[1] == first for x in hand])


def isStraight(hand):
    return all(card_values[a[0]] + 1 == card_values[b[0]] for a, b in zip(hand, hand[1:]))


def isStrFlush(hand):
    is_straight = isStraight(hand)
    is_flush = isFlush(hand)
    if is_flush and is_straight:
        return True
    else:
        return False


def isRoyalFlush(hand):
    value = sum([card_values[card[0]] for card in hand])
    if value == 60 and isFlush(hand):
        return True
    else:
        return False


def sort_hand(hand: list):
    """
    In place sort of hand by card value.

    :param hand:
    :return:
    """
    hand.sort(key=lambda card: card_values[card[0]])


def find_plays(hand: list):
    """
    This method looks at a player's hand and finds all possible plays (Pair, Flush, Straight, etc.).
    It also assigns a rank to the play that is relative to other plays of the same type. (example, a pair of twos
    is ranked lower than a pair of queens). After a play is found and a rank assigned, the play and rank tuple are
    appended to the list.

    The determination of rank depends on the type of play. For pairs aor three of a kind, rank is simply based on the
    card values. A pair of twos is rank 2. A three of a kind of tens is rank 10. For a full house, the set of three
    cards is evaluated. For Straights, Flushes, Straight Flush, and Royal Flush, value is assigned by the highest card
    in the hand.

    Play rank is used to determine who the winner is if two players make the same play (both have 4 of a kind, or both
    have a flush).

    :param hand: A hand of 5 cards.
    :return: A list of tuples in the format (play, rank), where the rank is a comparison of the play to others of
        the same type.
    """
    high_card_value = card_values[hand[4][0]]
    plays = [('High Card', high_card_value)]

    # Is Flush?
    if isFlush(hand):
        tie_card = hand[4]
        tie_value = card_values[tie_card[0]]
        plays.append(('Flush', tie_value))

    if isStraight(hand):
        tie_card = hand[4]
        tie_value = card_values[tie_card[0]]
        plays.append(('Straight', tie_value))

    if isRoyalFlush(hand):
        tie_card = hand[4]
        tie_value = card_values[tie_card[0]]
        plays.append(('Royal Flush', tie_value))

    if isStrFlush(hand):
        tie_card = hand[4]
        tie_value = card_values[tie_card[0]]
        plays.append(('Straight Flush', tie_value))

    if isPair(hand):
        pair = getPairs(hand)
        tie_value = card_values[pair[0]]
        plays.append(('Pair', tie_value))

    if isTwoPair(hand):
        pairs = getPairs(hand)
        tie_value = card_values[max(pairs)]
        plays.append(('Two Pair', tie_value))

    if isThree(hand):
        tie_value = card_values[getThree(hand)]
        plays.append(("Three of a Kind", tie_value))

    if isFour(hand):
        tie_value = getFour(hand)
        plays.append(("Four of a Kind", tie_value))

    if isFullHouse(hand):
        tie_value = getThree(hand)
        plays.append(("Full House", tie_value))

    plays.sort(key=lambda x: hand_rank[x[0]])

    return plays


def get_best(hand):
    plays = find_plays(hand)
    if len(plays) == 0:
        return 'High Card'
    else:
        return plays[len(plays) - 1]


def compare_hands(p1_hand, p2_hand):
    sort_hand(p1_hand)
    sort_hand(p2_hand)

    # get all possible plays, and choose the best one.
    p1_plays = find_plays(p1_hand)
    p2_plays = find_plays(p2_hand)

    p1_choice, p1_tie_value = get_best(p1_hand)
    p2_choice, p2_tie_value = get_best(p2_hand)

    print("Player 1 Hand: ", end=' ')
    for card in p1_hand:
        print(card, end=' ')

    print("\nPlayer 1 hand possibilites:")
    for play in p1_plays:
        print(play[0], end=', ')

    print("\nPlayer 1 lays: \n", p1_choice, "with tie value", p1_tie_value)
    print(" High Card: ", p1_hand[4], '\n')

    print("Player 2 Hand: ", p2_hand)
    print("Player 2 hand possibilites: \n", p2_plays)
    print("Player 2 plays: \n", p2_choice)
    print(" High Card: ", p2_hand[4])

    # Check ranks of players choice of plays:
    if hand_rank[p1_choice] > hand_rank[p2_choice]:
        return 'Player 1'
    if hand_rank[p2_choice] > hand_rank[p1_choice]:
        return 'Player 2'

    # Tie Case 1: Two players make same play, check value of play (i.e. pair of queens beats pair of twos)
    if p1_choice == p2_choice:

        if p1_tie_value > p2_tie_value:
            return 'Player 1'
        if p2_tie_value > p1_tie_value:
            return 'Player 2'

        # Tie Case 2: Both players have identical play (i.e. p1 and p2 both play pair of twos)
        if p1_choice == p2_choice and p1_tie_value == p2_tie_value:

            p1_values = getValues(p1_hand)
            p2_values = getValues(p2_hand)

            # Compare high cards. If both players have same high card, check next highest cards. If both players
            # have identical cards, then there is a true tie.
            for card_value_p1, card_value_p2 in zip(p1_values, p2_values):
                p1_rank = card_values[card_value_p1]
                p2_rank = card_values[card_value_p2]
                if p1_rank > p2_rank:
                    return 'Player 1'
                if p2_rank > p1_rank:
                    return 'Player 2'
            return 'Tie'


if __name__ == '__main__':
    play('data\\p054_poker.txt')

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