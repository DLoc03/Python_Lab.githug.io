def TimUCLN(a, b):
        if a == 0 or b == 0:
            return a + b
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
    
