#blast.py    调用cmd执行blast
import os
import time
from multiprocessing import cpu_count    #读取CPU核心数用于匹配线程数
cpu=str(cpu_count())

a=input("What are you doing? \nIf nucleic acid, please enter 1 \nIf protein, please enter 2 \nIf nucleic acid and protein, please enter 3 \nenter:")
if(a=="1"):
    library=input("library file:")
    d=os.popen("makeblastdb -in %s -dbtype nucl -out library.fasta.blastdb" % (library))

    blast=input("blast file:")
    d=os.popen("blastn -query %s -db library.fasta.blastdb -out result.blast -outfmt 6 -evalue 1e-5 -num_threads %s" % (blast,cpu))
elif(a=="2"):
    library=input("library file:")
    d=os.popen("makeblastdb -in %s -dbtype nucl -out library.fasta.blastdb" % (library))

    blast=input("blast file:")
    d=os.popen("blastp -query %s -db library.fasta.blastdb -out result.blast -outfmt 6 -evalue 1e-5 -num_threads %s" % (blast,cpu))
elif(a=="3"):
    library=input("protein file:")
    d=os.popen("makeblastdb -in %s -dbtype nucl -out library.fasta.blastdb" % (library))

    blast=input("blast file:")
    d=os.popen("blastx -query %s -db library.fasta.blastdb -out result.blast -outfmt 6 -evalue 1e-5 -num_threads %s" % (blast,cpu))
else:
    print('format error')
time.sleep(2)
print('ok!!!')

#make by l.kiko