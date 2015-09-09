#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

#f(a,b,c,d) = (a+b)*c-d
#f(a,b,c,d) = (a+b)*(c-d)

def calc2(s):

    """
    def f_add(a,b): return a+b
    def f_mul(a,b): return a*b
    def f_sub(a,b): return a-b
    """
    
    if s=='+':
        return lambda a,b:a+b
    elif s=='*':
        return lambda a,b:a*b
    elif s=='-':
        return lambda a,b:a-b       
    else:
        assert False, "error: operator not defined"




calc_dict={
    '+':lambda a,b:a+b,
    '*':lambda a,b:a*b,
    '-':lambda a,b:a-b,
}


if __name__ == '__main__':

    a,b,c,d = 1,2,3,4

    print calc2('-')(calc2('*')(calc2('+')(a,b),c),d)
    print calc2('*')(calc2('+')(a,b), calc2('-')(c,d))


    #f(a,b,c,d) = (a+b)*c-d
    operators = [(calc_dict['+'],[a,b]),(calc_dict['*'],[c]),(calc_dict['-'],[d])]


    for operator,num in operators:
        if len(num)==1:
            num1=result
            num2=num[0]
        else:
            num1=num[0]
            num2=num[1]
        result=operator(num1,num2)

    print result

