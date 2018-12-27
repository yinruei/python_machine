movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
# for each_item in movies:
#     if isinstance(each_item, list):
#         for nested_item in each_item:
#             if isinstance(nested_item, list):
#                 for deeper_item in nested_item:
#                     if isinstance(deeper_item, list):
#                         for deepest_item in deeper_item:
#                             print(deepest_item)
#                     else:
#                         print(deeper_item)
#             else:
#                 print(nested_item)
#     else:
#         print(each_item)

#----------------------------------------------------------
'''上面的方法改用涵式寫法，變得超精簡不累贅 
'''
'''
這個函數的作用是打印列表，其中有可能包含(也可能不包含)嵌套列表
'''
import sys
def print_lol(the_list, indent=False, level=0, fn=sys.stdout):
    '''
    這個函數取一個位置參數，名為"the_list"，這可以是任何python列表(也可以是包含千套列表的列表)。
    所指定的列表中的每個數據項會(遞迴地)輸出到螢幕上，各數據項各占一行。
    '''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fn)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end="", file=fn)
            print(each_item, file=fn)

# print_lol(movies, 0)
# print('======================================================')
# print_lol(movies, True, 0)
# print('======================================================')
# print_lol(movies, True, 1)