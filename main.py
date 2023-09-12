

class Neuron:

    def __init__(self):
        self.weight = 0.5
        self.smoothing = 0.00001
        self.lastError = 1

    def processInputData(self, inputN):
        
        return inputN * self.weight

    def restoreInputData(self, output):
        
        return output / self.weight

    def train(self, inputN, expectedResult):
        
        actualResult = inputN * self.weight
        self.lastError = expectedResult - actualResult
        correction = (self.lastError / actualResult) * self.smoothing
        self.weight += correction


def main():
    
    km = 1
    miles = 0.621371

    nr = Neuron()
    i = 0
    while  ((nr.lastError > nr.smoothing) or (nr.lastError < -nr.smoothing)):
        nr.train(km, miles)
        print(f'Шаг - {i}, Вес - {nr.weight}, Последняя ошибка - {nr.lastError}')
        i += 1
            
    print(nr.processInputData(1))
    print(nr.processInputData(1000))
    print(nr.processInputData(543))
      

if __name__ == "__main__":
    main()
    