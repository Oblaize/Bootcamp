def fizz_buzz(number):
    if isinstance(number, int) or isinstance(number, float):
        if number <= 0:
            return "Number must be greater than zero"

        elif number % 3 == 0 and number % 5 == 0:
            return 'FizzBuzz'

        elif number % 5 == 0:
            return 'Buzz'

        elif number % 3 == 0:
            return 'Fizz'


        else:
            return number
    else:
        raise TypeError