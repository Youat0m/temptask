with open('CdSe_CdZnS Core_Shell.txt','r') as f:
    x = []
    y = []
    for line in f:
        x.append(int(line.split(',')[0]))
        y.append(float(line.split()[1].replace(',','.')))
    sum = 0
    for i in y:
        sum += i
    arth = sum/len(y)
    sigmasum = 0
    for i in y:
        sigmasum += (i-arth)**2
    sigma = (sigmasum/len(y))**0.5
    print('среднее: ',arth)
    print('среднеквадратичное отклонение:',sigma)
    z= input()
    