import random

def BinarySearch(arr, low, high, key):
    """
    Binary Search algorithm for finding an element in a sorted array
    Returns the index of the element if found, otherwise returns -1
    """
    if high >= low:
        mid = (high + low) // 2
        if (arr[mid] == key):
            return mid
        elif (arr[mid] > key):
            return BinarySearch(arr, low, mid - 1, key)
        else:
            return BinarySearch(arr, mid + 1, high, key)
    else:
        return -1

class GuessingGame:
    """
    A class that implements a guessing game using Binary Search
    """
    def __init__(self, num_numbers):
        """
        Initializes the GuessingGame object with a list of random numbers between 0 and 2000
        """
        self.numbers = sorted([random.randint(0, 2000) for _ in range(num_numbers)])

    def play(self):
        """
        Starts the guessing game
        """
        print("Welcome to the guessing game! I'm thinking of a number between 0 and 2000.")
        guess = int(input("What's your guess? "))
        index = BinarySearch(self.numbers, 0, len(self.numbers)-1, guess)
        if index == -1:
            # guess not found, find close number
            closest = min(self.numbers, key=lambda x: abs(x-guess))
            print(f"Sorry, {guess} is not in the list. The closest number is {closest}.")
        else:
            # guess found
            print("Congratulations, you found the number!")

if __name__ == '__main__':
    num_numbers = int(input("How many random numbers would you like in the list? "))
    game = GuessingGame(num_numbers)
    game.play()