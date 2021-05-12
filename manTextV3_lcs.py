#! -*- coding: UTF8 -*-
from wordcut import Wordcut
import pylcs

#keyword = ['ส่วนราชการ','ที่','เรื่อง','วันที่','โทร.','ส่วนงาน','(นาย','(นาง','(นางสาว','(รศ. ดร.',
# '(รองศาสตราจารย์ ดร.','(น.ส.','(รองศาสตราจารย์','(ผู้ช่วยศาสตราจารย์ ตร.','(ผศ. ดร.','(รศ.คร.','(ผศ.ดร.']

def spellcheck(text):
    #text = open("/home/ppunn/public_html/ocr/docs/{}.txt".format(filename), "r",encoding="utf-8") #input file 
    #res = ''
    newres = ''
    '''for word in text:
        res+=word
    text.close()'''
    #print(res)
    a = text
    #print("a: ",a)
    for i in range(len(a)):
        if a[i] == '\n' or a[i] == '(' or a[i] == ')' or a[i] == '.' or a[i] == '-' or a[i] == '"' or a[i] == '\\' or a[i] == ' ':
            continue 
        if a[i]=='เนิน' and a[i-1]!='ดำ':
            a[i]='ดำเนิน'
            a[i-1]=''
        if a[i]=='ดำ' and a[i+1]!='เนิน':
            a[i]='ดำเนิน'
            a[i+1]=''
        if a[i]=='ฮิ' or a[i]=='นย' or a[i]=='อ.':
            a[i]=''
        if a[i]=='ทะ' and a[i+1]!='เบียน':
            a[i]='ทะเบียน'
            a[i+1]=''
        if a[i]=='นรา' and (a[i+1]=='ชกา' or a[i+1]=='ชการ'):
            a[i]='ส่วนงานราชการ'
            a[i+1]=''
            if a[i+2]=='ร':
                a[i+2]=' '
        if a[i]=='เพ' and a[i+1]!='ิ่ม':
            a[i]='เพิ่ม'
            a[i+1]=''
        if a[i]=='งาน' and a[i+1]=='ภาควิชา' and a[i-1]!='ส่วน':
            a[i-1]='ส่วน'
        if a[i]=='อนุ' and a[i+1]!='ญาต' and a[i+1]!='มัติ':
            a[i]='อนุญาต'
            a[i+1]=''
        if a[i]=='ศูนย':
            a[i]='ศูนย์'
        if a[i]=='หรับ' and a[i-1]!='สำ':
            a[i-1]='สำหรับ'
            a[i]=''
        if a[i]=='สิต' and a[i-1]!='นิ':
            a[i-1]='นิสิต'
            a[i]=''
        if a[i]=='ดิ' and a[i+1]=='จิ' and a[i+2]!='ทัล':
            a[i]='ดิจิทัล'
            a[i+1]=''
            a[i+2]=''
        if a[i]=='ชา' and a[i+1]=='การ' and a[i-1]!='วิ':
            a[i]='วิชาการ'
            a[i+1]=' '
            a[i-1]=''
        if a[i]=='สงค์' and a[i-1]!='ประ':
            a[i]='ประสงค์'
            a[i-1]=''
        if a[i]=='พา' and a[i+1]=='ะ':
            a[i-1]='เฉพาะ'
            a[i]=''
            a[i+1]=''
        if a[i]=='ก' and a[i+1]=='ก่า':
            a[i]='กล่า'
            a[i+1]=''
        if a[i]=='บา':
            a[i]='ษา'
        if a[i]=='รดี' and a[i+1]=='ก':
            a[i]='รศึก'
            a[i+1]=''
        if a[i]=='หน้า' and a[i+1]=='ภาควิชา':
            a[i-1]=') หัว'
        if a[i]=='ยิน' and a[i+1]!='ยอม' and a[i+1]!='ดี':
            a[i]='ยินยอม'
            a[i+1]=''
        '''if a[i]=='รวิ' and a[i+1]!='จัย':
            a[i]='รวิจัย'
        '''
        if a[i]=='.ครง':
            a[i]='ในโครง'
        if a[i]=='ราญ' and a[i+1]=='การ':
            a[i]='ราช'
        if a[i]=='มืถุ' and a[i+1]=='นาย' and a[i+2]=='น':
            a[i]='มิถุนายน'
            a[i+1]=''
            a[i+2]=''
        if a[i]=='โร' and a[i+1]=='ด':
            a[i]='โปรด'
            a[i+1]=''
        if a[i]=='สนับ' and a[i+1]!='สนุน':
            a[i]='สนับสนุน'
            a[i+1]=''
        '''if a[i]=='วิ' and a[i+1]!='จัย':
            a[i]='วิจัย'
        '''
        if a[i]=='โครง' and a[i+1]!='การ':
            a[i]='โครงการ'
            a[i+1]=''
        if a[i]=='ครง':
            a[i]='โครง'
        if a[i]=='จัย' and a[i-1]!='วิ':
            a[i]='วิจัย'
            a[i-1]=''
        if a[i]=='ข้อ' and a[i+1]!='มูล':
            a[i]='ข้อมูล'
            a[i+1]=''
    for i in a:
        #print(i,end='')
        newres+=i
    #print(newres)
    return newres

def main():
    doc = input("file: ")
    data = open("docs/{}.txt".format(doc),"r")
    org,tel,topic,toUser,byUser,date,no = [],[],[],[],[],[],[] #org=ส่วนงานหรือส่วนราชการ tel=เบอร์โทร topic=เรื่อง toUser=เรียน byUser=คนเซ็น date=วันที่ no=ที่ศธ
    #check1,check2,check3,check4,check5,check6 = False,False,False,False,False,False
    keyword = ['ส่วนราชการ','ส่วนงาน','เรื่อง','เรียน','วันที่','โทร.','ที่','(นาย','(นาง','(นางสาว','(รศ. ดร.',
                '(รองศาสตราจารย์ ดร.','(น.ส.','(รองศาสตราจารย์','(ผู้ช่วยศาสตราจารย์ ตร.','(ผศ. ดร.','(รศ.คร.','(ผศ.ดร.']
    #check_keyword = True # true->enable false->disable
    line_no = 0
    temp1 = [] #ภาค
    temp2 = [] #คณะ 
    with open('dict.txt', encoding="UTF-8") as dict_file:
        word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
        wordcut = Wordcut(word_list)
        for line in data.readlines():
            res = ''
            inline = wordcut.tokenize(line)
            inline = list(map(lambda s: s.strip(), inline))
            inline.append('\n')
            lock_keep = True #initial value
            op = -1
            for ele in inline:
                candidate = pylcs.lcs_of_list(ele,keyword)
                chosen = max(candidate)
                indexOFchosen = candidate.index(chosen)
                if 'ภาค' in ele: temp1.append(ele)
                if 'คณะ' in ele: temp2.append(ele)
                if (abs(len(keyword[indexOFchosen]) - chosen) <= 2 and chosen > 0) or '\n' in ele:
                    #print(f'candidate is {candidate}, chosen is {chosen}, index is {indexOFchosen}, text is {keyword[indexOFchosen]}')
                    #print(f'chosen: {inline}, {keyword[indexOFchosen]}')
                    print(f'ele: {ele}')
                    if (lock_keep == False and line_no > 0) or '\n' in ele: 
                        #print(f'op: {op}, res: {res}')        
                        if op == 1: 
                            org.append(res)
                        elif op == 2: 
                            topic.append(res)
                        elif op == 3: 
                            toUser.append(res)
                        elif op == 4: 
                            date.append(res)
                        elif op == 5: 
                            tel.append(res)
                        elif op == 6: 
                            no.append(res)
                        elif op >= 7:
                            byUser.append(res)
                        res = ''
                        lock_keep = True
                    if lock_keep == True and '\n' not in ele:
                        #print('gayray') 
                        if indexOFchosen == 0 or indexOFchosen == 1: 
                            op = 1 #collect in org
                        elif indexOFchosen == 2: 
                            op = 2 #keep in topic
                        elif indexOFchosen == 3: 
                            op = 3 #keep in toUser
                        elif indexOFchosen == 4: 
                            op = 4 #keep in date
                        elif indexOFchosen == 5: 
                            op = 5 #keep in tel
                        elif indexOFchosen == 6: 
                            op = 6 #keep in no
                        elif indexOFchosen >= 7: 
                            op = 7 #keep in byuser
                        lock_keep = False
                    line_no += 1
                    continue             
                if lock_keep == False and ele != ')':
                    res = res + ele
                    if (op == 7 or op == 4):
                        res += ' '
                #print(f'op: {op}, res: {res}')
            line_no += 1  
    print(org,topic,toUser,byUser,tel,date,no)  
    print(temp1,temp2)  
    #print(org[0],topic[0],toUser[0],tel[0],date[0])   
    if len(org) == 0:
        if len(temp1) > 0: org.append(temp1[0])
        else: org.append("ไม่พบข้อมูล")
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
    print(f'ส่วนราชการ หรือ ส่วนงาน: {org[0]}')
    print(f'เรื่อง: {topic[0]}')
    print(f'เรียน: {toUser[0]}')
    print(f'โทร: {tel[0]}')
    print(f'วันที่ี: {date[0]}')
    print(f'คนเช็น: {byUser[-1]}')
    print(f'ที่: {no[0]}')

main()