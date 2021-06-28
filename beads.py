'''
입력의 첫 번째 줄에는 구슬의 개수 nn이 주어집니다. (100≤n≤200000)

두 번째 줄부터는 토끼가 구슬을 넣는 행위가 주어집니다.

각 줄은 두 개의 정수 a, b로 이루어지며, 이 뜻은 구슬 a를 왼쪽 혹은 오른쪽으로 넣는다는 의미입니다. (1≤a≤1000000000)

(b가 0이면 왼쪽, b가 1이면 오른쪽이며 그 외의 입력은 주어지지 않는다)

출력
최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 출력한다.

1. ListPipe 클래스를 완성하세요. 
2. processBeads 함수를 완성하세요.

'''

class ListPipe:
    '''
    List를 이용하여 다음의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        리스트 myPipe를 만듭니다. 이는 구슬의 배치를 저장합니다.
        '''
        self.myPipe = []
        pass

    def addLeft(self, n) :
        '''
        파이프의 왼쪽으로 구슬 n을 삽입합니다.
        '''
        self.myPipe.insert(0,n) #0번째 위치에 n을 넣는다!
        pass

    def addRight(self, n) :
        '''
        파이프의 오른쪽으로 구슬 n을 삽입합니다.
        '''
        self.myPipe.append(n) #맨 오른쪽에 n 구술
        pass

    def getBeads(self) :
        '''
        파이프의 배치를 list로 반환합니다.
        '''
        return self.myPipe 
        


def processBeads(myInput) :
    '''
    구슬을 파이프에 넣는 행위가 myInput으로 주어질 때, 구슬의 최종 배치를 리스트로 반환하는 함수를 작성하세요.

    myInput[i][0] : i번째에 넣는 구슬의 번호
    myInput[i][1] : i번째에 넣는 방향

    예를 들어, 예제의 경우 

    myInput[0][0] = 1, myInput[0][1] = 0,
    myInput[1][0] = 2, myInput[1][1] = 1,
    myInput[2][0] = 3, myInput[2][1] = 0

    입니다.

    '''

    myPipe = ListPipe()
    
    for bead, direction in myInput :
    
        if direction == 0:
            myPipe.addLeft(bead)
            
        elif direction == 1:
            myPipe.addRight(bead)
            
            
    result = myPipe.getBeads()
    
    return result