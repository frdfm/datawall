from PI1000000 import PI1000000;
r=PI1000000[2:];
o0=3*19*23*43*47;
i0=7*17*29*41*53;
j0=11*13*31*37*59;


def constanthash(o,i):#obj_id, replica_index
    res="";
    for j in range(0,3):#server_id_jth_digit
        res+=r[(o*o0+i*i*i0+j*j*j*j0)%1000000];
    return int(res);



#example        
for i in range(1,11):
    print constanthash(10,i);#prints ith replica of the object 10 in 1000 servers
