# Problem Statement
# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

print("Get List")

def main():
    lst = []
    val = input("Enter a value to add the list : ")
    while val:
        lst.append(val)
        val = input("Enter a value to add the list : ")
    print("Here is the list " , lst)    

if __name__ == '__main__':
    main()