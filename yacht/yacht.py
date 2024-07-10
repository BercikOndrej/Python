# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def digits(number, dice):
    return dice.count(number) * number


def score(dice, category):
    match category:
        case 0:
            final_score = 50 if len(set(dice)) == 1 else 0
        case category if category in range(1, 7):
            final_score = digits(category, dice)
        case 7:
            if all(dice.count(digit) > 1 for digit in dice) and len(set(dice)) == 2:
                final_score = sum(dice)
            else:
                final_score = 0
        case 8:
            dice_set = set(dice)
            dice_count = set([dice.count(digit) for digit in dice])
            if len(dice_set) == 1:
                final_score = 4 * dice_set.pop()
            elif len(dice_set) == 2 and 1 in dice_count and 4 in dice_count:
                elem = dice_set.pop()
                final_score = elem if dice.count(elem) == 4 else dice_set.pop()
                final_score *= 4
            else:
                final_score = 0
        case 9:
            final_score = 30  if sorted(dice) == [1, 2, 3, 4, 5] else 0
        case 10:
            final_score = 30  if sorted(dice) == [2, 3, 4, 5, 6] else 0
        case 11:
            final_score = sum(dice)

    return final_score
