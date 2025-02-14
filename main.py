import random
from task3.py import decorator_1
from task1.py import kwargsAcceptFun
from task2.py import typeBasedTransformer

@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
        
@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i

if __name__ == "__main__":
    func()
    funx()
    func()
    funx()
    func()

    kwargsAcceptFun(name="John", age=25, profession="Engineer")

    transformed = typeBasedTransformer(
        num=31,
        text="Hello World",
        val=True,
        number_list=[1, 2, 3],
        letter_num={"a": 1, "b": 2}
    )
    print(transformed)