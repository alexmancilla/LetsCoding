# Sol 0
# print(max([sum(i) for i in accounts]))

# Sol 1
accounts = [[1,5],[7,3],[3,5]]

n = len(accounts)
m = len(accounts[0])

max_money = 0

for i in range(n):
    money_for_account = 0
    for j in range(m):
        money_for_account += accounts[i][j]

    max_money = max(max_money, money_for_account)


print(f'max money for account {max_money}')
# return max_money
