# Odd\_AND\_Even

## Writeup:

This challenge is divided in two parts, First part is a PE .Net executable and the second is a standard c/c++ PE executable.

* Firstly we get a .Net PE executable and we are supposed to change the name of the executable, it uses a xor operation to check the name of executable with **"OddEven.exe"**, Once we give it correctly, the executable drops another executable by downlading it from net.

* The dropped executable is a standard C/C++ PE executable which takes two input, One from command line arguments and other using fgets.

* After going through the algorithm we can find out that the input given through command line is taken as the odd index characters of the flag and is compared the result of xoring of  **"f`c(I&amp;gt;fJZb5BrQZQL"** string with 3 integers repeatedly.

* The input that was taken from fgets is taken as the even characters of the flag and is compared with a result of xoring of **"'-gsM!T;:Q?S&amp;gt;9K0A2"** string with 3 integers repeatedly.

*  Once our input passes both the cases it is printed out as flag.

FLAG: **flag{0DD_4nD_3v3N_C4n_n3V3r_B3_T0geth3r}**

**Full Writeup** [Writeup](https://learnernevergiveup.wordpress.com/2018/10/29/bsidesctf-2108-odd_even/)
