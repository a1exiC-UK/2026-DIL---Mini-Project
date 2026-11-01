import time

def ascending(number):
    start = time.perf_counter()
    for i in range(len(number)):
        for x in range (len(number)-1-i):
            if number[x] > number[x+1]:
                number[x], number[x+1] = number[x+1], number[x]
    end = time.perf_counter()
    print(number)
    elapsed = (end - start) * 1000
    print(f'Time taken: {elapsed:.3f} milliseconds')

def descending(number):
    start = time.perf_counter()
    for i in range(len(number)):
        for x in range (len(number)-1-i):
            if number[x] < number[x+1]:
                number[x], number[x+1] = number[x+1], number[x]
    end = time.perf_counter()
    print(number)
    elapsed = (end - start) * 1000
    print(f'Time taken: {elapsed:.3f} milliseconds')

def wordsOLD():
    strng = "I like pineapples 123123123"
    char = list(strng)
    sortcategories = [[], [], []]
    for part in char:
        if part.isalpha():
            category = 0
        elif part.isdigit():
            category = 1
        else:
            category = 2
        sortcategories[category].append(part)
    for category in sortcategories:
        for i in range(len(category)):
            for x in range (len(category)-1-i):
                if category[x] > category[x+1]:
                    category[x], category[x+1] = category[x+1], category[x]
        result = ''.join(sortcategories[0] + sortcategories[1] + sortcategories[2])
    print("'" + result + "'")

def asciiwords():
    strng = input("Enter a string: ")
    strng = list(strng)
    start = time.perf_counter()
    for i in range(len(strng)):
        for x in range(len(strng)-1-i):
            a = 127 if strng[x] == " " else ord(strng[x])
            b = 127 if strng[x+1] == " " else ord(strng[x+1])   
            if a > b:
                strng[x], strng[x+1] = strng[x+1], strng[x]
    end = time.perf_counter()
    result = ''.join(strng)
    print("'" + result + "'")
    elapsed = (end - start) * 1000
    print(f'Time taken: {elapsed:.3f} milliseconds')

def main():
    while True:
        print("1. Sort numbers in ascending order")
        print("2. Sort numbers in descending order")
        print("3. Sort characters in a string")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            number = list(map(float, input("Enter numbers separated by spaces: ").split()))
            ascending(number)
        elif choice == "2":
            number = list(map(float, input("Enter numbers separated by spaces: ").split()))
            descending(number)
        elif choice == "3":
            asciiwords()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

main()
