def one(number):
    """
    Write a program that finds the prime factors of a given number using a for loop. A prime factor is a prime number that divides another number exactly, e.g. the prime factors of 12 are 2 and 3.
    """
    print('\ndifficult.one:')

    factors = []
    for i in range(2, number + 1):
        if number % i == 0:
            # i divides number, so check if i is prime
            is_prime = True
            for d in range(2, i):
                if i % d == 0:
                    is_prime = False
                    break
            if is_prime:
                factors.append(i)
    print('\t', f'the prime factors of {number} are {factors}')

def two(n):
    """
    Write a program that calculates the nth term of the Fibonacci sequence using a while loop.
    """
    print('\ndifficult.two:')

    second_to_last = 0
    last = 1
    count = 0
    while count < n:
        total = second_to_last + last
        second_to_last = last
        last = total
        count += 1
    print('\t', f'term number {n} of the Fibonacci sequence is {second_to_last}')

def three(first, second):
    """
    Write a program that checks if a given string is an anagram using a for loop. Two strings are anagrams if they use the same letters.
    """
    print('\ndifficult.three:')

    word1 = first.replace(' ', '').lower()
    word2 = second.replace(' ', '').lower()

    is_anagram = True
    if len(word1) != len(word2):
        is_anagram = False
    else:
        for letter in word1:
            if word1.count(letter) != word2.count(letter):
                is_anagram = False
                break

    if is_anagram:
        print('\t', f'"{first}" and "{second}" are anagrams')
    else:
        print('\t', f'"{first}" and "{second}" are not anagrams')

def four(start, difference, n):
    """
    Write a program that prints the first n terms of the arithmetic sequence using a while loop. Each term after the first is found by adding the common difference, e.g. 2, 4, 6, 8, 10, ... where the common difference is 2.
    """
    print('\ndifficult.four:')

    term = start
    count = 0
    while count < n:
        print('\t', term)
        term = term + difference
        count += 1

def five(numbers):
    """
    Write a program that finds the median of a given list of numbers using a for loop. The median is the middle value when the numbers are sorted. If there is an even number of values, the median is the average of the two middle values.
    """
    print('\ndifficult.five:')

    # make a copy of the list so we don't change the original
    sorted_numbers = []
    for number in numbers:
        sorted_numbers.append(number)

    # sort the copy using bubble sort
    for i in range(len(sorted_numbers)):
        for j in range(len(sorted_numbers) - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                temp = sorted_numbers[j]
                sorted_numbers[j] = sorted_numbers[j + 1]
                sorted_numbers[j + 1] = temp

    middle = len(sorted_numbers) // 2
    if len(sorted_numbers) % 2 == 1:
        median = sorted_numbers[middle]
    else:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    print('\t', f'the median of {numbers} is {median}')

def six(number):
    """
    Write a program that checks if a given number is a perfect number using a while loop. A perfect number equals the sum of its divisors, not counting itself, e.g. 6 = 1 + 2 + 3.
    """
    print('\ndifficult.six:')

    total = 0
    divisor = 1
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1

    if total == number:
        print('\t', f'{number} is a perfect number')
    else:
        print('\t', f'{number} is not a perfect number')

def seven(number):
    """
    Write a program that prints the sum of all digits in a given number using a for loop. For example, the sum of the digits in 12345 is 1 + 2 + 3 + 4 + 5 = 15.
    """
    print('\ndifficult.seven:')

    total = 0
    for digit in str(number):
        total += int(digit)
    print('\t', f'the sum of the digits in {number} is {total}')

def eight(sentence):
    """
    Write a program that finds the longest word in a given sentence using a while loop.
    """
    print('\ndifficult.eight:')

    words = sentence.split()
    longest = ''
    i = 0
    while i < len(words):
        if len(words[i]) > len(longest):
            longest = words[i]
        i += 1
    print('\t', f'the longest word in "{sentence}" is "{longest}"')

def nine(sentence):
    """
    Write a program that checks if a given string is a pangram using a for loop. A pangram is a sentence that contains every letter of the alphabet at least once, e.g. The quick brown fox jumps over the lazy dog.
    """
    print('\ndifficult.nine:')

    sentence_lower = sentence.lower()
    is_pangram = True
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in sentence_lower:
            is_pangram = False
            break

    if is_pangram:
        print('\t', f'"{sentence}" is a pangram')
    else:
        print('\t', f'"{sentence}" is not a pangram')

def ten():
    """
    Write a program that prints the prime numbers between 1 and 1000 using a while loop.
    """
    print('\ndifficult.ten:')

    primes = []
    number = 2
    while number <= 1000:
        # check if number is prime
        is_prime = True
        divisor = number - 1
        while divisor > 1:
            if number % divisor == 0:
                is_prime = False
                break
            divisor -= 1
        if is_prime:
            primes.append(number)
        number += 1
    print('\t', primes)
