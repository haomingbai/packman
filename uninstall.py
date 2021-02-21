# -*- coding:utf-8 -*-
import os,shutil,zipfile,sqlite3
pkg=raw_input("what to remove:")
print "REMOVING "+pkg
pkgl=sqlite3.connect('C:/ProgramData/pkgl.db')
pkgl.execute("drop table "+pkg)
shutil.rmtree("C:/Program Files/"+pkg)
pkgl.commit()
cac=pkgl.execute("select name from sqlite_master where type='table' order by name")
result=cac.fetchall()
for re in result:
    formt=re[0]
    if formt=="sqlite_master" or formt=="sqlite_sequence":
        pass
    else:
        print "l17"+formt
        cac=pkgl.execute("select dep from "+formt+" where id>0")
        resul=cac.fetchall()
        for rr in resul:
            dep=rr[0]
            shutil.copytree("C:/Dependences/"+dep,"C:/ProgramData/cache/"+dep)
shutil.rmtree("C:/Dependences")
print "Removing Dependences"
if not os.path.exists("C:/ProgramData/cache"):
    os.makedirs("C:/ProgramData/cache")
shutil.copytree("C:/ProgramData/cache","C:/Dependences")
shutil.rmtree("C:/ProgramData/cache")
pkgl.close()
