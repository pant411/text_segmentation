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
    if indexOFchosen <= 1: op = 1 #store in org
    elif indexOFchosen >= 7: op = 7 #store in byuser   
    else: op = indexOFchosen #
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


def org_tag(ele,tag1):
    x_tag1 = ele.find('ภาควิชา')
    x_tag2 = ele.find('คณะ')
    x_tag3 = ele.find('มหาวิทยาลัย')
    x_tag4 = ele.find('สถาน')
    x_tag5 = ele.find('สำนัก')
    x_tag6 = ele.find('สภา')
    x_tag7 = ele.find('กรม')
    x_tag8 = ele.find('กอง')
    res = ''
    if x_tag1 != -1: res = ele[x_tag1:len(ele)-1]
    elif x_tag2 != -1: res = ele[x_tag2:len(ele)-1]
    elif x_tag3 != -1: res = ele[x_tag3:len(ele)-1]
    elif x_tag4 != -1: res = ele[x_tag4:len(ele)-1]
    elif x_tag5 != -1: res = ele[x_tag5:len(ele)-1]
    elif x_tag6 != -1: res = ele[x_tag6:len(ele)-1]
    elif x_tag7 != -1: res = ele[x_tag7:len(ele)-1]
    elif x_tag8 != -1: res = ele[x_tag8:len(ele)-1]
    space = res.find(' ')
    if space != -1:
        res = res[:space]
    if res != '':
        tag1.append(res)
    return tag1
 
def score_test():
    data = read_text()


def main():
    data = read_text()
    keyword = read_keyword()
    line_no = 0
    org,tel,topic,toUser,byUser,date,no = [],[],[],[],[],[],[] #org=ส่วนงานหรือส่วนราชการ tel=เบอร์โทร topic=เรื่อง toUser=เรียน byUser=คนเซ็น date=วันที่ no=ที่ศธ
    tag1,tag2,tag3 = [],[],[] #tag1=ภาค tag2=คณะ tag3=มหาวิทยาลัย
    wordcut = read_dict()
    for line in data.readlines():
        res = ''
        tag1 = org_tag(line,tag1)
        inline = wordcut.tokenize(line)
        inline = list(map(lambda s: s.strip(), inline))
        inline.append('\n')
        lock_store = True #สถานะการเก็บข้อมูลลงlist
        op = -1
        for ele in inline:
            candidate = pylcs.lcs_of_list(ele,keyword)
            chosen = max(candidate)
            indexOFchosen = candidate.index(chosen)
            if (abs(len(keyword[indexOFchosen]) - chosen) <= 2) or '\n' in ele or ele in keyword:
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
                if ('ดร' in ele or 'ดร.' in ele or 'ตร.' in ele or 'ตร' in ele or ele == ' ') and op == 7: continue
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