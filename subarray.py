# this is a program to find a subarrray of unsorted non negative integers 
# task is to find a continuos subarray whose sum equals a specified value target.
# function to find subarray
def subarray(list,target):
    current_sum = 0
    start_index = 0
    for end_index in range(len(list)):
        current_sum += list[end_index]
        while current_sum > target and start_index <= end_index:
            current_sum -= list[start_index]
            start_index += 1
        if current_sum == target:
            return start_index +1, end_index +1
    return None
def userinput():
    list1 = []
    n = int(input("enter the number of data elements: "))
    for i in range(n):
        x= int(input("enter the element: "))
        list1.append(x)
    target = int(input("enter the target number"))
    return list1, target
list1, target = userinput()
result = subarray(list1, target)
if result:
    print(f"subarray with sum {target} found at indices: {result}")
else:
    print(f"No subarray wiith sum {target} found.")
