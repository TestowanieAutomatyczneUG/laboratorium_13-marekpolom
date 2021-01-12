class FizzBuzz:
    def game(num):
        
        if not str(num).isnumeric():
            return "ValueError"

        if((num%15) == 0):
            return "FizzBuzz"
        elif((num%3) == 0):
            return "Fizz"
        elif((num%5) == 0):
            return "Buzz"
        else:
            return "None"