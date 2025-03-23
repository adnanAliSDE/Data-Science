"""
9. Given a character, check if it is a vowel or consonant.
Input: e
Output: Vowel
"""

char = input("Enter a character: ")

if char in {"a", "e", "i", "o", "u"}:
    print("Vowel")
else:
    print("Consonant")