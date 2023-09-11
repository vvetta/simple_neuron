

class Neuron:

    def __init__(self):
        self.weight = 0.5
        self.smoothing = 0.00001
        self.lastError = 0

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
    
    km = 100
    miles = 62.1371

    nr = Neuron()

    for iter in range(1000000):

        nr.train(km, miles)
        print(iter)

        # if ((nr.lastError > nr.smoothing) or (nr.lastError < -nr.smoothing)):
        #     nr.train(km, miles)
        #     print(iter)
    print(nr.processInputData(km))



    


if __name__ == "__main__":
    main()