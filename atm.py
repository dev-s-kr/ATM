#잔액 초기화
balance = 1000

#조건이 True면 계속 작동
while True:

    #사용자가 기능 선택
    num = input("사용하실 기능의 번호를 입력해주세요. (1.입금, 2.출금, 3.영수증 보기, 4.종료) : ")
    
    #출금 기능 선택(2번)
    if num == "2":
        withdraw_amount = int(input("출금할 금액을 입력해주세요 : "))
        withdraw_amount = min(balance, withdraw_amount)
        balance -= withdraw_amount
        print(f"출금하신 금액은 {withdraw_amount}원입니다. 현재 잔액은 {balance}원입니다.")

    #입금 기능 선택(1번)
    if num == "1":
        deposit_amount = int(input("입금할 금액을 입력해주세요 : "))
        balance += deposit_amount
        print(f"입금하신 금액은 {deposit_amount}원입니다. 현재 잔액은 {balance}원입니다.")

    #종료 기능 선택(4번)
    if num == "4":
        print("종료")
        break