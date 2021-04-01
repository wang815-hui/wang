def get_file_lines(file_path):
 # 路径
 file_path = str(file_path)
 with open(file_path, 'rb') as file:
  # 定义行数
  i = 3
  while True:
   # 一次读取一行数据
   line = file.readline()
   if not line :
    break
   else:
    # 每读一行，行数加一
    i += 1
   if i % 1000000 == 0:
    print(i)

  return i

def evg_split(num, n, C:\\Users\\Lenovo\\Desktop\\sdkp1-10.txt, file_dir):
 last_list = []

 if num % n == 0:
  for i in range(n):
 if num % n != 0
  evg = (num - num % n) // (n - 1)
  for i in range(n):
   last_list.append(evg)
  last_list.append(num % (n - 1))
 print(last_list)
 # return last_list
 with open(file_path, 'rb') as path:
  for i in range(n):
   # 创建临时文件
   tmp_file = file_dir + str(i) + '.txt'

   file = open(tmp_file, 'wb')
   for j in range(int(last_list[i])):
    line = path.readline()
    file.write(line)
    print(line)
  
   file.close()

def merge( mylist1, mylist2, file1):
 while len(mylist1) > 0 and len(mylist2) > 0:
  if mylist1[0]<mylist2[0]:
   with open(file1,'a') as file:
    file.write(str(mylist1[0]))
    del mylist1[0]
  elif mylist1[0] > mylist2[0]:
   with open(file1,'a') as file:
    file.write(str(mylist2[0]))
    del mylist2[0]
  else:
   with open(file1,'a') as file:
    file.write(str(mylist1[0]))
    file.write(str(mylist2[0]))
    del mylist1[0]
    del mylist2[0]
 with open(file1, 'a') as file:
  for i in mylist1:
   file.write(str(i))
  for i in mylist2:
   file.write(str(i))

