f=open("b.txt",'w')
for i in range(50,501):
    x=str(i)
    f.write(x+'\n')
f.close()
