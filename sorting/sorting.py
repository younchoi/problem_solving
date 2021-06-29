'''
내림차순 정렬하기

단, ‘최댓값 기계’문제에서 작성하였던 자료구조를 이용하여 문제를 풀도록 합니다.

숫자들을 최댓값 기계에 넣고, 최댓값 기계에서 반환되는 숫자들을 받아 출력하면 됩니다.

지시사항
입력
첫째줄에 nn개의 정수들이 공백으로 구분되어 입력됩니다. (100≤n≤200000)

출력
입력된 정수들을 내림차순으로 정렬하여 출력합니다.

1. maxMachine 클래스를 완성하세요.
2. sorting 함수를 완성하세요.
'''

class maxMachine :
    
    def __init__(self) :
        self.myData = []

    def addNumber(self, n) :
        self.myData.append(n)

    def removeNumber(self, n) :
        self.myData.remove(n)

    def getMax(self) :
        return max(self.myData)

def sorting(myList) :
    '''
    myList를 내림차순으로 정렬하여 반환하는 함수를 작성하세요.

    예를 들어, myList = [5, 2, 3, 1] 이라면 [5, 3, 2, 1] 을 반환해야 합니다.

    단, maxMachine class를 이용하도록 합니다. 
    '''

    myMachine = maxMachine()
    

    result = []
    
    for element in myList :    
        myMachine.addNumber(element)
    
    for i in range(len(myList)) :
        myMax = myMachine.getMax()
        
        result.append(myMax)
        
        myMachine.removeNumber(myMax)

    return result