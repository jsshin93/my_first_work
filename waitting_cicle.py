# 웨이팅 원형
# 대기번호 호출에 문제가 있음

class Node():
    def __init__(self):
        self.data = None
        self.link = None

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M")

head = None
pre = None
current = None
count = 0

def sort_node(info):
    
    node = Node()
    
    node.data = info
    
    print(node.data)
    
    global head, pre, current, count
    
    if head == None:
        head = node
        return
    
    if head.data[3]>info[3]:
        node.link = head
        head = node
        
    current = head

    while current.link != None:
        
        pre = current
        current = current.link
        
        if current.data[3]>info[3]:
            pre.link = node
            node.link = current
            return
        
        
    current.link = node
            
    
    
def print_node():
    current = head
    print(head.data)
    while current.link != None:
        current = current.link
        print(current.data)
            
        
    
    
    


if __name__ == "__main__":
    
    while True:
        
        print("1. 대기  2. 예약  3. 나가기")
        choice = int(input())
        
        if choice == 1:
            name = input("이름: ")
            phone = input("전화번호: ")
            people = input("인원수: ")
            count +=1
            
            sort_node((name, phone, people, current_time))
            
            print_node()
        
        
        elif choice == 2:
            name = input("이름: ")
            phone = input("전화번호: ")
            people = input("인원수: ")
            time = input("예약시간: ")
            count +=1
            sort_node((name, phone, people, time))
            
            print_node()
            
        
        
        
        elif choice == 3:
            print("종료")
            break
        
        else:
            print("잘못된 입력")
            continue
    