class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [""] * n
        for i in range(n):
            if (i+1)%3 == 0 and (i+1)%5 == 0:
                answer[i] = "FizzBuzz"
            elif (i+1)%3 == 0:
                answer[i] = "Fizz"
            elif (i+1)%5 == 0:
                answer[i] = "Buzz"
            else:
                answer[i] = str((i+1))
        return answer




class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [] 
        for i in range(n):
            curr = ""
            if (i+1)%3 == 0:
                curr += "Fizz"
            if (i+1)%5 == 0:
                curr+="Buzz"
            if not curr:
                curr = str(i+1)
            answer.append(curr)
        return answer