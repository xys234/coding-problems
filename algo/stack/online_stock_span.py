"""

Write a class StockSpanner which collects daily price quotes for some stock,
and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days
(starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85],
then the stock spans would be [1, 1, 1, 2, 1, 4, 6].



Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation:
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.


Note:

Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
There will be at most 10000 calls to StockSpanner.next per test case.
There will be at most 150000 calls to StockSpanner.next across all test cases.
The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.

History:
2019.02
2019.07

"""


class StockSpanner:

    def __init__(self):
        self.prices = []

    def next1(self, price: 'int') -> 'int':
        """

        :param price:
        :return:

        Time: O(n)
        Space: O(n)

        """
        self.prices.append(price)
        self.spans.append(1)
        current_day = day_ptr = len(self.prices) - 1
        while day_ptr > 0:
            prev_day = day_ptr - self.spans[day_ptr]
            if prev_day >= 0 and self.prices[current_day] >= self.prices[prev_day]:
                self.spans[current_day] += self.spans[prev_day]
                day_ptr = prev_day
            else:
                break
        return self.spans[-1]

    def next(self, price: 'int') -> 'int':

        span = 1
        while self.prices and self.prices[-1][0] <= price:
            span += self.prices.pop(-1)[1]
        self.prices.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


if __name__=='__main__':
    spanner = StockSpanner()

    cases = (
            ([100, 80, 60, 70, 60, 75, 85], [1,1,1,2,1,4,6]),
    )

    for i, case in enumerate(cases):
        inputs, expected = case
        ans = []
        for p in inputs:
            ans.append(spanner.next(p))
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))
