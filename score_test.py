from os import replace
from Levenshtein import editops
from manTextV4 import main_mantext

def read_key(File):
    my_file = open('docs_source/'+File+'_key.txt', "r")
    content = my_file.read()
    content_list = content.split(",")
    my_file.close()    
    return content_list

def recall(test,Insert,Replace):
    return (len(test)-Insert-Replace)/len(test)

def precision(test,source,Insert,Replace):
    return (len(test)-Insert-Replace)/len(source)

def cal_score(test,source):
    if test == ' ' or source == ' ':
        return 0.0,0.0
    t = editops(test,source)
    print(t)
    Insert,Delete,Replace = 0,0,0
    for ele in t:
        Insert += ele.count('insert')
        Delete += ele.count('delete')
        Replace += ele.count('replace')
    return recall(test,Insert,Replace),precision(test,source,Insert,Replace)

def test_score():
    File = input('please input file: ')
    source = read_key(File)
    data_test = main_mantext('score program',File)
    '''print(f'ส่วนราชการ หรือ ส่วนงาน: {org}')
    print(f'เรื่อง: {topic}')
    print(f'เรียน: {toUser}')
    print(f'โทร: {tel}')
    print(f'วันที่ี: {date}')
    print(f'คนเช็น: {byUser}')'''
    #print(source)
    #print(data_test)
    for i in range(6):
        print(data_test[i],source[i])
        Recall,Precision = cal_score(data_test[i],source[i])
        print(f'recall: {Recall} precision: {Precision}')

test_score()