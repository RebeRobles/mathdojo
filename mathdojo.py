from math import sqrt

class MathDojo:

    def __init__(self, result=0):
        self.result = result

    def add(self, num, *nums):
        acumsum = 0
        for i in nums:
            acumsum += i
        self.result += num + acumsum
        return self

    def subtract(self, num, *nums):
        acumsubtract = 0
        for i in nums:
            acumsubtract += i
        self.result-= acumsubtract + num
        return self

    def desvStandard(self, num, *nums):
        #determinación de promedio
        acumsum = 0
        avg = 0
        for i in nums:
            acumsum += i
        self.result += num + acumsum
        avg = (self.result/(1+len(nums)))
        #determinación cuadrado de la diferencia
        sqrdif = (num - avg)**2
        for i in nums:
            sqrdif += (i - avg)**2
        #determinación desviación estandar
        ds = sqrt(sqrdif/len(nums))
        self.result = ds
        return self




md = MathDojo()
#x=md.add(2).add(2,5,1).subtract(3,2).result
#print(x)

#print(md.subtract(2).result)
#print(md.subtract(3,2).result)
#print(md.subtract(2,5,1).result)
#print(md.add(2).result)
#print(md.add(2,3).result)
#print(md.add(2,5,1).result)

#print(md.desvStandard(3,2).result)
print(md.desvStandard(727.7,1086.5,1091,1361.3,1490.5,1956.1).result)