
def minimum_coins(target_value: int, coins: list[int]) -> int:
    """ Find minimum number of values 'coins' needed to make change 'target_value' """

    min_coins_needed = [float('inf') for i in range(target_value+1)]
    min_coins_needed[0] = 0

    for coin in coins:
        for current_target in range(len(min_coins_needed)):
            if coin <= current_target:
                min_coins_needed[current_target] = min(
                    min_coins_needed[current_target], 1 + min_coins_needed[current_target-coin])
    return min_coins_needed[target_value]


print(minimum_coins(5, [1, 2, 3]))
