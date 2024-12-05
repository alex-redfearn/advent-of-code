from unittest import TestCase
from corrupt_multiplication import CorruptMultiplication


class TestCorruptMultiplication(TestCase):

    def test_given_corrupt_multiplication_when_get_total_return_total(self):
        data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        
        assert CorruptMultiplication(data).multiply() == 48