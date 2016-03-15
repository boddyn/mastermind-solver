import random
class MastermindGame:

    solution = [0]
    guesses = [[0]]

    def __init__(self, numPeople, numTents):
        self.numPeople = numPeople
        self.numTents = numTents
        MastermindGame.solution = [numTents]
        MastermindGame.solution = [i for i in range(0, numPeople)]
        random.shuffle(MastermindGame.solution)
        MastermindGame.solution = MastermindGame.solution[:numTents]
        
    def solution(self):
        return MastermindGame.solution
        
    def makeMove(self, move):   
        result = [0]*2        
        for x in range(0, len(MastermindGame.solution)):
            if(move[x] == MastermindGame.solution[x]):
                result[0] += 1
            else:
                found = False
                for y in range (0, len(MastermindGame.solution)):
                    if(move[x] == MastermindGame.solution[y] and not found):
                        result[1] +=1
                        found = True
        return result
        
def main():
    x = MastermindGame(6, 4)
    print x.solution
    print x.makeMove([1,2,3,4])
    
main()