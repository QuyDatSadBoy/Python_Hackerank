def count_parity():
    le = 0
    chan = 0
    a = []
    while True:
        try:
            s = input()
            a += list(map(int, s.split()))
        except EOFError:
            break
    for i in a:
        if (i % 2 == 1):
            le += 1
        else:
            chan += 1
    if chan > le:
        print("CHAN")
    elif chan < le:
        print("LE")
    else:
        print("CHANLE")


count_parity()
