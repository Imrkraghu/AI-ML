# using a function to print the name and age
def hello(to,much):
    print(f"hello, Mr. {to} your age is {much}")
# its my first python program
name = input("what is your full name? ")
#removing whitespace and capitalized name 
name = name.strip().capitalize()
# spliting the name into first and last name
first, last =  name.split(" ")
# taking age as input
age = int(input("enter your age: "))
# using f-string here
hello(last,age)