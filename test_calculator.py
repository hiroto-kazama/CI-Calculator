"""
Tests for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)

    def test_sub(sub):
        assert 5 == calculator.subtract(10, 5)

    def test_mutiply(self):
        assert 4 == calculator.multiply(2, 2)

    def test_division(self):
        assert 4 == calculator.division(8, 2)
