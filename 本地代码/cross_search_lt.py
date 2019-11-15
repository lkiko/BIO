#cross_search_lt.py利用数组方法。根据txt文件中的基因ID，从blast文件中查找对应基因位置，再从对应fasta文件中提取出对应序列并输出为新文件。
#    运行环境win
#blast文件提取函数
def blast(a):
    for line in open("D:\\VScode\\python lab\\Python区\\file\\source_\\Ca_Dr.blk1.blast",mode='r'):#打开blast文件
    	b_1=line#按行读入
    	b_1_1=[]#设置空数组
    	b_1=b_1.replace('	',',')#将tab键替换成逗号
    	b_1_1=b_1.split(',')#以逗号为标记将字符串转为列表
    	if(b_1_1[0]==a):#对列表第一个元素（基因ID）进行判断是否于传入的基因的ID相同
        	b_1_1=b_1_1[0:2]+b_1_1[6:10]#相同则重新赋值为两个基因ID和位置信息
        	return(b_1_1)#返回新列表

#fasta文件提取函数
def fa1(a):
    s=''#储存序列
    s1=''#储存ID
    for line in open("D:\\VScode\\python lab\\Python区\\file\\source_\\Ca_Dr.fasta",mode='r'):#打开目标fasta文件，按行读取
        x=line
        x=x.strip('\n')#去除末尾换行
        if(x[0]=='>'):#判断是ID还是序列
            s=s+','#不同序列与ID之间以逗号隔开 第一个ID时序列多出一个逗号
            s1=s1+x+','#将读取的ID行储存至字符串以逗号隔开 最后一个ID后面也会有一个逗号要记得去除
        else:
            s=s+x#将读取的序列储存至字符串
    lt=s.split(',')#以逗号为标记字符串转列表，序列 开头为空格元素
    lt1=s1.split(',')#以逗号为标记字符串转列表，ID
    lt=lt[1:]#去除开头的空格元素
    lt1=lt1[:-1]#去除最后一个ID后面的逗号带来的空格元素
    for i in range(len(lt)):#设置循环次数以ID个数为准
        lt1.insert(2*i+1,lt[i])#将序列数组按1、3、5...的位置插入ID列表中，lt1成为ID+序列的复合列表 偶数为ID（包括0）奇数为序列
    m1=''#设置储存目标位置的空字符串 第一个ID
    m2=''#设置储存目标位置的空字符串 第二个ID
    for i in range(int(len(lt1)/2)):#设置循环 次数为lt1 ID数
        if(lt1[2*i]==a[0]):#判断偶数位是否与函数外变量0位（第一个ID）相等
            if(int(a[2])<int(a[3])):#判断序列始末位置 前小于后 从前往后
                m1=lt1[2*i+1]
                m1=m1[int(a[2])-1:int(a[3])+1]#取对应位置的序列！注意切片操作前减后加
            elif(int(a[2])>int(a[3])):#判断序列始末位置 前大于后 从后往前
                m1=lt1[2*i+1]
                m1=m1[int(a[3])-1:int(a[2])+1]#取对应位置的序列！注意切片操作前减后加
        elif(lt1[2*i]==a[1]):#判断偶数位是否与函数外变量1位（第二个ID）相等
            if(int(a[4])<int(a[5])):#判断序列始末位置 前小于后 从前往后
                m2=lt1[2*i+1]
                m2=m2[int(a[4])-1:int(a[5])+1]#取对应位置的序列！注意切片操作前减后加
            elif(int(a[4])>int(a[5])):#判断序列始末位置 前大于后 从后往前
                m2=lt1[2*i+1]
                m2=m2[int(a[5])-1:int(a[4])+1]#取对应位置的序列！注意切片操作前减后加
    m=''#设置返回字符串
    m=a[0]+'\n'+m1+'\n'+a[1]+'\n'+m2#返回字符串格式
    return(m)#返回字符串m

#主函数
k_1=''#设置一个用于储存信息的字符串
b_1_1=''#设置一个用于储存信息的字符串
f=open("D:\\VScode\\python lab\\Python区\\file\\result\\Ca_Dr.blk2.txt",mode='w')#创建结果文件
for line in open("D:\\VScode\\python lab\\Python区\\file\\source_\\Ca_Dr.blk1.txt",mode='r'):#打开txt文件
    x_1=line#按行写入
    k_1_1=[]#设置空列表
    if(x_1[0]=='C' or x_1[0]=='A'):#判断
    	x_1=x_1.replace(' ',',')#逗号替换空格
    	k_1_1=x_1.split(',')#字符串转列表以逗号为标记
    	b_1_1=blast(k_1_1[0])#向blast函数输入列表的0位元素：查询序列一的碱基位置
    	b_1_1[0]='>'+b_1_1[0]#在序列一ID前加上>
    	b_1_1[1]='>'+b_1_1[1]#在序列二ID前加上>
    	m=fa1(b_1_1)#按照blast函数返回的位置信息去fasta文件取出相应的碱基
    	f.write(m)#写入文件
    	f.write('\n')#写入换行
f.close()#关闭文件
print('ok!!!')#运行结束标志

#make by l.kiko