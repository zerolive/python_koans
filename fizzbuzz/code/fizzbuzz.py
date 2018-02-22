
class FizzBuzz():

  FIZZ_NUMBER = 3
  BUZZ_NUMBER = 5
  BUZZ = 'Buzz'
  FIZZ = 'Fizz'

  def __init__(self, number):
    self._number = number

  def evaluate(self):
    if self._is_fizzbuzz():
      return self.FIZZ + self.BUZZ

    if self._is_fizz():
      return self.FIZZ

    if self._is_buzz():
      return self.BUZZ

    return str(self._number)

  def _is_fizz(self):
    return (self._number % self.FIZZ_NUMBER == 0)

  def _is_buzz(self):
    return (self._number % self.BUZZ_NUMBER == 0)

  def _is_fizzbuzz(self):
    return self._is_buzz() and self._is_fizz()
