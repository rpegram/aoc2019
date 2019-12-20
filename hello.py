from unittest import TestCase

def get_fuel2(mass):

    FuelInit = 0

    FuelAdd = (mass // 3) - 2

    while FuelAdd > 0:

        FuelInit = FuelInit + FuelAdd

        FuelAdd = (FuelAdd // 3) - 2

    return FuelInit

def get_fuel(mass):
    fuel = (mass // 3) - 2
    if fuel < 0:
        return 0
    return fuel + get_fuel(fuel)

def fib(n):
    return _fib(0, 1, n - 1)

def _fib(a, b, n):
    if n == 0:
        return a + b
    return _fib(b, a+b, n - 1)

    
class TestGetFuel(TestCase):
    def test_fib(self):
        self.assertEqual(
            fib(5),
            8
        )
        self.assertEqual(
            fib(6),
            13
        )
        self.assertEqual(
            fib(69),
            190392490709135
        )

    def test(self):
       
        self.assertEqual(
           
            get_fuel(12),
  
            2
        )

    def test2(self):
       
        self.assertEqual(
           
            get_fuel(14),
  
            2
        )

    def test3(self):
       
        self.assertEqual(
           
            get_fuel(1969),
  
            966
        )

def fuel_total(masses):

    FuelTotal = 0

    for i in masses:

        FuelTotal = FuelTotal + get_fuel(i)

    return(FuelTotal)

PuzzleInputMass = [131787,
    116597,
    71331,
    101986,
    56538,
    105039,
    119405,
    87762,
    113957,
    69613,
    63698,
    117674,
    72876,
    105026,
    83620,
    132592,
    137403,
    96832,
    58387,
    97609,
    50978,
    52896,
    145584,
    140832,
    74504,
    52998,
    64722,
    143334,
    89601,
    89326,
    85906,
    117840,
    91299,
    50593,
    74470,
    141591,
    61069,
    130479,
    69195,
    77411,
    106137,
    80954,
    117644,
    113063,
    127587,
    148770,
    71286,
    123430,
    133562,
    121053,
    64311,
    52818,
    148583,
    107511,
    92838,
    79724,
    122022,
    122602,
    50344,
    56938,
    102363,
    123140,
    105469,
    72773,
    96023,
    53669,
    70394,
    100930,
    55213,
    53756,
    62225,
    57172,
    56049,
    64661,
    112321,
    59872,
    111597,
    115958,
    105468,
    62111,
    72865,
    80323,
    103897,
    137687,
    70178,
    113314,
    122121,
    128654,
    136723,
    77279,104806,103491,92168,119263,128791,102237,86578,92728,104785,116658]



class TestFuelTotal(TestCase):

    def test(self):
       
        self.assertEqual(
           
            fuel_total([12]),
  
            2
        )
    
    def test1(self):
       
        self.assertEqual(
           
            fuel_total([12,14]),
  
            4
        )
    
    def test3(self):
       
        self.assertEqual(
           
            fuel_total([12,14,1969]),
  
            970
        )

    def test4(self):
       
        self.assertEqual(
           
            fuel_total(PuzzleInputMass),
  
            4757427
        )