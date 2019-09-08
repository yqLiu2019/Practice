score = 0
while(score != 999):
    score =int(input("请输入分数:"))
    if score == 999:
        print("Done!")
    elif 90<score<=100:
        print("A")
    elif 80<score<=90:
        print("B")
    elif 70<score<=80:
        print("C")
    else:
        print("Wrong Score")

print("Finished")