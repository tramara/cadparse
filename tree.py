# -*-coding:UTF-8 -*-

pdfdir = "D:\\python_work\\cad_program\\CAD"  # Define the dir of pdf file. Format string.
txtdir = "D:\\python_work\\cad_program\\post"  # Define the dir of txt file. Format string.

import os
import re
import sys
import get as g
import tranpdf as t

pdflist = os.listdir(pdfdir)
# 将目录下文件名称列表，包含文件属性名
for i in range(0, len(pdflist)):
    pdflist[i] = pdflist[i].strip(".pdf")
    # 提取pdf文件目录下的所有文件名称，剔除属性名

namelist = pdflist
# 将pdf文件名（不包含属性名）单独存放在名称列表中

for i in range(0, len(namelist)):
    pathtxt = os.path.join(txtdir, namelist[i] + ".txt")
    if os.path.exists(pathtxt) == False:
        t.pdftxt(pdfdir + "\\" + pdflist[i] + ".pdf", txtdir)


txtlist = os.listdir(txtdir)
for i in range(0,len(txtlist)):
    inpath = os.path.join(txtdir, txtlist[i])
    print(g.cadno(pathtxt), "\n", g.amendno(pathtxt), "\n", g.app(pathtxt), "\n", g.ref(pathtxt), "\n",
          g.text(pathtxt), "\n", g.effdate(pathtxt), "\n", g.pubdate(pathtxt), "\n", g.author(pathtxt))
'''
txtlist = os.listdir(txtdir)
for i in range(0, len(txtlist)):
    txtlist[i] = pdflist[i].strip(".txt")
print(txtlist)
    pathtxt = os.path.join(txtdir, txtlist[i])
    if os.path.exists(pathtxt) == False:
        f.pdftxt(pdfdir + "\\"+ pdflist[i]+ ".pdf", "D:\\python_work\\cad_program\\post")
        

if len(list(set(pdflist).difference(set(txtlist)))) > 0:
    tranlist = list(set(pdflist).difference(set(txtlist)))
    for i in range(0,len(tranlist)):
        tranlist[i] = pdfdir + "\\" + tranlist[i] + ".pdf"
        rtfname = f.pdftxt(tranlist[i], txtdir)
        print(rtfname)
        t.pdftxt(rtfname, "D:\\python_work\\cad_program\\post")
        print(g.cadno(rtfname),"\n", g.amendno(rftname),"\n", g.app(rftname),"\n", g.ref(rftname),"\n", g.text(rtfname),"\n", g.effdate(rtfname),"\n", g.pubdate(rftname),"\n", g.author(rftname))
'''
