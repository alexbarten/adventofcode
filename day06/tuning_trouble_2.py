with open('day06/day06_1.txt', 'r') as tt:
    for signal in tt:
        for i in range(len(signal)):
            sig_set = signal[i:i+14]
            if len(set(sig_set)) == 14:
                print(i+14)
                break
