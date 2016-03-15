import random
import math
class MastermindGame:

    guesses = [[0]]

    def __init__(self, numPeople, numTents):
        self.numPeople = numPeople
        self.numTents = numTents
        self.__solution = [numTents]
        self.__solution = [i for i in range(1, numPeople + 1)]
        random.shuffle(self.__solution)
        self.__solution = self.__solution[:numTents]
        
    def makeMove(self, move):
        if type(move) is list and len(move) == len(self.__solution):
            result = [0]*2
            for x in range(0, len(self.__solution)):
                if(move[x] == self.__solution[x]):
                    result[0] += 1
                else:
                    for y in range (0, len(self.__solution)):
                        if(move[x] == self.__solution[y]):
                            result[1] +=1
                            break
            return result
        else:
            return 'move parameter is invalid'
        
def getAvgFirstGuess(numPeople, numTents, numGuesses):
    people = numPeople
    tents = numTents
    guesses = numGuesses
    results = [0] * guesses
    for j in range(0, guesses):
        i = 0
        result = [0,0]
        while result[0] != tents:
            x = MastermindGame(people, tents)
            result = x.makeMove([w for w in range(1, tents + 1)])
            i += 1
        results[j] = i
    average = (sum(results) * 1.0) / len(results)
    print 'Average should approach: ' + str(math.factorial(people)/math.factorial(people - tents))
    print 'Average: ' + str(average)
    return average

def main():
    getAvgFirstGuess(6, 4, 1000)
    
main()