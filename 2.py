# generator rejestrowy
class RegisterGenerator:
    def __init__(self, p, q, seed):
        self.prev = seed       # ziarno o długości 7 wynikającej z max(p,q)
        self.len = 31          # długość liczby która ma zostać wygenerowana
        self.p = p
        self.q = q
    
    def generateNumber(self) -> float: 
        new = self.prev
        for i in range(7, self.len):
            new += str(int(new[i - self.p]) ^ int(new[i - self.q]))

        new = new[::-1]
        self.prev = new[:7]
        self.prev = self.prev[::-1]

        return int(new, 2)

    def generateNumbers(self, n: int) -> list:
        numbers = [self.generateNumber()]
        for _ in range(n-1):
            numbers.append(self.generateNumber())

        return numbers
    
    def classifyNumbers(self, numbers: list) -> list[int]:
        classification = [0 for _ in range(10)]
        for number in numbers:
            index = number * 10 // 2**31-1
            classification[index] += 1
        return classification
    

mulGen = RegisterGenerator(7, 3, "1001101")
numbers = mulGen.generateNumbers(100000)
classification = mulGen.classifyNumbers(numbers)
print(classification)