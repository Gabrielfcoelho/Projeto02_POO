class IsNumber:

    @staticmethod
    def isNumber(n):
        try:
            float(n)
        except ValueError:
            return False
        return True