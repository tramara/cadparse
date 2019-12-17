'''
pdftxt()用来将pdf文件转换问txt文件
'''

# -*-coding:UTF-8 -*-

import re
import sys
import os
import csv
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed




def pdftxt(pdffile, inpath):

    filename = os.path.basename(pdffile).strip('.pdf')

    tagfilename = inpath + '\\' + filename + '.txt'

    fp = open(pdffile, 'rb')
    # 用文件对象来创建一个pdf文档分析器
    praser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器 与文档对象
    praser.set_document(doc)
    doc.set_parser(praser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 循环遍历列表，每次处理一个page的内容
        for page in doc.get_pages():  # doc.get_pages() 获取page列表
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
            i = 0
            for x in layout:
                # print("x的类型是：" , type(x),"x是：", x)
                if isinstance(x, LTTextBoxHorizontal):
                    # 需要写出编码格式
                    with open(tagfilename, 'a', encoding='utf-8') as f:
                        results = x.get_text()
                        if i == 0:
                            pass
                        # 删除页眉内容
                        elif re.findall('第 . 页 共 . 页 ', results):
                            pass
                        # 删除页脚内容
                        else:
                            f.write(results)
                i +=1
    return tagfilename
