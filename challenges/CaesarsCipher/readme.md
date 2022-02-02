# Caesar's Cipher Challenge

For each character in a string find the index and shift it by an integer using the characters string or list below.
```
characters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

encrypt(plaintext: str, key: int) -> str:
    """encrypt plain text by shifting the index of each character by the key"""

decrypt(ciphertext: str, key: int) -> str:
    """decrypt cipher text by shifting the index of each character by the key"""
```

### CHARACTERS LIST
| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
---
| a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z |
:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 | 51 |

### Examples
#### Encrypt
1.
     * Input: plaintext="Python", key=7
     * Output: "WFAovu"
     * Explanation: We shift the index of each character in "Python" by key and return the result.
___

2.
    * Input: plaintext="Caesars Cipher", key=21
    * Output: "XvzNvMNXDKCzM"

#### Decrypt
___
1.
   * Input: ciphertext="SoinomgtVEznut", key=6
   * Output: "Michigan Python"

### Bonus
Write a brute force decryption method.
```
bruteforce_decrypt(ciphertext: str) -> list[str]:
"""Brute force a cipher text"""
```
