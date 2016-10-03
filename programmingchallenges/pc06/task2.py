# Programming Challenge 6: Bar Chart
# A-Levels 2013 Q4
# Task 2

def barChart2():
    X = []
    frequency = []
    count = 0

    loop = True
    while loop:
        if count > 5:
            loop = False
        else:
            Xvalue = input("Next X value ... <ZZZ to END> ")
            if Xvalue == "ZZZ":
                break
            else:
                Xfrequency = eval(input("Frequency ... "))
                if Xfrequency < 0 or Xfrequency > 60:
                    print("Frequency out of range.")
                    print()
                    continue
                else:
                    X.append(Xvalue)
                    frequency.append(Xfrequency)
                    count +=1

    print()
    print("+"*80)
    print("Frequency distribution")
    print("+"*80)
    for i in range(len(X)):
        print("{0:^20}{1}".format("", "\u2588"*frequency[i]))
        print("{0:^20}{1}".format(X[i], "\u2588"*frequency[i]))
        print("{0:^20}{1}".format("", "\u2588"*frequency[i]))
