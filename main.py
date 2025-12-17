from itertools import combinations

ITEMS = [
    ('r', 'rifle', 3, 25),
    ('p', 'pistol', 2, 15),
    ('a', 'ammo', 2, 15),
    ('m', 'medkit', 2, 20),
    ('i', 'inhaler', 1, 5),
    ('k', 'knife', 1, 15),
    ('x', 'axe', 3, 20),
    ('t', 'talisman', 1, 25),
    ('f', 'flask', 1, 15),
    ('d', 'antidot', 1, 10),
    ('s', 'supplies', 2, 20),
    ('c', 'crossbow', 2, 20),
]

CAPACITY = 8
BASE_POINTS = 10
REQUIRED_ITEM = 'd'
NUMBER_ITEMS = len(ITEMS)

total_all_points = sum(item[3] for item in ITEMS)

best_items = []
best_score = float('-inf')

# Перебор всех комбинаций предметов
for count_item in range(1, NUMBER_ITEMS + 1):
    for combinat in combinations(range(NUMBER_ITEMS), count_item):
        size = sum(ITEMS[i][2] for i in combinat)
        if size > CAPACITY:
            continue

        symbols = [ITEMS[i][0] for i in combinat]
        if REQUIRED_ITEM not in symbols:
            continue

        taken_points = sum(ITEMS[i][3] for i in combinat)
        not_taken_points = total_all_points - taken_points
        final_points = BASE_POINTS + taken_points - not_taken_points

        if final_points <= 0:
            continue

        if final_points > best_score:
            best_score = final_points
            best_items = combinat

# Формирование инвентаря
cells = []
for i in best_items:
    symbol, _, size, _ = ITEMS[i]
    cells.extend([symbol] * size)

cells.extend(['.'] * (CAPACITY - len(cells)))

inventory = [cells[:4], cells[4:8]]

# Вывод результатов
print('Инвентарь:')
for row in inventory:
    print(' '.join(f'[{cell}]' for cell in row))

print(f'\nИтоговые очки выживания: {best_score}')
