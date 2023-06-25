def __recur__factorial(n) :
    if n==1:
        return n
    else:
        return n*recur__factorial(n-1)
num=7
if num<0:
    print("sorry factorial dose not exit for negitive members:")
else:
    print("The factorial of",num "is", recur__factorial(num))
        
