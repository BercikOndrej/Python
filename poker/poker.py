from collections import Counter
CARDS_IN_HAND = 5
CARD_VALUES = {
	"A": 14,
	"K": 13,
	"Q": 12,
	"J": 11
}

def best_hands(hands):
	"""
	Take list of poker hands and returns best poker hand/hands (with the highest rank)
	# """
	hand_values_with_rank = [get_hand_rank(hand) for hand in hands]
	# Here we want max from tuples and not only from rank. First we compare ranks and then other values one by one if ranks are equals -> exactly like in poker
	max_rank = max(hand_values_with_rank)
	return [hands[i] for i in range(len(hands)) if hand_values_with_rank[i] == max_rank]

def edit_hand(hand):
	"""
	Take a poker hand and return with sorted values and Counter object
	"""
	extracted_digits = sorted(
		[CARD_VALUES[card[:-1]] if card[:-1] in CARD_VALUES.keys() else int(card[:-1]) for card in hand.split()],
		reverse= True
	)
	return Counter(extracted_digits).most_common(CARDS_IN_HAND)
	
def get_hand_rank(hand):
	"""
	Take a poker hand and return tuple with rank and with hand values 
	"""
	values, counts = zip(*edit_hand(hand))
	colors = [card[-1] for card in hand.split()]
	values = (5, 4, 3, 2, 1) if values == (14, 5, 4, 3, 2) else values

	# Here we must decide which winning comb poker hand has
	pair = counts[0] == 2
	two_pairs = counts[:2] == (2, 2)
	three_of_kind = counts[0] == 3
	straight = all(digit in range(min(values), min(values) + CARDS_IN_HAND) for digit in values) and len(counts) == CARDS_IN_HAND
	flush = len(set(colors)) == 1
	full_house = counts[:2] == (3, 2)
	four_of_kind = counts[0] == 4
	straight_flush = flush and straight

	rank = (
		8 if straight_flush else
		7 if four_of_kind else
		6 if full_house else
		5 if flush else
		4 if straight else
		3 if three_of_kind else
		2 if two_pairs else
		1 if pair 
		else 0
	)

	return (rank, *values)


# Tests
print( best_hands(["2H 3C 4D 5D 6H", "4S AH 3S 2D 5H"]))