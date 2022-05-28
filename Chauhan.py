""" Create a file a.txt and enter the values from 50 to 500 with space"""

f=open("a.txt",'w')
for i in range(50,501):
    x=str(i)
    f.write(x+' ')
f.close()
