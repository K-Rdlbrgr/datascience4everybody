# Start with some pseudo-code!
def fizzbuzz(n=100):
    # Looping through the range of the game
    for i in range(1, n+1):
        # If number is divisible by 3 and 5
        if i % 5 == 0 and i % 3 == 0:
            print('fizzbuzz')
        # If divisible by 3 but not 5
        elif i % 3 == 0:
            print('fizz')
        # If divisible by 5 but not 3
        elif i % 5 == 0:
            print('buzz')
        # If not divisible by either 3 nor 5
        else:
            print(i)


# Running the function
fizzbuzz()
