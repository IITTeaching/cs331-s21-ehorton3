import unittest
import sys
import math
from contextlib import contextmanager
from io import StringIO

#################################################################################
# TESTING OUTPUTS
#################################################################################
@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

#################################################################################
# EXERCISE 1
#################################################################################

# implement this function
def is_perfect(n):
    pass
    sum = 0
    for i in range(1,n):
        if (n%i) == 0:
            sum+=i
        if sum>n:
            return False
    if sum == n:
        return True
    return False
    


# (3 points)
def test1():
    tc = unittest.TestCase()
    for n in (6, 28, 496):
        tc.assertTrue(is_perfect(n), '{} should be perfect'.format(n))
    for n in (1, 2, 3, 4, 5, 10, 20):
        tc.assertFalse(is_perfect(n), '{} should not be perfect'.format(n))
    for n in range(30, 450):
        tc.assertFalse(is_perfect(n), '{} should not be perfect'.format(n))

#################################################################################
# EXERCISE 2
#################################################################################

# implement this function
def multiples_of_3_and_5(n):
    pass
    sum =0
    for i in range(0,n,3):
        if(i%5 !=0):
            sum+=i
    for i in range(0,n,5):
        sum+=i
    return sum

#print(multiples_of_3_and_5(10))

# (3 points)
def test2():
    tc = unittest.TestCase()
    tc.assertEqual(multiples_of_3_and_5(10), 23)
    tc.assertEqual(multiples_of_3_and_5(500), 57918)
    tc.assertEqual(multiples_of_3_and_5(1000), 233168)

#################################################################################
# EXERCISE 3
#################################################################################
def integer_right_triangles(perim):
    pass
    goodTris =[]
    #iterate 
    for c in range (3, perim):
        a=3
        b=perim-c-a
        #iterate b
        for j in range(perim-c-3):
            tup = (a,b,c)
            if((a**2+b**2)==c**2):
                goodTris.append(tup)
            a+=1
            b-=1
            if(b<a):
                break
            #print(tup)
    return len(goodTris)
            
            
        
        

def test3():
    tc = unittest.TestCase()
    tc.assertEqual(integer_right_triangles(60), 2)
    tc.assertEqual(integer_right_triangles(100), 0)
    tc.assertEqual(integer_right_triangles(180), 3)

#################################################################################
# EXERCISE 4
#################################################################################

# implement this function
def gen_pattern(chars):
    if len(chars)==1:
        st =""
        st += chars
        print(st)
    else:
        final=[]
        finalStr= ""
        leng = len(chars)
        for i in range(leng):
            res=""
            dots = (leng*2)-2
            dots-=(i*2)
            #initial dots
            for j in range (dots):
                res +="."
            #chars for that line
            linechars =""
            for m in range(i+1):
                x=(len(chars)-1)-m
                linechars+=chars[x]
            #add the forward line chars-c,b--0,1==c,b,a,--0,1,2
            for a in (linechars):
                res+=a
                if(len(linechars)!=1):
                    res+="."
            #add the backward line chars- c--0==b,c--1,0
            for a in range(len(linechars)-2,-1,-1):
                res+=linechars[a]
                if(a != 0):
                    res+="."
            #after dots
            for j in range (dots):
                res +="."
            final.append(res)
        #create the final string from the pattern list
        for a in (final):
                finalStr+=a
                finalStr+="\n"
        for a in range(len(final)-2,-1,-1):
                finalStr+=final[a]
                finalStr+="\n"
        print(finalStr)

def test4():
    tc = unittest.TestCase()
    with captured_output() as (out,err):
           gen_pattern('@')
           tc.assertEqual(out.getvalue().strip(), '@')
    with captured_output() as (out,err):
        gen_pattern('@%')
        tc.assertEqual(out.getvalue().strip(),
        """
..%..
%.@.%
..%..
""".strip())
    with captured_output() as (out,err):
        gen_pattern('ABC')
        tc.assertEqual(out.getvalue().strip(),
        """
....C....
..C.B.C..
C.B.A.B.C
..C.B.C..
....C....
""".strip())
    with captured_output() as (out,err):
        gen_pattern('#####')
        tc.assertEqual(out.getvalue().strip(),
                             """
........#........
......#.#.#......
....#.#.#.#.#....
..#.#.#.#.#.#.#..
#.#.#.#.#.#.#.#.#
..#.#.#.#.#.#.#..
....#.#.#.#.#....
......#.#.#......
........#........
""".strip())
    with captured_output() as (out,err):
        gen_pattern('abcdefghijklmnop')
        tc.assertEqual(out.getvalue().strip(),
"""
..............................p..............................
............................p.o.p............................
..........................p.o.n.o.p..........................
........................p.o.n.m.n.o.p........................
......................p.o.n.m.l.m.n.o.p......................
....................p.o.n.m.l.k.l.m.n.o.p....................
..................p.o.n.m.l.k.j.k.l.m.n.o.p..................
................p.o.n.m.l.k.j.i.j.k.l.m.n.o.p................
..............p.o.n.m.l.k.j.i.h.i.j.k.l.m.n.o.p..............
............p.o.n.m.l.k.j.i.h.g.h.i.j.k.l.m.n.o.p............
..........p.o.n.m.l.k.j.i.h.g.f.g.h.i.j.k.l.m.n.o.p..........
........p.o.n.m.l.k.j.i.h.g.f.e.f.g.h.i.j.k.l.m.n.o.p........
......p.o.n.m.l.k.j.i.h.g.f.e.d.e.f.g.h.i.j.k.l.m.n.o.p......
....p.o.n.m.l.k.j.i.h.g.f.e.d.c.d.e.f.g.h.i.j.k.l.m.n.o.p....
..p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p..
p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p
..p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p..
....p.o.n.m.l.k.j.i.h.g.f.e.d.c.d.e.f.g.h.i.j.k.l.m.n.o.p....
......p.o.n.m.l.k.j.i.h.g.f.e.d.e.f.g.h.i.j.k.l.m.n.o.p......
........p.o.n.m.l.k.j.i.h.g.f.e.f.g.h.i.j.k.l.m.n.o.p........
..........p.o.n.m.l.k.j.i.h.g.f.g.h.i.j.k.l.m.n.o.p..........
............p.o.n.m.l.k.j.i.h.g.h.i.j.k.l.m.n.o.p............
..............p.o.n.m.l.k.j.i.h.i.j.k.l.m.n.o.p..............
................p.o.n.m.l.k.j.i.j.k.l.m.n.o.p................
..................p.o.n.m.l.k.j.k.l.m.n.o.p..................
....................p.o.n.m.l.k.l.m.n.o.p....................
......................p.o.n.m.l.m.n.o.p......................
........................p.o.n.m.n.o.p........................
..........................p.o.n.o.p..........................
............................p.o.p............................
..............................p..............................
""".strip()
)

#################################################################################
# RUN ALL TESTS
#################################################################################
def main():
    test1()
    test2()
    test3()
    test4()

if __name__ == '__main__':
    main()
