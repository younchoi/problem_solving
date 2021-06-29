'''
orderManager 클래스를 완성하세요.
이 주문 관리 시스템은 총 3가지 기능 주문생성, 주문취소, 주문조회를 구현해야 합니다.
'''

class orderManager :
    '''
    주문을 처리하는 class를 작성합니다.
    '''

    def __init__(self) :
        '''
        이 부분은 고치지 마세요.
        '''
        self.data = []

    def addOrder(self, orderId) :
        '''
        주문번호 orderId를 추가합니다.
        '''
        self.data.append(orderId)
        pass

    def removeOrder(self, orderId) :
        '''
        주문번호 orderId를 제거합니다.
        '''
        self.data.remove(orderId)
        pass

    def getOrder(self, orderId) :
        '''
        주문번호 orderId가 몇 번째로 처리될지를 반환합니다.

        만약 주문번호 orderId가 존재하지 않으면 -1을 반환합니다. 
        '''
        
        for i in range(len(self.data)) :
            if self.data[i] == orderId :
                return(i + 1)
        return -1
        
        
        pass