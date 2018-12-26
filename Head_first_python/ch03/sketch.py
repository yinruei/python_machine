# import os
# if os.path.exists('sketch.txt'):
#     data = open('sketch.txt')

#     for each_line in data:
#         if not each_line.find(':') == -1:#如果字串中找不到冒號就會等於-1，但是前面有not，所以找到冒號就會運行下面代碼
#             (role, line_spoken) = each_line.split(':',1)
#             print(role, end='')
#             print(' said: ', end='')
#             print(line_spoken, end='')

#     data.close()
# else:
#     print('The data file os missing!')
# 
'''
首先導入os涵式庫，然後使用"path.exists"來確保數據文件存在，
在此之後才會嘗試打開這個數據文件。然後處理文件中的每一行，
不過只是在確定數據行符合所需的格式之後才進行處理，這是通過數據行中是否有一個":"
字符來做到的。如果到了":"，則處理這個數據行，否則就將這個數據行忽略。所有工作完成時，
關閉數據文件。如果文件未找到，最後你會得到一個友好的消息。
'''
# 以上方法雖然可以成功，但是若條件不同就要重新判斷，會變得較為複雜，所以這方法較脆弱

# ===========================================================================
try:
    data = open('sketch.txt')
    
    for each_line in data:
        try:
            if not each_line.find(':') == -1:#如果字串中找不到冒號就會等於-1，但是前面有not，所以找到冒號就會運行下面代碼
                (role, line_spoken) = each_line.split(':',1)
                print(role, end='')
                print(' said: ', end='')
                print(line_spoken, end='')
        except ValueError:
            pass#pass語句就是python的空語句或null語句，他什麼也不做。

    data.close()
except IOError:
    print('The data file is missing!')
'''
代碼一打開一個數據文件，處理這個文件中的各個數據行，抽取出感興趣的數據，
並顯示在屏幕上。完成後關閉文件。如果出現任何異常，這個代碼會進行處理。
'''