import easy
import medium
import difficult

def do_easy():
    # "easy" problems
    easy.one()
    easy.two()
    easy.three()
    easy.four()
    easy.five(5)
    easy.six(50)
    easy.seven('circumlocution')
    easy.eight(29)
    easy.nine()
    easy.ten('circumlocution')

def do_medium():
    # "medium" problems
    medium.one([3, 7, 2, 9, 4])
    medium.two([10, 20, 30, 40])
    medium.three('racecar')
    medium.four(2, 2, 10)
    medium.five([3, 7, 2, 9, 4])
    medium.six(6)
    medium.seven(81)
    medium.eight()
    medium.nine('Hello, world! How are you?')
    medium.ten([1, 2, 3, 4], [3, 4, 5, 6])

def do_difficult():
    # "difficult" problems
    difficult.one(360)
    difficult.two(10)
    difficult.three('listen', 'silent')
    difficult.four(2, 2, 10)
    difficult.five([7, 1, 3, 9, 5])
    difficult.six(28)
    difficult.seven(12345)
    difficult.eight('The quick brown fox jumps')
    difficult.nine('The quick brown fox jumps over the lazy dog')
    difficult.ten()

def main():
    do_easy()
    do_medium()
    do_difficult()

main()
