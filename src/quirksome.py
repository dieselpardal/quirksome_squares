#!/usr/bin/python

class QuirkSome:

    def add_zeros(selfself,num,digit):
        a = digit - len(str(num))
        sub = ""
        if a>0:
            for seq in range(0,a):
                sub +="0"
        return sub + str(num)

    def found_square(self,a,b,s):
        return ( int(a) + int(b) ) ** 2 == int(s)

    def add_square(self,a,b,s):
        return "("+ a + "+" + b + ") **  2 = "+ s + "\n"

    def value(self,digit):
        if digit < 2:
            return ""
        str = ""
        separate = int(digit / 2)
        for seq in range(0,10 ** digit):
            s= self.add_zeros(seq,digit)
            a= s[:separate]
            b= s[-separate:]
            if self.found_square(a,b,s):
                str += self.add_square(a,b,s)
        return str

