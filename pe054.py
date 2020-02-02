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
    return [card[0] for card in hand]


def deal(file):
    with open(file) as f:
        for line in f.readlines():
            hands = line.rstrip('\n').split()
            p1_hand = hands[0:5]
            p2_hand = hands[5:]
            winner = compare_hands(p1_hand, p2_hand)
            print("Winner: ", winner, "\n ---------------------")




def getPairs(hand: list):
    value_list = getValues(hand)
    pairs = []
    counted = []
    for value in value_list:
        if value_list.count(value) >= 2 and value not in counted:
            pairs.append(value)
            counted.append(value)

    return pairs


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


def isFour(hand):
    value_list = getValues(hand)
    for value in value_list:
        if value_list.count(value) == 4:
            return True
    return False


def isTwoPair(hand: list):
    pairs = getPairs(hand)
    if len(pairs) == 2:
        return True
    return False


def isFlush(hand: list):
    first = hand[0][1]
    return all([x[1] == first for x in hand])


def isStraight(hand):
    return all(card_values[a[0]] + 1 == card_values[b[0]] for a,b in zip(hand, hand[1:]))


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
    hand.sort(key=lambda card: card_values[card[0]])


def find_plays(hand: list):

    plays = []

    # Is Flush?
    if isFlush(hand):
        plays.append('Flush')

    if isStraight(hand):
        plays.append('Straight')

    if isRoyalFlush(hand):
        plays.append('Royal Flush')

    if isStrFlush(hand):
        plays.append('Straight Flush')

    if isPair(hand):
        plays.append('Pair')

    if isTwoPair(hand):
        plays.append('Two Pair')

    if isThree(hand):
        plays.append("Three of a Kind")

    if isFour(hand):
        plays.append("Four of a Kind")

    if isPair(hand) and isThree(hand):
        plays.append("Full House")

    plays.sort(key=lambda x: hand_rank[x])

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
    p1_high = p1_hand[4]
    p2_high = p2_hand[4]

    # get all possible plays, and choose the best one.
    p1_plays = find_plays(p1_hand)
    p2_plays = find_plays(p2_hand)

    p1_choice = get_best(p1_hand)
    p2_choice = get_best(p2_hand)

    print("Player 1 Hand: ", p1_hand)
    print("Player 1 hand possibilites: \n", p1_plays)
    print("Player 1 plays: \n", p1_choice)
    print(" High Card: ", p1_high, '\n')

    print("Player 2 Hand: ", p2_hand)
    print("Player 2 hand possibilites: \n", p2_plays)
    print("Player 2 plays: \n", p2_choice)
    print(" High Card: ", p2_high)

    if hand_rank[p1_choice] > hand_rank[p2_choice]:
        return 'Player 1'

    if hand_rank[p2_choice] > hand_rank[p1_choice]:
        return 'Player 2'

    if p1_choice == p2_choice:
        return 'Tie'


if __name__ == '__main__':
    deal = deal('data\\p054_poker.txt')


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