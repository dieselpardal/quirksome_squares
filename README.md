Quirksome Squares
=================

The number 3025 has a remarkable quirk: if you split its decimal representation in two strings of equal
length (30 and 25) and square the sum of the numbers so obtained, you obtain the original number:
(30 + 25)2 = 3025

The problem is to determine all numbers with this property having a given even number of digits.
For example, 4-digit numbers run from 0000 to 9999. Note that leading zeroes should be taken into account. This means that 0001 which is equal to (00 + 01)2 is a quirksome number of 4 digits. The number of digits may be 2,4,6 or 8. Although maxint is only 32767 and numbers of eight digits are asked for, a well-versed programmer can keep his numbers in the range of the integers. However e ciency should be given a thought.
Input

The input of your program is a text le containing numbers of digits (taken from 2,4,6,8), each number on a line of its own.
Output

The output is a text le consisting of lines containing the quirksome numbers (ordered according to the input numbers and for each input number in increasing order).
Warning: Please note that the number of digits in the output is equal to the number in the corre- sponding input line : leading zeroes may not be suppressed.
Sample Input

2
Sample Output

00

01

81


#### Código de Fonte

   A listagem de código é em python. 
   
####Terminal - execute:

```sh
python quirksome.py 4
Square:
(00+00) **  2 = 0000
(00+01) **  2 = 0001
(20+25) **  2 = 2025
(30+25) **  2 = 3025
(98+01) **  2 = 9801
```


####Terminal - test:

```sh
python test/testquirksome.py
```