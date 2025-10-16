class MathUtils:
    def add(self,a,b):
        return a + b
    
    def divide(self,a , b):
        if b == 0:
            raise ZeroDivisionError("can divide on zero")
        return a /b
    def is_even(self,a):
        return a % 2 == 0
    
    