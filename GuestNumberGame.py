import random

# 定义一个变量leave，用于表示难度
leave = 100

# 定义一个变量answer
answer = random.randint(0, leave)

#显示提示及游戏规则
print("我已经想好了一个100以内的整数，请猜猜我想的数是多少呢？\n要是现在不想玩了，那就打个00吧\n")

while True:
    temp = input("你的答案是：\n")
    guest_answer = int(temp)
    if guest_answer == 00:
        print("OK,既然你不想玩了那我就不勉强你啦！")
        break
    else:
        if guest_answer > answer:
            print("傻瓜，你猜的大啦。重新猜吧！")
        else:
            if guest_answer < answer:
                print("傻瓜，你猜的小啦，重新猜吧！")
            else:
                if guest_answer == answer:
                    print("哇塞，你好牛逼，猜对啦！")
                    break
