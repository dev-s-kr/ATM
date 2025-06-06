#잔액 초기화
balance = 1000


#조건이 True면 계속 작동
while True:

    #사용자가 기능 선택
    num = input("사용하실 기능을 선택해주세요. (1.입금, 2.출금, 3.영수증 보기, 4.종료) : ")

    #종료 기능 선택(4번)
    if num == "4":
        print("종료")
        break