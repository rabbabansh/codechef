for t in range(int(input())):
    num, x = map(int, input().split())
    num_list = list(str(num))

    if str(x) not in num_list:
        print(0)
    elif len(num_list) == 1:
        print(1)
    elif x == 0:
        first = 0
        rem = 0
        for i in range(len(num_list)):
            if int(num_list[i]) == x:
                first = len(num_list) - i - 1
                rem = int(str(num)[(i + 1) :])
                break
        bruh = 10 ** first - rem
        bruh += int("1" * first)
        print(bruh)
    else:
        first = 0
        rem = 0
        for i in range(len(num_list)):
            if int(num_list[i]) == x:
                first = len(num_list) - i - 1
                rem = int(str(num)[(i + 1) :])
                break
        print(10 ** first - rem)
