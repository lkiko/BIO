#cross_search.py    字典方法 根据txt文件中的基因ID，从blast文件中查找对应基因位置，再从对应fasta文件中提取出对应序列并输出为新文件。
#    运行环境win
def blast(a):    #搜索基因位置函数
    import re    #引用正则
    dic={}    #建立空字典
    for line in open("D:\\VScode\\python lab\\Python区\\file\\source_\\Ca_Dr.blk1.blast",mode='r'):    #打开文件
        line = line.strip('\n')    #去除结尾换行符
        if(re.match('C',line)):    #正则判断
            b = line.split('\t')    #按照\t分为数组
            lt1=[b[6],b[7]]    #设置数组1，对应第一物种基因位置
            lt2=[b[8],b[9]]    #设置数组2，对应第二物种基因位置
            dic[b[0]]=lt1    #建立第一物种指向关系dic[键]=值
            dic[b[1]]=lt2    #建立第二物种指向关系dic[键]=值
    b_1_1=[a[0],a[2],dic[a[0]][0],dic[a[0]][1],dic[a[2]][0],dic[a[2]][1]]    #for循环外即字典建成后检索两物种输出
    return(b_1_1)    #返回列表


def fa11(a):    #物种一序列检索
    dic={}    #建立空字典
    s=''    #建立空字符串储存读取行
    s1=''    #建立空字符串储存读取行累加
    for line in open("D:\\VScode\\python lab\\Python区\\file\\source_\\Ca_Dr.fasta",mode='r'):    #打开文件
        x=line    #这一步有点多余...
        x=x.strip('\n')    #去除结尾换行符
        if(x[0]=='>'):    #判断方法二，也可以使用正则import re 判断是否为id行
            s=s+','    #添加标记符
            s1=s1+x+','    #添加标记符
        else:
            s=s+x
    lt=s.split(',')    #以标记符为界字符转数组
    lt1=s1.split(',')    #以标记符为界字符转数组
    lt=lt[1:]    #去开头空元素
    lt1=lt1[:-1]    #去除结尾空元素
    for i in range(len(lt)):    #建立字典钥值关系循环，次数为数组长度
        dic[lt1[i]]=lt[i]    #建立字典钥值关系
    m1=''    #建立空字符串
    if(int(a[1])<int(a[2])):    #判断位置关系
        m1=dic[a[0]][int(a[1])-1:int(a[2])+1]    #赋值字典加
    elif(int(a[1])>int(a[2])):    #判断位置关系
        m1=dic[a[0]][int(a[2])-1:int(a[1])+1]    #赋值字典加
    m1=a[0]+'\n'+m1+'\n'    #设置格式
    return(m1)    #返回字符串

def fa12(a):    #物种er序列检索
    dic={}    #建立空字典
    s=''    #建立空字符串储存读取行
    s1=''    #建立空字符串储存读取行累加
    for line in open("D:\\VScode\\python lab\\Python区\\file\\source_\\b1.fasta",mode='r'):    #打开文件
        x=line    #这一步有点多余...
        x=x.strip('\n')    #去除结尾换行符
        if(x[0]=='>'):    #判断方法二，也可以使用正则import re 判断是否为id行
            s=s+','    #添加标记符
            s1=s1+x+','    #添加标记符
        else:
            s=s+x
    lt=s.split(',')    #以标记符为界字符转数组
    lt1=s1.split(',')    #以标记符为界字符转数组
    lt=lt[1:]    #去开头空元素
    lt1=lt1[:-1]    #去除结尾空元素
    for i in range(len(lt)):    #建立字典钥值关系循环，次数为数组长度
        dic[lt1[i]]=lt[i]    #建立字典钥值关系
    m1=''    #建立空字符串
    if(int(a[1])<int(a[2])):    #判断位置关系
        m2=dic[a[0]][int(a[1])-1:int(a[2])+1]    #赋值字典加
    elif(int(a[1])>int(a[2])):    #判断位置关系
        m2=dic[a[0]][int(a[2])-1:int(a[1])+1]    #赋值字典加
    m2=a[0]+'\n'+m2+'\n'    #设置格式
    return(m2)    #返回字符串

#主函数
k_1=''    #设置空字符串
b_1_1=''    #设置空字符串
f=open("D:\\VScode\\python lab\\Python区\\file\\result\\测试.blk3.txt",mode='w')    #建立输出文件
for line in open("D:\\VScode\\python lab\\Python区\\file\\source_\\Ca_Dr.blk1.txt",mode='r'):    #打开文件
    x_1=line
    k_1_1=[]
    b_2=[]
    b_3=[]
    if(x_1[0]=='C' or x_1[0]=='A'):
        x_1=x_1.replace(' ',',')    #以逗号替换空格
        k_1_1=x_1.split(',')    #以逗号为界转数组
        b_1_1=blast(k_1_1)
        b_1_1[0]='>'+b_1_1[0]    #添加>id前缀
        b_1_1[1]='>'+b_1_1[1]
        b_2=[b_1_1[0],b_1_1[2],b_1_1[3]]
        b_3=[b_1_1[1],b_1_1[4],b_1_1[5]]
        m1=fa11(b_2)
        m2=fa12(b_3)
        m1=fa11(b_2)
        f.write(m1)    #文件写入物种一
        m2=fa12(b_3)
        f.write(m2)    #文件写入物种二
        f.write('\n')
f.close()
print('ok!!!')    #运行结束提醒

#make by l.kiko