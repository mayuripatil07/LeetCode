class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i = 1
        stack = [0]
        while(i < len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] = prices[stack[-1]] -  prices[i]
            stack.append(i)
            i += 1

        return prices
