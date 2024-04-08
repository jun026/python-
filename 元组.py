'''
python的元组的元素不能修改
元组使用小括号，又逗号来分隔
如果需要修改元组中的元素，可以先将元组转换为列表，修改列表中的元素，然后再将列表转换成元组
'''

#my_tuple = ([1,2,3])
#print(my_tuple)#输出:1,2,3
#print(my_tuple[1])  # 2
'''
使用索引访问元素，元组中的元素可以通过索引来访问，索引从0开始，表示元组中的第一个元素
'''
#print(my_tuple[0:1])  # 步长为1 输出：3
#print(my_tuple[0:2])  # 步长为2 输出：3，4
#print(my_tuple[0:3])  # 步长为3 输出：3，4，5
'''
使用切片访问元素，可以使用切片来访问元组中多个元素
切片使用 start:stop:step的形式，但包含stop，步长为step
'''
#t=(1,2,3,4,5)   
#print(t[1:4])  # 2,3,4  ????？
#print(t[1:2])

#使用负索引访问元素，可以使用负索引来从元组的末尾开始访问元素
#print(my_tuple[-1])   # 3

#### 练习python
###5-8 以特殊方式跟管理员打招呼：创建一个至少包含5个用户名的列表，且其中一个用户名为‘admin’。
###想想你要编写代码，在每位用户登陆网站后都打印一条问候消息。遍历用户名列表，并向每位用户打印一条问候消息。
 
## 如果用户名为‘admin’，就打印一条特殊的问候消息，如“Hello admin, would you like to see a status report?"
## 否则，打印一条普通的问候消息，如“Hello Eric, thank you for logging in again."

##usenames = ['Alice','Bob','Eric','admin','David']
'''for usename in usenames:
    print("Hello" + usename.title() + ", thank you for logging in again." + "\n")

    if usename =='adimin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello Eric, thank you for logging in again.")
'''


###5-9 处理没有用户的情形：在完成练习5-8编写的程序中 添加一条if语句，检查用户名列表是否为空
## 如果为空，就打印消息"We need to find some uses!"
## 删除列表中的所有用户名，确定将打印正确的消息
'''
usenames = ['Alice','Bob','Eric','admin','David']
if usenames:
    for usename in usenames:
       print("Hello" + usename.title() + ", thank you for logging in again.")

else:
    print("We need to find some uses!")
    
    
if not usenames:del usenames
print("已删除列表中的所有用户名，列表为空")
 '''         
###5-10 检查用户名：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都是唯一的。
## 创建一个至少包含5个用户名的列表，并将其命名为current_users。
## 再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users中。
##遍历列表new_users,对于其中的每个人用户名，都检查它是否已被使用。
# 如果是这样，就打印一条消息，指出需要输出别的用户名； 否则，打印一条消息，指出这个用户名未被使用。
##确保比较是不区分大小写；换句话说，如果用户名‘John’已被使用，应拒绝用户名‘JOHN’。

current_users = ['Alice','Bob','Eric','admin','David']
new_users = ['jun','Tom','Alice','Mike','David']

for new_users in new_users:
    if new_users in current_users:
        print("用户名已被使用请使用其他用户名")
    
    else:
        print("用户名可用")


### 5-11序数：序数表示位置，如1st 和2nd。大多数序数都以th结尾，只有1、2和3例外。
## 在一个列表中存储数字1～9
## 遍历这个列表
## 在循环中使用一个if-elif-else语句，以打印每个数字对应的序数。输出内容为“数字+序数”，但每个序数都独占一行。

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(str(number)+"st")

    elif number ==2:
        print(str(number)+"nd")
    
    elif number ==3:
        print(str(number)+"rd")

    else:
        print(str(number)+"th")

