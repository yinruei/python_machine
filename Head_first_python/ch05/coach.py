
# with open('james.txt','r') as james_file:
#     data = james_file.readline()
# james = data.strip().split(',')
# '''
# 先去除自符串中所有不想要的空白符。
# 之後，去除了空白符的結果由第二個方法split(',')，
# 這會創建一個列表
# '''

# with open('julie.txt','r') as julie_file:
#     data = julie_file.readline()
# julie = data.strip().split(',')

# with open('mikey.txt','r') as mikey_file:
#     data = mikey_file.readline()
# mikey = data.strip().split(',')

# with open('sarah.txt','r') as sarah_file:
#     data = sarah_file.readline()
# sarah = data.strip().split(',')

'''
把4個with語句改為一個涵式
'''
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return (data.strip().split(','))
    except IOError as err:
        print('File error: '+str(err))
        return None

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

# # print(clean_james)
# # print(james)
# # print(julie)
# # print(mikey)
# # print(sarah)

# # print(sorted(james))
# # print(sorted(julie))
# # print(sorted(mikey))
# # print(sorted(sarah))

def sanitize(time_string):

    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)

    (mins, secs) = time_string.split(splitter)

    return (mins + '.' +secs)

# # clean_james = []
# # clean_julie = []
# # clean_mikey = []
# # clean_sarah = []

# # for each in james:
# #     clean_james.append(sanitize(each))
# # for each in julie:
# #     clean_julie.append(sanitize(each))
# # for each in mikey:
# #     clean_mikey.append(sanitize(each))
# # for each in sarah:
# #     clean_sarah.append(sanitize(each))
    
# # # print(sorted(clean_james, reverse=True))
# # print(sorted(clean_james))
# # print(sorted(clean_julie))
# # print(sorted(clean_mikey))
# # print(sorted(clean_sarah))
# '''
# 上面的方法比較為詳細，但很多重複的部分，
# 下面也是完成同樣的功能，這包括創建一個新列表，
# 為此要指定將應用到一個現有列表中各個數據項的轉換。
# '''

# # clean_mikey = [sanitize(each) for each in mikey]
# # print(sorted(clean_mikey))

# '''
# 再簡化如下.....
# '''

# # clean_mikey = sorted(sanitize(each) for each in mikey)
# # print(clean_mikey)

# # print(sorted([sanitize(each) for each in james]))
# # print(sorted([sanitize(each) for each in julie]))
# # print(sorted([sanitize(each) for each in mikey]))
# # print(sorted([sanitize(each) for each in sarah]))



# '''
# 先判斷列表中有沒有重複的數據，將沒有重複的丟到新的列表
# 最後再取前三名的資料
# '''
# # james = sorted([sanitize(each) for each in james])
# # julie = sorted([sanitize(each) for each in julie])
# # mikey = sorted([sanitize(each) for each in mikey])
# # sarah = sorted([sanitize(each) for each in sarah])

# # unique_james = []

# # for each in james:#再現有數據迭代處理
# #     if  each not in unique_james:#如果這個數據項還不再新列表中
# #         unique_james.append(each)#將這個唯一的數據項追加到新列表中
# # print(unique_james[0:3])

# # unique_julie = []
# # for each in julie:
# #     if each not in unique_julie:
# #         unique_julie.append(each)
# # print(unique_julie[0:3])

# # unique_mikey = []
# # for each in mikey:
# #     if each not in unique_mikey:
# #         unique_mikey.append(each)
# # print(unique_mikey[0:3])

# # unique_sarah = []
# # for each in sarah:
# #     if each not in unique_sarah:
# #         unique_sarah.append(each)
# # print(unique_sarah[0:3])



'''
上面再簡化
'''

james = sorted(set([sanitize(each) for each in james]))[0:3]
julie = sorted(set([sanitize(each) for each in julie]))[0:3]
mikey = sorted(set([sanitize(each) for each in mikey]))[0:3]
sarah = sorted(set([sanitize(each) for each in sarah]))[0:3]
print(james)
print(julie)
print(mikey)
print(sarah)