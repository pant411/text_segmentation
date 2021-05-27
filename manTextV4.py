#! -*- coding: UTF8 -*-
from wordcut import Wordcut
import pylcs

def read_text():
    doc = input("file: ")
    data = open("docs/{}.txt".format(doc),"r")
    return data

def read_dict():
    with open('dict.txt', encoding="UTF-8") as dict_file:
        word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
        wordcut = Wordcut(word_list) 
    return wordcut

def select_tag(indexOFchosen):
    if indexOFchosen <= 1: op = 1 #collect in org
    elif indexOFchosen >= 7: op = 7 #keep in byuser   
    else: op = indexOFchosen
    return op 

def store_tag(op,text,org,tel,topic,toUser,byUser,date,no):
    if op == 1: org.append(text)
    elif op == 2: topic.append(text)
    elif op == 3: toUser.append(text)
    elif op == 4: date.append(text)
    elif op == 5: tel.append(text)
    elif op == 6: no.append(text)
    elif op >= 7: byUser.append(text)
    return org,tel,topic,toUser,byUser,date,no

def read_keyword():
    my_file = open("keyword.txt", "r")
    content = my_file.read()
    content_list = content.split(",")
    my_file.close()    
    return content_list

def test_tag(ele,tag1,tag2,tag3):
    if 'ภาควิชา' in ele: tag1.append(ele)
    if 'คณะ' in ele: tag2.append(ele)
    if 'มหาวิทยาลัย' in ele: tag3.append(ele)    
    return tag1,tag2,tag3

def main():
    data = read_text()
    keyword = read_keyword()
    line_no = 0
    org,tel,topic,toUser,byUser,date,no = [],[],[],[],[],[],[] #org=ส่วนงานหรือส่วนราชการ tel=เบอร์โทร topic=เรื่อง toUser=เรียน byUser=คนเซ็น date=วันที่ no=ที่ศธ
    tag1,tag2,tag3 = [],[],[] #tag1=ภาค tag2=คณะ tag3=มหาวิทยาลัย
    wordcut = read_dict()
    for line in data.readlines():
        res = ''
        inline = wordcut.tokenize(line)
        inline = list(map(lambda s: s.strip(), inline))
        inline.append('\n')
        lock_store = True #initial value
        op = -1
        for ele in inline:
            candidate = pylcs.lcs_of_list(ele,keyword)
            chosen = max(candidate)
            indexOFchosen = candidate.index(chosen)
            tag1,tag2,tag3 = test_tag(ele,tag1,tag2,tag3)
            if (abs(len(keyword[indexOFchosen]) - chosen) <= 2) or '\n' in ele:
                if (lock_store == False and line_no > 0) or '\n' in ele:      
                    org,tel,topic,toUser,byUser,date,no = store_tag(op,res,org,tel,topic,toUser,byUser,date,no)
                    res = ''
                    lock_store = True
                if lock_store == True and '\n' not in ele:
                    op = select_tag(indexOFchosen)
                    lock_store = False
                line_no += 1
                continue             
            if lock_store == False and ele != ')':
                res = res + ele
                if (op == 7 or op == 4):
                    res += ' '
        line_no += 1  
    print(f'org: {org}')
    print(f'topic: {topic}')
    print(f'toUser: {toUser}')
    print(f'byUser: {byUser}')
    print(f'tel: {tel}')
    print(f'date: {date}')
    print(f'no: {no}')
    print(f'tag1: {tag1},tag2: {tag2},tag3: {tag3}')  
    #print(org[0],topic[0],toUser[0],tel[0],date[0])   
    index_org = 0
    '''if temp1[0] not in org[0]:
        org.append(temp1[0])
        index_org = len(org)-1
    if temp3[0] not in org[0]:
        org.append(temp3[0])
        index_org = len(org)-1 '''
    if len(org) == 0:
        org.append("ไม่พบข้อมูล")
    if len(topic) == 0:
        topic.append("ไม่พบข้อมูล")
    if len(toUser) == 0:
        toUser.append("ไม่พบข้อมูล")
    if len(byUser) == 0:
        byUser.append("ไม่พบข้อมูล")
    if len(tel) == 0:
        tel.append("ไม่พบข้อมูล")
    if len(date) == 0:
        date.append("ไม่พบข้อมูล")
    if len(no) == 0:
        no.append("ไม่พบข้อมูล")
    print(f'ส่วนราชการ หรือ ส่วนงาน: {org[index_org]}')
    print(f'เรื่อง: {topic[0]}')
    print(f'เรียน: {toUser[0]}')
    print(f'โทร: {tel[0]}')
    print(f'วันที่ี: {date[0]}')
    print(f'คนเช็น: {byUser[-1]}')
    print(f'ที่: {no[0]}')

main()