# 5-3 外星人颜色：假设在游戏中刚杀了一个外星人，请创建一恶搞名为alien_color的变量，
#   并将其设置为‘green’，‘yellow’，‘red‘
#编写一条if语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了5个点
'''
alien_color = 'yellow'
if alien_color == 'green':
    print('恭喜成功击杀绿色外星人，获得5个积分')
elif alien_color == 'yellow':
    print('恭喜成功击杀黄色外星人，获得10个积分')
else :
    print('恭喜成功击杀红色外星人，获得15个积分')

'''
'''
#5-6 人生的不同阶段：设置变量age的值，在编写一个if-elif-else的结构，根据age的值判断处于人生的哪一个阶段
#如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿
age = 79
if age < 2:
    print('这个人是小baby') # age<2岁，是婴儿

#如果一个人的年龄为2（含）～4岁，就打印一条消息，指出他正在蹒跚学步
elif 2<=age<4:
    print('这个正在蹒跚学步')

#如果一个人的年龄为4（含）～13岁，就打印一条消息，指出他是儿童
elif 4<=age<13:
    print ('这个人是儿童')

#如果一人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年
elif 13<=age<20:
    print('这个人是青少年')

#如果一个的年龄为20（含）～65岁，就打印一条信息，指出他是成年人
elif 20<=age<65:
    print('这个人是成年人')

#如果一个人的年龄超过65（含）岁，就打印一条消息，指出他是老年人
else :
    print('这个人是老年人')
'''

#5-7 喜欢的水果：创建一个列表，其中包含你喜欢的水果，在编写一系列独立的if语句，检查列表中是否包含特定的水果
#将该列表命名为favourite_fruits,并在其中包含三种水果
#编写5条if语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，就打印一条消息，如“You really like bananas!"
'''
favourite_fruits = ['apple','cantaloupe','bananas']
if 'apple' in favourite_fruits:
    print('You really like apples!')
if 'cantaloupe' in favourite_fruits:
    print('You really like cantaloupe!')
if 'bananas' in favourite_fruits:
    print('You really like bananas!')
    
'''
###5.4.2确定列表不是空的
###下面在制作比萨前检查顾客点的配料列表是否为空。如果列表是空的，就向顾客确认他是否
###要点普通比萨；如果列表不为空，就像前面的示例那样制作比萨
'''
requested_toppings = []
#创建一个空列表，表示顾客还没有点任何配料
if requested_toppings: #检查列表是否为空Python将在列表
    #至少包含一个元素时返回True，并在列表为空时返回False
    
    for requested_topping in requested_toppings:
         #如果requested_toppings不为空，就运行与前一个示例相同的for循环
        print("Adding" + requested_topping + ".")
    print("\nFinished making your pizza!")
#否则，就打印一条消息，询问顾客是否确实要点不加任何配料的普通比萨

else:#列表为空，因此输出：询问顾客是否确实点普通披萨
    print("Are you sure you want a plain pizza?")
'''

###5.4.3使用多个列表
###顾客的要求往往五花八门，在比萨配料方面尤其如此。如果顾客要在比萨中添加炸薯条，该怎么办呢？可使用列表和if语句来确定能否满足顾客的要求
###下面的示例定义了两个列表，其中第一个列表包含比萨店供应的配料，而第二个列表包含顾客点的配料。
###这次对于requested_toppings中的每个元素，都检查它是否是比萨店供应的配料，再决定是否在比萨中添加它

avalable_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
#定义一个包含比萨店供应的固定配料的列表

requested_toppings = ['mushrooms','french fries','extra cheese']
#再创建一个包含顾客点的配料的列表，‘french fries'是顾客点的配料，不包含在avalable_toppings中

for requested_topping in requested_toppings:
#遍历顾客点的每个配料
    if requested_toppings in avalable_toppings: #如果顾客点的配料在披萨店的供应列表中，就添加到披萨中
        print("Adding "+ requested_topping + ".")
    
    else: # 如果顾客点的配料不在披萨店的供应列表中，就打印一条消息，告诉顾客不供应这种配料
        print("Sorry,we dont't have " + requested_topping +".")

print("\nFinished making your pizza!")


