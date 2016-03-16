import random
import math
class MastermindGame:

    def __init__(self, numPeople, numTents):
        tents = 4
        people = 6
        if type(numPeople) is int and numPeople > 0:
            people = numPeople
        if type(numTents) is int and numTents > 0:
            tents = numTents
        self.__solution = [tents]
        self.__solution = [i for i in range(1, people + 1)]
        random.shuffle(self.__solution)
        self.__solution = self.__solution[:tents]
        self.__guesses = [[]]
        
    def makeGuess(self, guess):
        if type(guess) is list and len(guess) == len(self.__solution):
            self.__guesses.append(guess)
            result = [0]*2
            for x in range(0, len(self.__solution)):
                if(guess[x] == self.__solution[x]):
                    result[0] += 1
                else:
                    for y in range (0, len(self.__solution)):
                        if(guess[x] == self.__solution[y]):
                            result[1] +=1
                            break
            return result
        else:
            return 'invalid guess'
        
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
            result = x.makeGuess([w for w in range(1, tents + 1)])
            i += 1
        results[j] = i
    average = (sum(results) * 1.0) / len(results)
    print 'Average should approach: ' + str(math.factorial(people)/math.factorial(people - tents))
    print 'Average: ' + str(average)
    return average

def main():
    getAvgFirstGuess(6, 4, 100)
    
main()