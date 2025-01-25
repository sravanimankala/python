# #file handlings and modes
# #'r' mode =used to read the data from existing file
file=open("file.txt",mode='r')
read_data=file.read()
print(read_data)
file.close()

# #'a' =used to append the data to existing file or create file
file=open("file.txt",mode='a')
write_data=file.write("\nthis is sravani")
file.close()

# #'w'=used to write the data in the eisting file or create new file
file=open("file.txt",mode='w')
write_data1=file.write("hello")
file.close()

#r+ is used to read,append,write the data into existing file
file=open("file.txt",mode='r+')
write_data=file.write("this is sravani")
write_data1=file.writelines(["\nhooo","heloo"])
file.seek(0)
read_data=file.readline()
read_data1=file.readlines()
print(read_data)
print(read_data1)
file.close()

#w+ is used to read,write,append and creating the new file
file=open("file.txt",mode='w+')
write_data=file.write("prince\n")
write_data1=file.writelines(["hooo","hiii"])
file.seek(0)
read_data=file.readline()
read_data1=file.readlines()
print(read_data)
print(read_data1)
file.close()

#a+ is used to read,write,append and creating the new file 
file=open("niha.txt",mode='w+')
write_data1=file.write("gill\n")
write_data2=file.writelines(["hloo","hiii"])
append_data=file.write("hlooo")
file.seek(0)
read_data=file.readline()
read_data1=file.readlines()
print(read_data)
print(read_data1)
file.close()


