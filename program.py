filei = open('input.txt', 'r')
Lines = filei.readlines()
slurs = ["aaa","sss"]

fileo = open('output.txt', 'w')
fileo.write(" Hello, the degree of slurs in each line are ...")
count = 0
lno = 0
for line in Lines:
    lno = lno +1
    count = 0 
    for i in line.split() :
        if i in slurs:
            count =count+1           
    fileo.write("\n Line %04d: %04d "%(lno,count))

