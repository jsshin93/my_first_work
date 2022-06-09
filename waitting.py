# 웨이팅프로그램 선형

from datetime import datetime

guest = []
wnum = 0

now = datetime.now()
current_time = now.strftime("%H:%M")

def print_guest():
     for i in range(0,wnum,1):
         print(guest[i])


while True:
    
    print("1.웨이팅 2.예약 3.나가기")
    choice = int(input())
    guest.append(None)
    
    
    if choice == 1:
    
        name = input("이름입력: ")
        phone = input("전화번호: ")
        num = input("인원수: ")
        
        wnum += 1
        
        guest[wnum-1] = (name, phone, num, current_time)
        # print(guest[wnum-1])
        print_guest()
        print("대기번호 ",wnum)
        print(guest[wnum-1][3])
        print()
    
    elif choice ==2:
        
        name = input("이름입력: ")
        phone = input("전화번호: ")
        num = input("인원수: ")
        time = input("예약시간(H:M): ")
        
        wnum += 1
        guest[wnum-1] = (name, phone, num, time)
        
        
        # 시간순 정렬이 제대로 안됨
        for i in range(0, wnum):
            for j in range(1,wnum):
                if guest[i][3]>guest[j][3]:
                    temp = guest[i]
                    guest[i] = guest[j]
                    guest[j] = temp

        print_guest()
        print()
    
    elif choice == 3:
        break            
                 
                 
                   
        
    