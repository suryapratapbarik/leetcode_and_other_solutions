"""
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for
the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1,n+1):
            by3, by5 = False, False
            if i%3==0: by3 = True
            if i%5==0: by5 = True
            if by3 and by5:
                result.append("FizzBuzz")
            elif by5:
                result.append("Buzz")
            elif by3:
                result.append("Fizz")
            else:
                result.append(str(i))
        return result
    
print (Solution().fizzBuzz(15))
#['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']