import time

def ascending(number):
    start = time.perf_counter()
    for i in range(len(number)):
        for x in range(len(number)-1-i):
            if number[x] > number[x+1]:
                number[x], number[x+1] = number[x+1], number[x]
    end = time.perf_counter()
    elapsed = (end - start) * 1000
    return number, elapsed

def descending(number):
    start = time.perf_counter()
    for i in range(len(number)):
        for x in range(len(number)-1-i):
            if number[x] < number[x+1]:
                number[x], number[x+1] = number[x+1], number[x]
    end = time.perf_counter()
    elapsed = (end - start) * 1000
    return number, elapsed

def asciiwords(strng):
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
    elapsed = (end - start) * 1000
    return result, elapsed

passed = 0
failed = 0

def show(test_name, given, expected, actual, timing):
    global passed, failed
    print(test_name)
    print("  Input:    ", given)
    print("  Expected: ", expected)
    print("  Actual:   ", actual)
    print("  Time:     ", timing)
    if actual == expected:
        print("  PASS")
        passed += 1
    else:
        print("  FAIL")
        failed += 1
    print()

def test_numbers(function, test_name, typed, expected):
    try:
        numbers = list(map(float, typed.split()))
        actual, elapsed = function(numbers)
        timing = f"{elapsed:.3f} milliseconds"
    except ValueError:
        actual, timing = "Invalid input", "n/a"
    show(test_name, repr(typed), expected, actual, timing)

def test_string(test_name, given, expected):
    actual, elapsed = asciiwords(given)
    show(test_name, repr(given), repr(expected), repr(actual), f"{elapsed:.3f} milliseconds")

NUMBER_TESTS = [
    ("Ten valid integers",
     "5 3 8 1 9 2 7 4 10 6",
     [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]),
    ("Ten decimals",
     "2.5 1.1 3.75 0.5 2.25 1.0 4.5 0.1 3.3 2.0",
     [0.1, 0.5, 1.0, 1.1, 2.0, 2.25, 2.5, 3.3, 3.75, 4.5]),
    ("Ten negative and positive integers",
     "-3 5 -10 0 2 -1 7 -5 1 3",
     [-10.0, -5.0, -3.0, -1.0, 0.0, 1.0, 2.0, 3.0, 5.0, 7.0]),
    ("Mixture of integers, decimals and negatives",
     "4 2.5 -1 7.75 0 3 -2.5 10 1.5 6",
     [-2.5, -1.0, 0.0, 1.5, 2.5, 3.0, 4.0, 6.0, 7.75, 10.0]),
    ("Text only",
     "a b c d e f g h i j",
     "Invalid input"),
    ("Mixture of numbers and text",
     "1 2 three 4 5 6 7 8 9 10",
     "Invalid input"),
    ("Mixture of decimals and symbols",
     "1.5 2.5 £ 4 5 6 7 8 9 10",
     "Invalid input"),
    ("Number with two decimal points",
     "1 2 3 4 5 6 7 1.2.3 9 10",
     "Invalid input"),
    ("More than ten values (15)",
     "15 3 12 7 1 14 9 5 11 2 13 8 4 10 6",
     [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]),
    ("Less than ten values (5)",
     "9 4 7 1 5",
     [1.0, 4.0, 5.0, 7.0, 9.0]),
    ("One value",
     "42",
     [42.0]),
    ("No values",
     "",
     []),
    ("Ten of the same value",
     "7 7 7 7 7 7 7 7 7 7",
     [7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0]),
    ("Duplicate values",
     "3 1 3 2 1 2 3 1 2 3",
     [1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0]),
    ("Already in ascending order",
     "1 2 3 4 5 6 7 8 9 10",
     [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]),
    ("Already in descending order",
     "10 9 8 7 6 5 4 3 2 1",
     [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]),
    ("Large numbers",
     "1000000 5 999999 42 123456 0 77 500000 1 99",
     [0.0, 1.0, 5.0, 42.0, 77.0, 99.0, 123456.0, 500000.0, 999999.0, 1000000.0]),
]

print("========== ASCENDING ==========\n")
for test_name, typed, expected in NUMBER_TESTS:
    test_numbers(ascending, test_name, typed, expected)

print("========== DESCENDING ==========\n")
for test_name, typed, expected in NUMBER_TESTS:
    if expected != "Invalid input":
        expected = expected[::-1]
    test_numbers(descending, test_name, typed, expected)

print("========== STRING SORT ==========\n")
test_string("Lowercase word", "hello", "ehllo")
test_string("Capitals come before lowercase", "Zebra", "Zaber")
test_string("Mixed case with a space", "Hello World", "HWdellloor ")
test_string("Sentence (spaces go to the end)", "The quick brown fox", "Tbcefhiknooqruwx   ")
test_string("Digits only", "9876", "6789")
test_string("Digits come before letters", "cba321", "123abc")
test_string("Mixture of symbols, digits, letters and a space", "Ab3!z ", "!3Abz ")
test_string("Single character", "x", "x")
test_string("Empty string", "", "")

print("========== SUMMARY ==========")
print("Passed:", passed)
print("Failed:", failed)