"""
Assignment 3: Questions from Test 3
"""

def question1():
    numbers = [1, 2, 3, 4, 5]
    total = 0
    for num in numbers:
        if num == 3:
            break
        total += num
    print(total)


def question2():
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        if num % 2 == 0:
            continue
    print(num)


def question3():
    i= 0
    while i < 5:
        if i == 3:
            break
        i += 1
    print(i) 


def question4():
    x = 10 
    y= 5
    if x > y:
        print("x is greater than y")
    elif x == y:
        print("x is equal to y")
    else:
        print("x is less than y")


def question5():
    i= 0
    while i < 5:
        i += 1
        if i == 3:
            continue
        print(i, end=' ')


def question6():
    numbers = [1, 2, 3, 4, 5]
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    print(total)


def question7():
    x= 5 
    y= 3
    if x > y:
        if x % y == 0:
            print("x is divisible by y")
        else:
            print("x is not divisible by y")
    else:
        print("Invalid comparison")


def question8():
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        if num % 2 == 0:
            break
        print(num)
    else:
        print("All numbers are even")


def question9():
    i= 0
    while i < 5:
        i += 1
        if i == 3:
            continue
        print(i, end=' ')
    else:
        if i == 5:
            print("Loop completed successfully", end=' ')


def question10():
    x = 100
    while x > 0:
        print(x, end=' ')
        x = x // 2

if __name__ == "__main__":
    for i in range(10):
        func = globals()['question'+str(i+1)]
        func()
