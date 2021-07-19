from random import randint,random,seed;

def hash1(s):
    seed(int(s));
    return random();

def datawall(id1):
    dest=[];
    hpl=[];
    for d in D:
        hpl.append(hash1(int(id1)*2*3*5*7*11*13*17*19*23*29*31+int(d)));
        dest.append(d);
    return [x for _, x in sorted(zip(hpl, dest))]

D=range(0,10);#10 servers

for j in range(1,11):
    print datawall(j); #prints the list of ordered and unique replicas for obj j




    
    
 
        






        

