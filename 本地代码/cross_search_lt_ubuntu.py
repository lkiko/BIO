#cross_search_lt_ubuntu.py用数组方法。根据txt文件中的基因ID，从blast文件中查找对应基因位置，再从对应fasta文件中提取出对应序列并输出为新文件。
#    运行环境ubuntu
def blast(a):
    for line in open("/home/kiko/source/Ca_Dr.blast.blast",mode='r'):
    	b_1=line
    	b_1_1=[]
    	b_1=b_1.replace('	',',')
    	b_1_1=b_1.split(',')
    	if(b_1_1[0]==a[0]):
        	if(b_1_1[1]==a[2]):
        	    b_1_1=b_1_1[0:2]+b_1_1[6:10]
        	    return(b_1_1)


def fa11(a):
    s=''
    s1=''
    for line in open("/home/kiko/source/Ca_Dr.fasta",mode='r'):
        x=line
        x=x.strip('\n')
        if(x[0]=='>'):
            s=s+','
            s1=s1+x+','
        else:
            s=s+x
    lt=s.split(',')
    lt1=s1.split(',')
    lt=lt[1:]
    lt1=lt1[:-1]
    for i in range(len(lt)):
        lt1.insert(2*i+1,lt[i])
    m1=''
    for i in range(int(len(lt1)/2)):
        if(lt1[2*i]==a[0]):
            if(int(a[1])<int(a[2])):
                m1=lt1[2*i+1]
                m1=m1[int(a[1])-1:int(a[2])+1]
            elif(int(a[1])>int(a[2])):
                m1=lt1[2*i+1]
                m1=m1[int(a[2])-1:int(a[1])+1]
    m1=a[0]+'\n'+m1+'\n'
    return(m1)

def fa12(a):
    s=''
    s1=''
    for line in open("/home/kiko/source/b1.fasta",mode='r'):
        x=line
        x=x.strip('\n')
        if(x[0]=='>'):
            s=s+','
            s1=s1+x+','
        else:
            s=s+x
    lt=s.split(',')
    lt1=s1.split(',')
    lt=lt[1:]
    lt1=lt1[:-1]
    for i in range(len(lt)):
        lt1.insert(2*i+1,lt[i])
    m2=''
    for i in range(int(len(lt1)/2)):
        if(lt1[2*i]==a[0]):
            if(int(a[1])<int(a[2])):
                m2=lt1[2*i+1]
                m2=m2[int(a[1])-1:int(a[2])+1]
            elif(int(a[1])>int(a[2])):
                m2=lt1[2*i+1]
                m2=m2[int(a[2])-1:int(a[1])+1]
    m2=a[0]+'\n'+m2+'\n'
    return(m2)

k_1=''
b_1_1=''
f=open("/home/kiko/result/测试.txt",mode='w')
for line in open("/home/kiko/source/Ca_Dr.blk1.txt",mode='r'):
    x_1=line
    k_1_1=[]
    b_2=[]
    b_3=[]
    if(x_1[0]=='C' or x_1[0]=='A'):
    	x_1=x_1.replace(' ',',')
    	k_1_1=x_1.split(',')
    	b_1_1=blast(k_1_1)
    	b_1_1[0]='>'+b_1_1[0]
    	b_1_1[1]='>'+b_1_1[1]
    	b_2=[b_1_1[0],b_1_1[2],b_1_1[3]]
    	b_3=[b_1_1[1],b_1_1[4],b_1_1[5]]
    	m1=fa11(b_2)
    	m2=fa12(b_3)
    	m1=fa11(b_2)
    	f.write(m1)
    	m2=fa12(b_3)
    	f.write(m2)
    	f.write('\n')

f.close()
print('ok!!!')
#make by l.kiko

