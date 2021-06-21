#! -*- coding: UTF8 -*-
from wordcut import Wordcut
if __name__ == '__main__':
    with open('bigthai.txt', encoding="UTF-8") as dict_file:
        word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
        wordcut = Wordcut(word_list)
    #wordcut = Wordcut.bigthai()
    print(wordcut.tokenize("ภาควิชาวิศวกรรมคอมพิวเตอร์"))
    print(wordcut.tokenize("ขอความอนุเคราะห์สถานที่จัดโครงการประชุมสัมมนาวิชาการ “วิทยาการคำนวณและสารสนเทศศาสตร์"))
    print(wordcut.tokenize('คณบดีคณะวิศวกรรมศาสตร์'))
    print(wordcut.tokenize('๐ ๒๗๙๗ ๐๙๙๙  ต่อ ๑๔๐๓ - ๑๔๐๔'))
