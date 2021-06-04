#! -*- coding: UTF8 -*-
from wordcut import Wordcut
if __name__ == '__main__':
    with open('dict.txt', encoding="UTF-8") as dict_file:
        word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
        wordcut = Wordcut(word_list)
        print(wordcut.tokenize("ขอเรียนเชิญท่านผู้ทรงคุณวุฒิเข้าร่วมการวิพากษ์หลักสูตร"))
        print(wordcut.tokenize("นเชิญท่านผู้ทรงคุณวุฒิเข้าร่วมการวิพากษ์หลักสูตร"))
