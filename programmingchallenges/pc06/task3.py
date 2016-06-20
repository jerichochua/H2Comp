#Programming Challenge 6: Bar Chart
#Task 3

def barChart3():
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
                if Xfrequency < 0:
                    print("Frequency out of range.")
                    print()
                    continue
                else:
                    X.append(Xvalue)
                    frequency.append(Xfrequency)
                    count +=1

    maximum = 0
    for freq in frequency:
        if freq > maximum:
            maximum = freq

    if maximum > 60:
        scale = maximum / 60
        scaling = True
    else:
        scaling = False

    print()
    print("+"*80)
    print("Frequency distribution")
    print("+"*80)

    if scaling is True:
        for i in range(len(X)):
            print("{0:^20}{1}".format("", "\u2588"*int(frequency[i]/scale)))
            print("{0:^20}{1}".format(X[i], "\u2588"*int(frequency[i]/scale)))
            print("{0:^20}{1}".format("", "\u2588"*int(frequency[i]/scale)))

        #Horizontal axis
        axisValue = maximum / 6
        print("{0:^20}{1}".format("", "-"*60))
        print("{0:^20}{1:<10}{2:<10.1f}{3:<10.1f}{4:<10.1f}{5:<10.1f}{6:<10.1f}{7:<10.1f}".format("", "0.0", axisValue, axisValue*2, axisValue*3, axisValue*4, axisValue*5, axisValue*6))
    else:
        for i in range(len(X)):
            print("{0:^20}{1}".format("", "\u2588"*frequency[i]))
            print("{0:^20}{1}".format(X[i], "\u2588"*frequency[i]))
            print("{0:^20}{1}".format("", "\u2588"*frequency[i]))

        #Horizontal axis
        print("{0:^20}{1}".format("", "-"*60))
        print("{0:^20}{1:<10}{2:<10}{3:<10}{4:<10}{5:<10}{6:<10}{7:<10}".format("", 0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0))
