from itertools import combinations

ROW_ALLOWED = "+-"
COL_ALLOWED = "+|"

def rectangles(strings):
    return sum([
            1 for verticles
            in combinations(get_all_verticles(strings), 4)
            if is_rectangle(verticles, strings)
        ]
    )

def get_all_verticles(strings):
    """
    Return all verticles coordination
    """
    return [
        (row_index, col_index)
        for row_index, row in enumerate(strings)
        for col_index, symbol in enumerate(row)
        if symbol == "+"
    ]

def is_complete_vertical_side(start, end, strings):
    """
    Returns True if vertical side is comlete in a diagram
    """
    x1, y1 = start
    x2, y2 = end

    return y1 == y2 and x1 < x2 and \
        all(strings[index][y1] in COL_ALLOWED for index in range(x1, x2 + 1))

def is_complete_horizontal_side(start, end, strings):
    """
    Returns True if horizontal side is comlete in a diagram
    """
    x1, y1 = start
    x2, y2 = end

    return x1 == x2 and y1 < y2 and \
        all(strings[x1][index] in ROW_ALLOWED for index in range(y1, y2 + 1))    


def is_rectangle(verticles, strings):
    left_top, right_top, left_bottom, right_bottom = list(sorted(verticles))

    return all([
        is_complete_horizontal_side(left_top, right_top, strings),
        is_complete_horizontal_side(left_bottom, right_bottom, strings),
        is_complete_vertical_side(left_top, left_bottom, strings),
        is_complete_vertical_side(right_top, right_bottom, strings)
    ])
