def one(numbers):
    """
    Write a program that finds the largest element in a given list using a for loop.
    """
    print('\nmedium.one:')

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    print('\t', f'the largest element in {numbers} is {largest}')

def two(numbers):
    """
    Write a program that calculates the average of a list of numbers using a while loop. You are not allowed to use the built-in sum() function.
    """
    print('\nmedium.two:')

    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    average = total / len(numbers)
    print('\t', f'the average of {numbers} is {average}')

def three(text):
    """
    Write a program that checks if a given string is a palindrome using a for loop. A palindrome reads the same forwards and backwards, e.g. radar, level, mom, noon, civic, racecar, ...
    """
    print('\nmedium.three:')

    # build the string backwards by adding each letter to the front
    backwards = ''
    for letter in text:
        backwards = letter + backwards

    if text == backwards:
        print('\t', f'"{text}" is a palindrome')
    else:
        print('\t', f'"{text}" is not a palindrome')

def four(start, ratio, n):
    """
    Write a program that prints the first n terms of the geometric sequence using a while loop. Each term after the first is found by multiplying the previous term by the common ratio, e.g. 2, 4, 8, 16, 32, ... where the common ratio is 2.
    """
    print('\nmedium.four:')

    term = start
    count = 0
    while count < n:
        print('\t', term)
        term = term * ratio
        count += 1

def five(numbers):
    """
    Write a program that finds the second largest element in a given list using a for loop.
    """
    print('\nmedium.five:')

    # first find the largest
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

    # then find the largest of the numbers that are not the largest
    second = numbers[0]
    found = False
    for number in numbers:
        if number != largest:
            if found == False or number > second:
                second = number
                found = True
    print('\t', f'the second largest element in {numbers} is {second}')

def six(number):
    """
    Write a program that calculates the factorial of a given number using a while loop.
    """
    print('\nmedium.six:')

    product = 1
    i = 1
    while i <= number:
        product = product * i
        i += 1
    print('\t', f'{number} factorial = {product}')

def seven(number):
    """
    Write a program that checks if a given number is a perfect square using a for loop. A perfect square is a number equal to some integer times itself, e.g. 1, 4, 9, 16, 25, ...
    """
    print('\nmedium.seven:')

    is_perfect_square = False
    for i in range(number + 1):
        if i * i == number:
            is_perfect_square = True
            break

    if is_perfect_square:
        print('\t', f'{number} is a perfect square')
    else:
        print('\t', f'{number} is not a perfect square')

def eight():
    """
    Write a program that prints the sum of all prime numbers between 1 and 100 using a while loop.
    """
    print('\nmedium.eight:')

    total = 0
    number = 2
    while number <= 100:
        # check if number is prime
        is_prime = True
        divisor = number - 1
        while divisor > 1:
            if number % divisor == 0:
                is_prime = False
                break
            divisor -= 1
        if is_prime:
            total += number
        number += 1
    print('\t', f'the sum of all primes between 1 and 100 is {total}')

def nine(sentence):
    """
    Write a program that counts the number of words in a given sentence using a for loop. Words can be separated by spaces.
    """
    print('\nmedium.nine:')

    count = 0
    for word in sentence.split():
        count += 1
    print('\t', f'the number of words in "{sentence}" is {count}')

def ten(list_a, list_b):
    """
    Write a program that prints the common elements between two lists using a while loop.
    """
    print('\nmedium.ten:')

    common = []
    i = 0
    while i < len(list_a):
        if list_a[i] in list_b:
            common.append(list_a[i])
        i += 1
    print('\t', f'the common elements between {list_a} and {list_b} are {common}')
