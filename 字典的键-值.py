
###字典的创建和访问
alien_o = {'color':'green', 'points':5}
#字典是一系列键，值对的集合。键必须是唯一的，值可以取任何数据类型。字典用大括号{}
#表示，键和值之间用冒号：分隔。键和值用逗号隔开。

#访问字典中的值
print(alien_o['color'])  #输出：green

new_points = alien_o['points']
print("你获得了"+str(new_points)+"个点")

##修改字典的值
#添加键-值对（字典是一种动态结构，可随时在其中添加键-值对）
#添加键-值对，可依次指定字典名，用方括号括起的键和相关联的值

alien_o['x_position']=0  #添加坐标X
alien_o['y_position']=25 #添加坐标Y
print(alien_o)


##修改字典中的值
#可依次指定字典名，用方括号括起的键以及与该键相关联的新值

alien_o ['color'] = 'red'
print("这个外星人现在的颜色是" + alien_o['color'] +"。")
print(alien_o)

##删除键-值对 可使用del语句将相应的键-值对彻底删除
#del语句必须指定的字典名和要删除的键

##{'color': 'red', 'points': 5, 'x_position': 0, 'y_position': 25}

del alien_o['points']
print(alien_o)
##{'color': 'red', 'x_position': 0, 'y_position': 25}
#删除的键-值对永远消失


###遍历字典 

## 遍历所有的键-值对  items（）
favorite_languages ={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
#键是名字，值是语言  用for循环进行遍历先声明键-值两个变量  
#for name ,language in favorite_languages.items():
   # print(name.title() + "'s favorite language is" + language.title() +".")


##遍历字典中的所有键  keys() 并非只能用于遍历；它返回一个列表，其中包含字典中的所有键
 
#for name in favorite_languages.keys():
    #提取字典favorite_languages中的所有键，并依次将它们存储到变量name中
    #print (name.title())


## 按顺序遍历字典中的所有键
# sorted()函数是获得按特定的顺序排列的键列表的副本

#for name in sorted (favorite_languages.keys()):
    
    #print (name.title() +", thank you for taking the poll.")

## 遍历字典中的所有值
# values()函数返回一个值列表，而不包含任何键
# set()集合 剔除字典中的重复项
print("The following languages have been mentioned:")
#for languages in favorite_languages.values():

    #提取字典中的每一个值，并将存储到变量languages中
    #print(languages.title())


#for languages in set(favorite_languages.values()):
    #调用set()，提取出列表独一无二的元素，并创建一个集合

    #print(languages.title())

