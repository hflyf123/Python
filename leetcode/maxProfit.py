# 假设有一个数组，它的第 i 个元素是一个给定的股票在第 i 天的价格。

# 设计一个算法来找到最大的利润。你可以完成尽可能多的交易（多次买卖股票）。然而，你不能同时参与多个交易（你必须在再次购买前出售股票）。


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        Begin_value = prices[0]
        result = 0
        for p in prices:
            result = max(result, p-Begin_value)
            Begin_value = min(Begin_value, p)
        return result

        print(maxProfit(self, [1, 2, 3]))
