f=open('/home/shaik-suhail/Documents/P2S2/python/Experiment_ITlab/Experiment_6/file1.txt','a+')
data= '''1.parrathipuram Manyam 
         2.Alluri Sitharama Raju
         3.Anakapalli
         4.Kakinada
         5.DR.BR Ambedkar konaseema
         6.Eluru
         7.NTR
         8.Palnadu
         9.Bapatla
         10.Nandyal
         11.Sri Sathya Sai
         12.Annamayya
         13.Tirupati'''
f.write('\n New disticts:\n')
f.write(data)
f.seek(0)
x=f.read()
f.close()
print(x)