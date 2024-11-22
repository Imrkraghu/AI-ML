#this is a progra to solve gfg problem of stock market sell at maximum profit 
# given the data of days prize where buy at lowest and sell at highest 
# input will be given as the list
#function to check if the stock could be bought
def stock(prices):
    if not prices:
        print("Empty price list. Cannot determine buy/sell.")
        return

    # Initialize variables to track the minimum price and maximum profit
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        # Update the minimum price if a lower price is found
        if price < min_price:
            min_price = price

        # Calculate the profit if selling at the current price
        profit = price - min_price

        # Update the maximum profit if the current profit is higher
        if profit > max_profit:
            max_profit = profit

    if max_profit == 0:
        print("No profitable transaction possible.")
    else:
        print(f"Maximum profit is {max_profit}")

def inputdata():
    listdata = []
    print("this is a program which will decide wether to buy a stock or not based on the price history ")
    n = int(input("enter the number of data elements: "))
    for i in range(0,n):
        ele = int(input( ))
        listdata.append(ele)
    stock(listdata)
inputdata()