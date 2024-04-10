# 100'000 liczb
# od 0 do 2^31 - 1

# generator liniowy multiplikatywny
class MultiplicativeGenerator:
    def __init__(self, a: int, c: int, m: int, seed: int):
        self.a = a
        self.c = c
        self.m = m
        self.prev = seed
    
    def generateNumber(self) -> int: 
        self.prev = (self.a * self.prev + self.c) % self.m
        return self.prev

    def generateNumbers(self, n: int) -> list[int]:
        numbers = [self.generateNumber()]
        for _ in range(n-1):
            numbers.append(self.generateNumber())

        return numbers
    
    def classifyNumbers(self, numbers: list) -> list[int]:
        classification = [0 for _ in range(10)]
        for number in numbers:
            index = number * 10 // self.m
            classification[index] += 1

        return classification
    

mulGen = MultiplicativeGenerator(69069, 1, 2**31-1, 15)
numbers = mulGen.generateNumbers(100000)
classification = mulGen.classifyNumbers(numbers)
print(classification)