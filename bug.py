import numpy as np
                
def rebug(bugin,bugout,patch,bit,time,condition,result,t,p,answer):   
    if(np.array_equal(bugin,bugout)):
        print 'Time =',t
        for i in range(0,len(answer)):
            print "P",p[i],": ",answer[i]
    else :      
        b = np.zeros([int(patch)])
        check(b,bugin,patch,bit,condition)
        p.append((np.argmax(b)+1))
        t += time[np.argmax(b)]
        i = np.argmax(b)
        for j in range (0,int(bit)):
            if(result[i][j] == '0'):
                bugin[j] = bugin[j]                   
            else:
                bugin[j] = result[i][j]
        answer.append(list(bugin))
        rebug(bugin,bugout,patch,bit,time,condition,result,t,p,answer)
        
def check(bdata,bugin,patch,bit,condition):
    for i in range (0,int(patch)):  
        for j in range (0,int(bit)): 
            if bugin[j] == condition[i][j] and condition[i][j] == '+' :               
                bdata[i]= bdata[i]+1
            elif bugin[j] == condition[i][j] and condition[i][j] == '-' :
                bdata[i]= bdata[i]+2
            elif bugin[j] != condition[i][j] and condition[i][j] == '0' :
                bdata[i]= bdata[i]+0 
            else:
                bdata[i]= bdata[i]-99

###########################  MAIN  ###################################
print 'Enter number of bit' 
bit=raw_input()
print 'Enter number of patch'
patch=raw_input()
bugin = ['+']*int(bit)
bugout = ['-']*int(bit)
data=['']*int(patch)
time_s=['']*int(patch)
condi_s=['']*int(patch)
result_s=['']*int(patch)
for i in range(0,int(patch)):
        print 'Enter patch',i+1,'[time precon post]--> [1 000 00-]',':'
        data[i]=raw_input()
        data[i]=data[i].split()
        time_s[i]=data[i][0]
        condi_s[i]=data[i][1]
        result_s[i]=data[i][2]
time = []
condition = []
result = []
for i in range (0,int(patch)):
        time.append(int(time_s[i]))
        condition.append(list(condi_s[i]))
        result.append(list(result_s[i]))
print 'IN :',bugin
for i in range (0,int(patch)):
        print 'P',i+1,':',' ',time[i],'  ',
        for j in range (0,int(bit)):            
            print condition[i][j],
        print '    ',
        for k in range (0,int(bit)):      
            print result[i][k],
        print ' '
t = 0
p=[]
answer=[]
rebug(bugin,bugout,patch,bit,time,condition,result,t,p,answer)
print 'OUT :',answer[len(answer)-1]
