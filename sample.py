def FizzBuzz(num):
    ret_str = ""
    if num % 3 == 0:
        ret_str += "Fizz"
    if num % 5 == 0:
        ret_str += "Buzz"
    if ret_str == "":
        return num
    else:
        return ret_str