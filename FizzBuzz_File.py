import numpy as np
def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)
    result = nums.astype(object)
    fizz = (nums % 3 == 0)
    buzz = (nums % 5 == 0)
    result[fizz] = "fizz"
    result[buzz] = "buzz"
    result[fizz & buzz] = "fizzbuzz"

    return(result)
  
