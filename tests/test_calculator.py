from main import Calculator

class TestCalculator:
    def test_sum(self):
        assert Calculator.static_eval('14 + 3 + 9') == 26
        assert Calculator.static_eval('144 + 56') == 200
        assert Calculator.static_eval('7.7 + 2.3') == 10

    def test_negative_sum(self):
        assert Calculator.static_eval('-2 + 7 + 3') == 8

    def test_substraction(self):
        assert Calculator.static_eval('-5 - 5') == -10
        assert Calculator.static_eval('20 - 17') == 3

    def test_multiply(self):
        assert Calculator.static_eval('3 * 3') == 9
        assert Calculator.static_eval('-8 * 10') == -80

    def test_division(self):
        assert Calculator.static_eval('15 / 3') == 5
        assert Calculator.static_eval('-10 / 2') == -5

    def test_pow(self):
        assert Calculator.static_eval('3 ** 3') == 27
        assert Calculator.static_eval('10 ** 10') == 10000000000

    def test_expressions(self):
        assert Calculator.static_eval('^|-16 * (2+10)%2 + 14%(2 + a) - b|^', {
            'a': 5,
            'b': 4
        }) == -4.0
