import random
n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
def add(n1, n2):
    while n1 + n2 >=100:
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
    return n1 + n2
 
def sub(n1, n2):
    n1, n2 = max(n1, n2), min(n1, n2)
    return n1 - n2
 
def multi(n1, n2):
    while n1 * n2 >=100:  #控制积不超过100
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
    return n1 * n2
 
def divide(n1, n2):
    n1, n2 = max(n1, n2), min(n1, n2)
    return int(n1 / n2)
