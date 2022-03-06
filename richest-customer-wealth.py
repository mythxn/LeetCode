class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        balances = []

        for customer in accounts:
            sum = sum(customer)
            balances.append(sum)

        return max(balances)