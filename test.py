print('--------------------------------Start----------------------')
counts = 1

while(counts<=3):
    temp =input("猜猜我是谁：")
    guess=int(temp)

    if guess ==8:
        print("Correct!")
        break
    else:
        if guess<8:
            print("Too Small")
        else:
            print("Too Large")
        counts = counts +1
        print("No you failed!")

print("End Game!")