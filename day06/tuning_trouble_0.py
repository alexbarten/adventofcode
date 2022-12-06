with open('day06/day06_1.txt', 'r') as tt:
    signal = tt.readline()
    for i in range(len(signal)):
        sig_set = signal[i:i+4]
        if len(set(sig_set)) == 4:
            print(i+4)
            break
