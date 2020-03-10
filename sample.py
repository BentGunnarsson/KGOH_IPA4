def FizzBuzz(num):
    ret_str = ""
    if num % 3 == 0:
        ret_str += "Fizz"
        return ret_str
    if num % 5 == 0:
        ret_str += "Buzz"
        return ret_str
    return num