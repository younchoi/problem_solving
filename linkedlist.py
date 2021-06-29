
"""
Linked List
"""

'''
 (commit1에서 배열로 구현했던 걸 연결list로 구현한다. )

1.입력의 첫 번째 줄에는 구슬의 개수  n이 주어집니다. (100≤n≤200000)
2. 두 번째 줄부터는 토끼가 구슬을 넣는 행위가 주어집니다.
3. 각 줄은 두 개의 정수 a, b로 이루어지며, 이 뜻은 구슬 a를 왼쪽 혹은 오른쪽으로 넣는다는 의미
(b가 0이면 왼쪽, b가 1이면 오른쪽이며 그 외의 입력은 주어지지 않는다)
출력
최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 출력한다.
# 파이썬 내장 라이브러리로 제공되는 자료구조 덱과 큐는 연결 리스트로 구현되어 있다.

'''
class LinkedListElement :
    def __init__(self, val, ptr) :
        self.value = None
        self.myNext = None

class LinkedListPipe:
    '''
    Linked List를 이용하여 다음의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        리스트 myPipe를 만듭니다. 이는 구슬의 배치를 저장합니다.
        '''
        self.start = None
        self.end = None
        pass

    def addLeft(self, n) :
        '''
        파이프의 왼쪽으로 구슬 n을 삽입합니다.
        '''
        pass

    def addRight(self, n) :
        '''
        파이프의 오른쪽으로 구슬 n을 삽입합니다.
        '''
        pass

    def getBeads(self) :
        '''
        파이프의 배치를 list로 반환합니다.
        '''
        pass

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

    myPipe = LinkedListPipe()

    result = []

    return result