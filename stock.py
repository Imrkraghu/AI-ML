#this is a progra to solve gfg problem of stock market sell at maximum profit 
# given the data of days prize where buy at lowest and sell at highest 
# input will be given as the list
#function to check if the stock could be bought
def stock(list,n):
    buy =list[0]
    for i in range(len(list)):
        if(list[i]<buy):
            buy = list[i]
        else:
            i += 1
    if(buy==list[n-1]):
        print("can't buy this stock")
    else:
        stocksell(buy,list)
def stocksell(buy,list):
    sell= list[0]
    for i in range(len(list)):
        if(list[i]>sell):
            sell = list[i]
        else:
            i += 1
    if(buy>=sell):
        print("can't buy this stock")
    else:
        profit = sell - buy
        print(f"profit is {profit}")
def inputdata():
    listdata = []
    print("this is a program which will decide wether to buy a stock or not based on the price history ")
    n = int(input("enter the number of data elements: "))
    for i in range(0,n):
        ele = int(input( ))
        listdata.append(ele)
    stock(listdata,n)
inputdata()