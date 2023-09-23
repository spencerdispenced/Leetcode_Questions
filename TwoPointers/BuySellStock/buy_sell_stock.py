

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.




1. Create left pointer set to index 0
   Create right pointer set to index 1
   Create var to store max profit

2. Loop right pointer over rest of input array, while right pointer remains in array:

    2.1: Check if value at left pointer(buy) is greater or equl to value at right pointer(sell)

         If so: -Move left pointer to position of right pointer
                -Increment right pointer

        Otherwise: -Calculate current potential profit: Value of left minus value of right
                   -Compare against current max profit, update max profit if current potential is higher
                   -increment right pointer

3. Return max profit


"""


def max_profit(prices: list[int]) -> int:
    left = 0
    right = 1
    max_profit = 0

    while right < len(prices):
        if prices[left] >= prices[right]:
            left = right
            right += 1
        else:
            max_profit = max(max_profit, prices[right] - prices[left])
            right += 1

    return max_profit


if __name__ == '__main__':
    prices1 = [7, 1, 5, 3, 6, 4]  # 5
    prices2 = [7, 6, 4, 3, 1]  # 0
    prices3 = [7, 9, 3, 5, 2, 8]  # 6
    prices4 = [3, 6, 5, 10, 1, 5, 10]  # 9
    print(max_profit(prices1))
    print(max_profit(prices2))
    print(max_profit(prices3))
    print(max_profit(prices4))
