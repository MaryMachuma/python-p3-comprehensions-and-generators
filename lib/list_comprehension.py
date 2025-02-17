#!/usr/bin/env python3

def return_evens(num_list):
    # List comprehension to return even numbers
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    # List comprehension to add '!' to each sentence
    return [sentence + '!' for sentence in sentence_list]

# Example usage:
if __name__ == "__main__":
    print(return_evens([0, 1, 3, 5, 7, 8, 9]))  
    # Output: [0, 8]

    print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
    # Output: ["Hello!", "I'm doing great!", "Python is fun!"]
