from typing_extensions import Protocol

CARDS = {
    'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
    '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
}


def evaluate_hand(hand: list):
    
    def is_consecutive(sequence: list):
        return sorted(sequence) == list(range(min(sequence), max(sequence)+1))

    count = 0
    is_flush = False
    is_straight = False
    four_of_a_kind = False
    three_of_a_kind = False
    two_of_a_kind = False
    my_max = []
    max_of_match = []
    card_nums = [CARDS[card[0]] for card in hand]
    is_straight = is_consecutive(card_nums)
    vals = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    if len(set(suits)) == 1:
        is_flush = True
    for card in CARDS:
        card = str(card)
        if vals.count(card) == 4:
            print(f'4 of a kind: {hand}')
            max_of_match = CARDS[card]
            four_of_a_kind = True
            for j in vals:
                if j != card:
                    my_max.append(CARDS[j])
            max_card = max(my_max)
        elif vals.count(card) == 3:
            max_of_match = CARDS[card]
            three_of_a_kind = True
            for j in vals:
                if j != card:
                    my_max.append(CARDS[j])
            max_card = max(my_max)
        elif vals.count(card) == 2:
            max_of_match = CARDS[card]
            two_of_a_kind = True
            count += 1
            for j in vals:
                if j != card:
                    my_max.append(CARDS[j])
    if my_max:
        max_card = max(my_max)
    sorted_hand = sorted(hand)
    if sorted_hand[0].startswith('A'):
        starts_with_ace = True
    if is_straight and is_flush and starts_with_ace:
        return 500, 0, hand, 0
    elif is_straight and is_flush:
        max_card_list = list(dict.fromkeys(card_nums))
        max_card = max(max_card_list)
        return 450, max_card, hand, 0
    elif four_of_a_kind:
        return 400, max_card, hand
    elif two_of_a_kind and three_of_a_kind:
        return 350, max_card, hand, 0
    elif is_flush:
        max_card_list = list(dict.fromkeys(card_nums))
        max_card = max(max_card_list)
        return 300, max_card, hand, 0
    elif is_straight:
        max_card_list = list(dict.fromkeys(card_nums))
        max_card = max(max_card_list)
        return 250, max_card, hand, 0
    elif three_of_a_kind:
        return 200, max_card, hand, max_of_match
    elif two_of_a_kind and count > 1:
        return 100, max_card, hand, max_of_match
    elif two_of_a_kind:
        return 50, max_card, hand, max_of_match
    else:
        max_card = max(card_nums)
        return 1, max_card, hand, 0
    

with open('data/p054_poker.txt') as f:
    player_1 = []
    player_2 = []
    player_1_scores = []
    player_2_scores = []
    player_1_wins = 0
    player_2_wins = 0
    for line in f.readlines():
        line = line.strip().split(' ')
        line_len = len(line)
        line_div = line_len // 2
        player_2.append(line[line_div:])
        player_1.append(line[:line_div])

    for hand in player_1:
        player_1_scores.append(evaluate_hand(hand))

    for hand in player_2:
        player_2_scores.append(evaluate_hand(hand))


    zipped_scores = zip(player_1_scores, player_2_scores)

    for set_scores in zipped_scores:
        p1_score = set_scores[0][0]
        p2_score = set_scores[1][0]
        p1_max_card = set_scores[0][1]
        p2_max_card = set_scores[1][1]
        p1_hand = set_scores[0][2]
        p2_hand = set_scores[1][2]
        p1_high = set_scores[0][3]
        p2_high = set_scores[1][3]
        if p1_score > p2_score:
            player_1_wins += 1
        elif p1_score < p2_score:
            player_2_wins += 1
        elif p1_score == p2_score:
            if p1_high > p2_high:
                player_1_wins += 1
            elif p1_high < p2_high:
                player_2_wins += 1
            elif p1_high == p2_high:
                if p1_max_card > p2_max_card:
                    player_1_wins += 1
                elif p1_max_card < p2_max_card:
                    player_2_wins += 1


    print(f'player 1 won: {player_1_wins} - player 2 won: {player_2_wins}')

