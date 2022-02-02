import pyupbit

access = "RH8VqHs82xQcjT1j7BKgSEUHHjwZ6EJpnxr9hmII"          # 본인 값으로 변경
secret = "cFNaoUTkOKykxJO4xFelfUHf1Hc5Vo8Sd0TpqxRe"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회