from code.fizzbuzz import FizzBuzz
import unittest

class TestFizzBuzz(unittest.TestCase):
  def test_evaluates_the_number_for_a_non_fizzbuzz_number(self):
    non_fizzbuzz_number = 1
    fizzbuzz = FizzBuzz(non_fizzbuzz_number)

    evaluation = fizzbuzz.evaluate()

    self.assertEqual(evaluation, str(non_fizzbuzz_number))

  def test_evaluates_fizz_for_a_fizz_number(self):
    fizz_number = 3
    fizzbuzz = FizzBuzz(fizz_number)

    evaluation = fizzbuzz.evaluate()

    self.assertEqual(evaluation, 'Fizz')

  def test_evaluates_buzz_for_a_buzz_number(self):
    buzz_number = 5
    fizzbuzz = FizzBuzz(buzz_number)

    evaluation = fizzbuzz.evaluate()

    self.assertEqual(evaluation, 'Buzz')

  def test_evaluates_buzz_for_a_fizzbuzz_number(self):
    fizzbuzz_number = 15
    fizzbuzz = FizzBuzz(fizzbuzz_number)

    evaluation = fizzbuzz.evaluate()

    self.assertEqual(evaluation, 'FizzBuzz')

if __name__ == '__main__':
  unittest.main()
