# State Guesser

## Details
- difficulty: Easy
- category: Cryptography
- flags: flag{example}

## Description
Can you figure out which state I'm from? Decode this SHA-256 hash to reveal my home state:
`bd732730bd39834d83bf92a114960180d3bd4a6f1309307165e6f30ed9846fdd`

HINT #1: The answer is two words, all lower case. 

HINT #2: Bacon egg and cheese on a roll, please. SPK optional.

## Solution
The SHA-256 hash decrypts to "new york". Players can:
1. Use online SHA-256 crackers
2. Try common state names
3. Use hashcat with a state name wordlist
4. Write a script to test US state names

The final flag is: flag{new york}. When found, wrap in flag{} format. 