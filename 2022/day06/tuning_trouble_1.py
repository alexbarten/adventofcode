with open('2022/day06/day06_1.txt', 'r') as tt:
    for signal in tt:
        for i in range(len(signal)):
            if len(set(signal[i:i+4])) == 4:
                print(i+4)
                break
