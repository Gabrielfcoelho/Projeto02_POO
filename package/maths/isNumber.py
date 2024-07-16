class IsNumber:

    @staticmethod
    def isNumber(n):
        try:
            float(n)
        except ValueError:
            return False
        return True
    
    @staticmethod
    def turnInNumber(n):
        try:
            float(n)
        except ValueError:
            return TypeError
        return float(n)
    