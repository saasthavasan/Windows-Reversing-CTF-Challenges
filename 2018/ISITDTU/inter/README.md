# Inter

## Mini-Writeup:

This challenge creates 2 thread 1 for named pipe and other to check the breakpoint in oppcode which is kind of an antidebuggig check.
There are 5 stages in the challenge and all the input is taken as integer(there was a lot of bruteforcing involved in this challenge):

* The first stage the program checks if the user input is equal to **0x1e1e1e1e ^ 0x672E6B41**.
* Second stage checks if the sum of user input is equal to 0x23 and divides the user input in loop and cheks the remainder with **[0x1f, 0x21, 0x0c, 0x04, 0x18, 0x1f]**

* Third stage checks if the user input is equal to (0xcafebabe ^ 0xa8cad9ef) - 0x21

* Fourth stage takes the md5 hash of the input and compares it with *"e861a6e17bd11a7cec8b6c8514728d2b"*

* Fifth stage cheks if the sum of all the numbers is 0x2b and the input is equal to **(0xcafacada ^ 0xfb94f39) - 45)**


## Input And Flag:
Input for stage 1: 2033218911
Input for stage 2: 1664380511
Input for stage 3: 1647600432
Input for stage 4: 1835360107
Input for stage 5: 829307169

FLAG: **ISITDTU{y0u_c4n_b4c0me_k1n9!}**
