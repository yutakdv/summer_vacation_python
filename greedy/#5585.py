#greedy algorithm

money = int(input())
g_money = 1000 - money
cnt = 0

while g_money != 0:
    if g_money // 500:
        cnt += g_money // 500
        g_money = g_money % 500
    elif g_money // 100:
        cnt += g_money // 100
        g_money = g_money % 100
    elif g_money // 50:
        cnt += g_money // 50
        g_money = g_money % 50
    elif g_money // 10:
        cnt += g_money // 10
        g_money = g_money % 10
    elif g_money // 5:
        cnt += g_money // 5
        g_money = g_money % 5
    else:
        cnt += g_money
        break

print(cnt)