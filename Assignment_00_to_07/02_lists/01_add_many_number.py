# Problem Statement:
# Write a function that takes a list of numbers and returns the sum of those numbers.


print("Add many numbers")

def add_numbers(numbers)->int:
    num :int = 0
    for i in numbers:
        num +=i
    return num   
def main():
    numbers:list[int] = [10,20,30,40,50,60,70,80,90,100]
    sum = add_numbers(numbers)
    print(sum)

if __name__ == '__main__':
    main()
