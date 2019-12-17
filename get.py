'''
该函数用来提取适航指令文件当中的主要参数
适航指令编号，修正案号，适用性，适用机型，适用发动机型号，适用部件件号，适航指令正文部分，生效日期，发布日期，联系人
定义函数如下：
cadno()用来获得适航指令编号；
amendno()用来获得适航指令修正案号；
app()用来获得适航指令适用性；
model()用来获得适用该适航指令的飞机机型；
engine()用来获得适用该适航指令的发动机型号；
pn()用来获得适用该适航指令的部件件号；
ref()用来获得适航指令的参考文件；
text()用来获得适航指令的正文部分；
effdate()用来获得适航指令的生效日期；
pubdate()用来获得适航指令的发布日期；
author()用来获得适航指令的联系人；
'''

import re
# 导入re函数

def cadno(dir):
    # 定义函数 cadno()，dir为文本目录，格式为txt文本
    document = open(dir, 'r', encoding='utf-8')
    # 以UTF-8的字体格式打开目录中文本
    doc = document.read()
    # 获取文本中的文本内容
    eyebow = re.findall("(编号：.*)\n一. 标题：", doc, re.S)
    # 得到页眉部分
    cadno = re.findall("编号：(.*)修正案号", eyebow[0])
    # 从页眉部分获得文本的适航指令编号
    cadno[0] = cadno[0].strip()
    # 去除适航指令编号中的多余空格及换行
    return cadno[0]
    # 返回适航指令编号

def amendno(dir):
    # 定义函数 amendno()，dir为文本目录，格式为txt文本
    document = open(dir, 'r', encoding='utf-8')
    # 以UTF-8的字体格式打开目录中文本
    doc = document.read()
    # 获取文本中的文本内容
    eyebow = re.findall("(编号：.*)\n一. 标题：", doc, re.S)
    # 得到页眉部分
    amendno = re.findall("修正案号：(.*)", eyebow[0])
    # 从页眉部分获得文本的适航指令编号
    amendno[0] = amendno[0].strip()
    # 去除适航指令修正案号中的多余空格及换行
    return amendno[0]
    # 返回适航指令修正案号

def app(dir):
    # 定义函数 app()，dir为文本目录，格式为txt文本
    document = open(dir, 'r', encoding='utf-8')
    # 以UTF-8的字体格式打开目录中文本
    doc = document.readlines()
    # 获取文本中的文本内容
    app_1 = "".join(doc)
    app_orig =  re.findall("二. 适用范围：(.*)三. 参考文件", app_1, re.S)
    # 获取适航指令适用性部分
    app = app_orig[0].split("\n    ")
    # 将字符串中的段落划分出来
    for i in  range(0, len(app)):
        app[i].split()
        # 去除适航指令适用性中的多余空格及换行
    for i in app:
        if i == '' or i.isspace():
            app.remove(i)
        # 如果适航指令适用性为空或者为空格，则将其从列表中删除

    for i in range(0, len(app)):
        app[i] = app[i].replace("\n", "")
    # 去除列表元素中的换行符

    app_end = "\n".join(app)

    return app_end
    # 返回适航指令适用性部分

def ref(dir):
    # 定义函数 ref()，dir为文本目录，格式为txt文本
    document = open(dir, 'r', encoding='utf-8')
    # 以UTF-8的字体格式打开目录中文本
    doc = document.readlines()
    # 获取文本中的文本内容
    ref_1 = "".join(doc)
    ref_orig = re.findall("三. 参考文件：(.*)四. 原因、措施和规定", ref_1, re.S)
    # 获取适航指令参考文件部分
    ref = ref_orig[0].split("\n    ")
    # 将字符串中的段落划分出来
    for i in range(0, len(ref)):
        ref[i].strip()
        # 去除适航指令参考文件中的多余空格及换行
    for i in ref:
        if i == '' or i.isspace():
            ref.remove(i)
        # 如果适航指令参考文件为空格或者为空 则移除列表中元素

    for i in range(0, len(ref)):
        ref[i] = ref[i].replace("\n", "")
    # 去除列表元素中的换行符

    ref_end = "\n".join(ref)

    return ref_end
    # 返回适航指令参考文件部分

def text(dir):
    # 定义函数 text()，dir为文本目录，格式为txt文本

    document = open(dir, 'r', encoding='utf-8')
    # 以UTF-8的字体格式打开目录中文本

    doc = document.readlines()
    # 获取文本中的文本内容
    text_1 = "".join(doc)
    text_orig =  re.findall("四. 原因、措施和规定(.*)五. 生效日期：", text_1, re.S)
    # 获取适航指令正文部分

    text = text_orig[0].split('\n    ')
    # 将字符串中的段落划分出来

    for i in  range(0, len(text)):
        text[i].strip()
    # 去除适航指令正文中的多余空格及换行

    for i in text:
        if i == '' or i.isspace():
            text.remove(i)
    # 如果适航指令正文为空或者为空格，则将其从列表中删除

    for i in range(0, len(text)):
        text[i] = text[i].replace("\n", "")
    # 去除列表元素中的换行符

    text_end = "\n".join(text)

    return text_end
    # 返回适航指令正文部分

def effdate(dir):
    # 定义函数 effdate()，dir为文本目录，格式为txt文本
    document = open(dir, 'r', encoding='utf-8')
    # 以UTF-8的字体格式打开目录中文本
    doc = document.read()
    # 获取文本中的文本内容
    effdate_orig = re.findall("五. 生效日期：(.*)六. 颁发日期：", doc, re.S)
    # 获得生效日期
    effdate_orig[0] = effdate_orig[0].strip()
    # 去除适航指令生效日期中的多余空格及换行
    effdatestr = effdate_orig[0]
    effdate = [effdatestr[0:17].strip()]
    # 截取生效日期前18位字符，获得生效日期
    return effdate[0]
    # 返回适航指令生效日期

def pubdate(dir):
    # 定义函数 pubdate()，dir为文本目录，格式为txt文本
    document = open(dir, 'r', encoding='utf-8')
    # 以UTF-8的字体格式打开目录中文本
    doc = document.read()
    # 获取文本中的文本内容
    pubdate_orig = re.findall("六. 颁发日期：(.*)七. 联系人：", doc, re.S)
    # 获得颁发日期
    pubdate_orig[0] = pubdate_orig[0].strip()
    # 去除适航指令颁发日期中的多余空格及换行
    pubdatestr = pubdate_orig[0]
    pubdate = [pubdatestr[0:17].strip()]
    # 截取颁发日期前18位字符，获得颁发日期
    return pubdate[0]
    # 返回适航指令颁发日期

def author(dir):
    # 定义函数 author()，dir为文本目录，格式为txt文本
    document = open(dir, 'r', encoding='utf-8')
    # 以UTF-8的字体格式打开目录中文本
    doc = document.read()
    # 获取文本中的文本内容
    author_orig = re.findall("七. 联系人：(.*)", doc, re.S)
    # 获得适航指令联系人
    author_orig[0] = author_orig[0].strip()
    # 去除适航指令联系人中的多余空格及换行
    authorstr = author_orig[0]
    author = [authorstr[0:4].strip()]
    # 截取联系人前4位字符，获得联系人姓名
    return author[0]
    # 返回适航指令联系人
