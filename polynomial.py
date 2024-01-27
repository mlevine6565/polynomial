class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self,x):
        return x

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    
    def evaluate(self,x):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self,x):
        return self.p1.evaluate(x) + self.p2.evaluate(x)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub) or isinstance(self.p1, Div):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub) or isinstance(self.p2, Div):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub) or isinstance(self.p2, Div):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self,x):
        return self.p1.evaluate(x) * self.p2.evaluate(x)
    
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)

    def evaluate(self,x):
        return self.p1.evaluate(x) - self.p2.evaluate(x)
class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Mul) or isinstance(self.p1, Sub):
            if isinstance(self.p2, Add) or isinstance(self.p2, Mul) or isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, Mul) or isinstance(self.p2, Sub):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)
    
    def evaluate(self,x):
        return self.p1.evaluate(x) / self.p2.evaluate(x)


poly = Sub(Div( Sub( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1))))), Mul(Div(X(),Int(3)),Int(2)))
print(poly)
print(poly.evaluate(2))
