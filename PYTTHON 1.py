#!/usr/bin/env python

import random
from threading import Timer

def main():
    """Start a colour guessing game."""
    print("Guess the music genre!")
    
    genre = [
        "Rock",
        "Pop music",
        "Electronic music",
        "Rhythm and blues",
        "Hip hop music",
        ]
                
    x = random.choice(genre)
    guess = None
    
    while x != guess:
        
        guess = str(input("Guess the genre "))
        
        if x == guess:
            print("Congratulations you got it right!")
            break
        else:
            print("Unfortunately you got the wrong answer. Please try again!")                       
    
main()