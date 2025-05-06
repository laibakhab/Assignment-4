# Problem statement
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

print("GEt last element")

def get_last_element(lst):
    print(lst[-1])

def get_lst():
    lst = []
    elem:str = input("Enter an element to add to the list : ") 
    while elem != '':
        lst.append(elem)
        elem = input("Enter an element to add to the list : ")
    return lst

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == '__main__':
    main()           
