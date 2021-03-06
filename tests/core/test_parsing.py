import unittest
import operator
import os
from STLInspector.core.temporallogic import *
from STLInspector.core.parsing import *


class TestPARSER(unittest.TestCase):
    def test_simple_ltl(self):
        f = open('tmpfile.txt', 'w')
        f.write('a')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AP("a"))
        f = open('tmpfile.txt', 'w')
        f.write('!a')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), NOT(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('!(a)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), NOT(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('! a')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), NOT(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('! (a)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), NOT(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('N a')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), NEXT(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('N (a)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), NEXT(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('o a')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), NEXT(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('o (a)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), NEXT(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('F a')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), FINALLY(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('F (a)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), FINALLY(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('<> a')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), FINALLY(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('<> (a)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), FINALLY(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('G a')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), GLOBALLY(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('G (a)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), GLOBALLY(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('[] a')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), GLOBALLY(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('[] (a)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), GLOBALLY(AP("a")))
        f = open('tmpfile.txt', 'w')
        f.write('a&b')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('a & b')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(a)&(b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(a) & (b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('a|b')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), OR(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('a | b')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), OR(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(a)|(b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), OR(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(a) | (b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), OR(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('a->b')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), IMPLIES(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('a -> b')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), IMPLIES(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(a)->(b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), IMPLIES(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(a) -> (b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), IMPLIES(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('a U b')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(a)U(b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(a) U (b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('a R b')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(a)R(b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(AP("a"), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(a) R (b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(AP("a"), AP("b")))

        if os.path.isfile('tmp'):
            os.remove('tmp')
        if os.path.isfile('tmpfile.txt'):
            os.remove('tmpfile.txt')

    def test_simple_stl(self):
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) >= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AP(None, (1, 2, 3), operator.ge, 42., ('x', 'y', 'z')))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) < 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AP(None, (1, 2, 3), operator.lt, 42., ('x', 'y', 'z')))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) > 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AP(None, (1, 2, 3), operator.gt, 42., ('x', 'y', 'z')))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) != 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AP(None, (1, 2, 3), operator.ne, 42., ('x', 'y', 'z')))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2)^T (x, y) <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AP(None, (1, 2), operator.le, 42., ('x', 'y')))
        f = open('tmpfile.txt', 'w')
        f.write('3x <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AP(None, [3], operator.le, 42., ['x']))
        f = open('tmpfile.txt', 'w')
        f.write(' 42y!=42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AP(None, [42], operator.ne, 42., ['y']))
        f = open('tmpfile.txt', 'w')
        f.write('y >= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AP(None, None, operator.ge, 42., ['y']))
        f = open('tmpfile.txt', 'w')
        f.write('!(1,2,3)^T (x, y, z) != 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), NOT(AP(None, (1, 2, 3), operator.ne, 42., ('x', 'y', 'z'))))
        f = open('tmpfile.txt', 'w')
        f.write('! 3x <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), NOT(AP(None, [3], operator.le, 42., ['x'])))
        f = open('tmpfile.txt', 'w')
        f.write('!(y >= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), NOT(AP(None, None, operator.ge, 42., ['y'])))
        f = open('tmpfile.txt', 'w')
        f.write('N[42] (1,2,3)^T (x, y, z) <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         NEXT(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 42))
        f = open('tmpfile.txt', 'w')
        f.write('N[42] ((1,2,3)^T (x, y, z) <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         NEXT(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 42))
        f = open('tmpfile.txt', 'w')
        f.write('o[42] (1,2,3)^T (x, y, z) <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         NEXT(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 42))
        f = open('tmpfile.txt', 'w')
        f.write('o[42] ((1,2,3)^T (x, y, z) <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         NEXT(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 42))
        f = open('tmpfile.txt', 'w')
        f.write('F[24, 42] (1,2,3)^T (x, y, z) <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         FINALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('F[24,42] ((1,2,3)^T (x, y, z) <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         FINALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('<>[24, 42] (1,2,3)^T (x, y, z) <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         FINALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('<>[24,42] ((1,2,3)^T (x, y, z) <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         FINALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('G[24, 42] (1,2,3)^T (x, y, z) <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         GLOBALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('G[24,42] ((1,2,3)^T (x, y, z) <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         GLOBALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('[][24, 42] (1,2,3)^T (x, y, z) <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         GLOBALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('[][24,42] ((1,2,3)^T (x, y, z) <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         GLOBALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42&(1,2)^T (x, y) <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                               AP(None, (1, 2), operator.le, 42., ('x', 'y'))))
        f = open('tmpfile.txt', 'w')
        f.write('3x <= 42 & y >= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         AND(AP(None, [3], operator.le, 42., ['x']), AP(None, None, operator.ge, 42., ['y'])))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42|(1,2)^T (x, y) <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), OR(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                              AP(None, (1, 2), operator.le, 42., ('x', 'y'))))
        f = open('tmpfile.txt', 'w')
        f.write('3x <= 42 | y >= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         OR(AP(None, [3], operator.le, 42., ['x']), AP(None, None, operator.ge, 42., ['y'])))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42->(1,2)^T (x, y) <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         IMPLIES(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                 AP(None, (1, 2), operator.le, 42., ('x', 'y'))))
        f = open('tmpfile.txt', 'w')
        f.write('3x <= 42 -> y >= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         IMPLIES(AP(None, [3], operator.le, 42., ['x']), AP(None, None, operator.ge, 42., ['y'])))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) <= 42 U[24, 42] 42y!=42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')),
                                                                 AP(None, [42], operator.ne, 42., ['y']), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('((1,2,3)^T (x, y, z) <= 42)U[24,42](42y!=42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')),
                                                                 AP(None, [42], operator.ne, 42., ['y']), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('((1,2,3)^T (x, y, z) <= 42) U[24, 42] (42y!=42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')),
                                                                 AP(None, [42], operator.ne, 42., ['y']), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) <= 42 R[24, 42] 42y!=42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         RELEASE(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')),
                                 AP(None, [42], operator.ne, 42., ['y']), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('((1,2,3)^T (x, y, z) <= 42)R[24,42](42y!=42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         RELEASE(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')),
                                 AP(None, [42], operator.ne, 42., ['y']), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('((1,2,3)^T (x, y, z) <= 42) R[24, 42] (42y!=42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         RELEASE(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')),
                                 AP(None, [42], operator.ne, 42., ['y']), 24, 42))

        if os.path.isfile('tmp'):
            os.remove('tmp')
        if os.path.isfile('tmpfile.txt'):
            os.remove('tmpfile.txt')

    def test_nested_ltl(self):
        f = open('tmpfile.txt', 'w')
        f.write('a & b & c')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(AP("a"), AND(AP("b"), AP("c"))))
        f = open('tmpfile.txt', 'w')
        f.write('a | b | c')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), OR(AP("a"), OR(AP("b"), AP("c"))))
        f = open('tmpfile.txt', 'w')
        f.write('a & (b | c)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(AP("a"), OR(AP("b"), AP("c"))))
        f = open('tmpfile.txt', 'w')
        f.write('(a | b) & c')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(OR(AP("a"), AP("b")), AP("c")))
        f = open('tmpfile.txt', 'w')
        f.write('a & !b & c')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(AP("a"), AND(NOT(AP("b")), AP("c"))))
        f = open('tmpfile.txt', 'w')
        f.write('(!(a | b)) & c')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(NOT(OR(AP("a"), AP("b"))), AP("c")))
        f = open('tmpfile.txt', 'w')
        f.write('a & !(N b) & c')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(AP("a"), AND(NOT(NEXT(AP("b"))), AP("c"))))
        f = open('tmpfile.txt', 'w')
        f.write('a U (F b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(AP("a"), FINALLY(AP("b"))))
        f = open('tmpfile.txt', 'w')
        f.write('a U (G b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(AP("a"), GLOBALLY(AP("b"))))
        f = open('tmpfile.txt', 'w')
        f.write('a U (N b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(AP("a"), NEXT(AP("b"))))
        f = open('tmpfile.txt', 'w')
        f.write('(F a) U b')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(FINALLY(AP("a")), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(G a) U b')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(GLOBALLY(AP("a")), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(N a) U b')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(NEXT(AP("a")), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(N a) U (F b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(NEXT(AP("a")), FINALLY(AP("b"))))
        f = open('tmpfile.txt', 'w')
        f.write('(G a) U (F b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(GLOBALLY(AP("a")), FINALLY(AP("b"))))
        f = open('tmpfile.txt', 'w')
        f.write('(F a) U (b U c)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(FINALLY(AP("a")), UNTIL(AP("b"), AP("c"))))
        f = open('tmpfile.txt', 'w')
        f.write('(b U c) U (F a)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(UNTIL(AP("b"), AP("c")), FINALLY(AP("a"))))
        f = open('tmpfile.txt', 'w')
        f.write('(x U y) U (b U c)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(UNTIL(AP("x"), AP("y")), UNTIL(AP("b"), AP("c"))))
        f = open('tmpfile.txt', 'w')
        f.write('a R (F b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(AP("a"), FINALLY(AP("b"))))
        f = open('tmpfile.txt', 'w')
        f.write('a R (G b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(AP("a"), GLOBALLY(AP("b"))))
        f = open('tmpfile.txt', 'w')
        f.write('a R (N b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(AP("a"), NEXT(AP("b"))))
        f = open('tmpfile.txt', 'w')
        f.write('(F a) R b')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(FINALLY(AP("a")), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(G a) R b')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(GLOBALLY(AP("a")), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(N a) R b')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(NEXT(AP("a")), AP("b")))
        f = open('tmpfile.txt', 'w')
        f.write('(N a) R (F b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(NEXT(AP("a")), FINALLY(AP("b"))))
        f = open('tmpfile.txt', 'w')
        f.write('(G a) R (F b)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(GLOBALLY(AP("a")), FINALLY(AP("b"))))
        f = open('tmpfile.txt', 'w')
        f.write('(F a) R (b R c)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(FINALLY(AP("a")), RELEASE(AP("b"), AP("c"))))
        f = open('tmpfile.txt', 'w')
        f.write('(b R c) R (F a)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(RELEASE(AP("b"), AP("c")), FINALLY(AP("a"))))
        f = open('tmpfile.txt', 'w')
        f.write('(x R y) R (b R c)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         RELEASE(RELEASE(AP("x"), AP("y")), RELEASE(AP("b"), AP("c"))))
        f = open('tmpfile.txt', 'w')
        f.write('(x R y) U (b U c)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(RELEASE(AP("x"), AP("y")), UNTIL(AP("b"), AP("c"))))
        f = open('tmpfile.txt', 'w')
        f.write('(x U y) R (b R c)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(UNTIL(AP("x"), AP("y")), RELEASE(AP("b"), AP("c"))))
        f = open('tmpfile.txt', 'w')
        f.write('(x U y) R (b U c)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(UNTIL(AP("x"), AP("y")), UNTIL(AP("b"), AP("c"))))

        if os.path.isfile('tmp'):
            os.remove('tmp')
        if os.path.isfile('tmpfile.txt'):
            os.remove('tmpfile.txt')

    def test_nested_stl(self):
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42 & 3x <= 42 & y >= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                               AND(AP(None, [3], operator.le, 42., ['x']),
                                                                   AP(None, None, operator.ge, 42., ['y']))))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42 | 3x <= 42 | y >= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), OR(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                              OR(AP(None, [3], operator.le, 42., ['x']),
                                                                 AP(None, None, operator.ge, 42., ['y']))))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42 & (3x <= 42 | y >= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                               OR(AP(None, [3], operator.le, 42., ['x']),
                                                                  AP(None, None, operator.ge, 42., ['y']))))
        f = open('tmpfile.txt', 'w')
        f.write('((1,2,3)^T (x, y, z) == 42 | 3x <= 42) & y >= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(
            OR(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), AP(None, [3], operator.le, 42., ['x'])),
            AP(None, None, operator.ge, 42., ['y'])))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42 & !3x <= 42 & y >= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                               AND(NOT(AP(None, [3], operator.le, 42., ['x'])),
                                                                   AP(None, None, operator.ge, 42., ['y']))))
        f = open('tmpfile.txt', 'w')
        f.write('(!((1,2,3)^T (x, y, z) == 42 | 3x <= 42)) & y >= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(
            NOT(OR(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), AP(None, [3], operator.le, 42., ['x']))),
            AP(None, None, operator.ge, 42., ['y'])))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42 & !(N[11] 3x <= 42) & y >= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), AND(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                               AND(NOT(
                                                                   NEXT(AP(None, [3], operator.le, 42., ['x']), 11)),
                                                                   AP(None, None, operator.ge, 42., ['y']))))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42 U[24, 42] (F[3,11] 3x <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                                 FINALLY(AP(None, [3], operator.le, 42., ['x']), 3, 11),
                                                                 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42 U[24, 42] (G[3,11] 3x <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                                 GLOBALLY(AP(None, [3], operator.le, 42., ['x']), 3,
                                                                          11), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42 U[24, 42] (N[11] 3x <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                                 NEXT(AP(None, [3], operator.le, 42., ['x']), 11), 24,
                                                                 42))
        f = open('tmpfile.txt', 'w')
        f.write('(F[3,11] (1,2,3)^T (x, y, z) == 42) U[24, 42] 3x <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         UNTIL(FINALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                               AP(None, [3], operator.le, 42., ['x']), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('(G[3,11] (1,2,3)^T (x, y, z) == 42) U[24, 42] 3x <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         UNTIL(GLOBALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                               AP(None, [3], operator.le, 42., ['x']), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('(N[11] (1,2,3)^T (x, y, z) == 42) U[24, 42] 3x <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         UNTIL(NEXT(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 11),
                               AP(None, [3], operator.le, 42., ['x']), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('(N[11] (1,2,3)^T (x, y, z) == 42) U[24, 42] (F[3,11] 3x <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         UNTIL(NEXT(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 11),
                               FINALLY(AP(None, [3], operator.le, 42., ['x']), 3, 11), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('(G[3,11] (1,2,3)^T (x, y, z) == 42) U[24, 42] (F[3,11] 3x <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         UNTIL(GLOBALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                               FINALLY(AP(None, [3], operator.le, 42., ['x']), 3, 11), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('(F[3,11] (1,2,3)^T (x, y, z) == 42) U[24, 42] (3x <= 42 U[24, 42] y >= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         UNTIL(FINALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                               UNTIL(AP(None, [3], operator.le, 42., ['x']), AP(None, None, operator.ge, 42., ['y']),
                                     24, 42), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('(3x <= 42 U[24, 42] y >= 42) U[24, 42] (F[3,11] (1,2,3)^T (x, y, z) == 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(
            UNTIL(AP(None, [3], operator.le, 42., ['x']), AP(None, None, operator.ge, 42., ['y']), 24, 42),
            FINALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write(
            '((1,2,3)^T (x, y, z) == 42 U[24, 42] (1,2,3)^T (x, y, z) != 42) U[24, 42] (3x <= 42 U[24, 42] y >= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(
            UNTIL(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                  AP(None, (1, 2, 3), operator.ne, 42., ('x', 'y', 'z')), 24, 42),
            UNTIL(AP(None, [3], operator.le, 42., ['x']), AP(None, None, operator.ge, 42., ['y']), 24, 42), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42 R[7,9] (F[3,11] 3x <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         RELEASE(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                 FINALLY(AP(None, [3], operator.le, 42., ['x']), 3, 11), 7, 9))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42 R[7,9] (G[3,11] 3x <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         RELEASE(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                 GLOBALLY(AP(None, [3], operator.le, 42., ['x']), 3, 11), 7, 9))
        f = open('tmpfile.txt', 'w')
        f.write('(1,2,3)^T (x, y, z) == 42 R[7,9] (N[11] 3x <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         RELEASE(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                 NEXT(AP(None, [3], operator.le, 42., ['x']), 11), 7, 9))
        f = open('tmpfile.txt', 'w')
        f.write('(F[3, 11] (1,2,3)^T (x, y, z) == 42) R[7,9] 3x <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         RELEASE(FINALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                                 AP(None, [3], operator.le, 42., ['x']), 7, 9))
        f = open('tmpfile.txt', 'w')
        f.write('(G[3,11] (1,2,3)^T (x, y, z) == 42) R[7,9] 3x <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         RELEASE(GLOBALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                                 AP(None, [3], operator.le, 42., ['x']), 7, 9))
        f = open('tmpfile.txt', 'w')
        f.write('(N[11] (1,2,3)^T (x, y, z) == 42) R[7,9] 3x <= 42')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         RELEASE(NEXT(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 11),
                                 AP(None, [3], operator.le, 42., ['x']), 7, 9))
        f = open('tmpfile.txt', 'w')
        f.write('(N[11] (1,2,3)^T (x, y, z) == 42) R[7,9] (F[3,11] 3x <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         RELEASE(NEXT(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 11),
                                 FINALLY(AP(None, [3], operator.le, 42., ['x']), 3, 11), 7, 9))
        f = open('tmpfile.txt', 'w')
        f.write('(G[3,11] (1,2,3)^T (x, y, z) == 42) R[7,9] (F[3,11] 3x <= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         RELEASE(GLOBALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                                 FINALLY(AP(None, [3], operator.le, 42., ['x']), 3, 11), 7, 9))
        f = open('tmpfile.txt', 'w')
        f.write('(F[3,11] (1,2,3)^T (x, y, z) == 42) R[7,9] (3x <= 42 R[7,9] y >= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'),
                         RELEASE(FINALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                                 RELEASE(AP(None, [3], operator.le, 42., ['x']),
                                         AP(None, None, operator.ge, 42., ['y']), 7, 9), 7, 9))
        f = open('tmpfile.txt', 'w')
        f.write('(3x <= 42 R[7,9] y >= 42) R[7,9] (F[3,11] (1,2,3)^T (x, y, z) == 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(
            RELEASE(AP(None, [3], operator.le, 42., ['x']), AP(None, None, operator.ge, 42., ['y']), 7, 9),
            FINALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11), 7, 9))
        f = open('tmpfile.txt', 'w')
        f.write('((1,2,3)^T (x, y, z) == 42 R[7,9] (1,2,3)^T (x, y, z) != 42) R[7,9] (3x <= 42 R[7,9] y >= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(
            RELEASE(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                    AP(None, (1, 2, 3), operator.ne, 42., ('x', 'y', 'z')), 7, 9),
            RELEASE(AP(None, [3], operator.le, 42., ['x']), AP(None, None, operator.ge, 42., ['y']), 7, 9), 7, 9))
        f = open('tmpfile.txt', 'w')
        f.write('((1,2,3)^T (x, y, z) == 42 R[7,9] (1,2,3)^T (x, y, z) != 42) U[24, 42] (3x <= 42 U[24, 42] y >= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), UNTIL(
            RELEASE(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                    AP(None, (1, 2, 3), operator.ne, 42., ('x', 'y', 'z')), 7, 9),
            UNTIL(AP(None, [3], operator.le, 42., ['x']), AP(None, None, operator.ge, 42., ['y']), 24, 42), 24, 42))
        f = open('tmpfile.txt', 'w')
        f.write('((1,2,3)^T (x, y, z) == 42 U[24, 42] (1,2,3)^T (x, y, z) != 42) R[7,9] (3x <= 42 R[7,9] y >= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(
            UNTIL(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                  AP(None, (1, 2, 3), operator.ne, 42., ('x', 'y', 'z')), 24, 42),
            RELEASE(AP(None, [3], operator.le, 42., ['x']), AP(None, None, operator.ge, 42., ['y']), 7, 9), 7, 9))
        f = open('tmpfile.txt', 'w')
        f.write('((1,2,3)^T (x, y, z) == 42 U[24, 42] (1,2,3)^T (x, y, z) != 42) R[7,9] (3x <= 42 U[24, 42] y >= 42)')
        f.close()
        self.assertEqual(parse_from_path('tmpfile.txt'), RELEASE(
            UNTIL(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                  AP(None, (1, 2, 3), operator.ne, 42., ('x', 'y', 'z')), 24, 42),
            UNTIL(AP(None, [3], operator.le, 42., ['x']), AP(None, None, operator.ge, 42., ['y']), 24, 42), 7, 9))

        if os.path.isfile('tmp'):
            os.remove('tmp')
        if os.path.isfile('tmpfile.txt'):
            os.remove('tmpfile.txt')


    def test_direct_parse(self):
        self.assertEqual(parse('(1,2,3)^T (x, y, z) <= 42'), AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')))
        self.assertEqual(parse('(1,2,3)^T (x, y, z) >= 42'), AP(None, (1, 2, 3), operator.ge, 42., ('x', 'y', 'z')))
        self.assertEqual(parse('(1,2,3)^T (x, y, z) < 42'), AP(None, (1, 2, 3), operator.lt, 42., ('x', 'y', 'z')))
        self.assertEqual(parse('G a'), GLOBALLY(AP("a")))
        self.assertEqual(parse('F a'), FINALLY(AP("a")))
        self.assertEqual(parse('N a'), NEXT(AP("a")))
        self.assertEqual(parse('G (a)'), GLOBALLY(AP("a")))
        self.assertEqual(parse('a&b'), AND(AP("a"), AP("b")))
        self.assertEqual(parse('(a) & (b)'), AND(AP("a"), AP("b")))
        self.assertEqual(parse('a | b'), OR(AP("a"), AP("b")))
        self.assertEqual(parse('(a) | (b)'), OR(AP("a"), AP("b")))
        self.assertEqual(parse('a->b'), IMPLIES(AP("a"), AP("b")))
        self.assertEqual(parse('(a) -> (b)'), IMPLIES(AP("a"), AP("b")))
        self.assertEqual(parse('a U b'), UNTIL(AP("a"), AP("b")))
        self.assertEqual(parse('(a)U(b)'), UNTIL(AP("a"), AP("b")))
        self.assertEqual(parse('a R b'), RELEASE(AP("a"), AP("b")))
        self.assertEqual(parse('(a) R (b)'), RELEASE(AP("a"), AP("b")))

