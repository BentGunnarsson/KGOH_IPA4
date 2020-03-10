import sample

def test_return_number():
    assert sample.FizzBuzz(7) == 7

def test_return_fizz():
    assert sample.FizzBuzz(6) == "Fizz"

def test_return_buzz():
    assert sample.FizzBuzz(10) == "Buzz"