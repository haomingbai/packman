# -*- coding:utf-8 -*-
import os,shutil,zipfile,sqlite3
pkgl=sqlite3.connect('C:/ProgramData/pkgl.db')
pkgr=sqlite3.connect('C:/ProgramData/pkgr.db')
cac=pkgl.execute("select name from sqlite_master where type='table' order by name")
result=cac.fetchall()
for re in result:
    pkg=re[0]
    if formt=="sqlite_master" or formt=="sqlite_sequence":
        pass
    else:
        cache=pkgr.execute("select dep from "+pkg+" where id>0")
        resul=cache.fetchall()
        for rr in resul:
            dep=rr[0]
            zipsfile=zipfile.ZipFile("E:/repository/dep/"+dep+".zip")
            zipslist = zipsfile.namelist()
        for f in zipslist:
            zipsfile.extract(f, "C:/Dependences/"+dep)
            zipsfile.close()
            print "INSTALLING "+dep
        zipsfile=zipfile.ZipFile("E:/repository/pkg/"+pkg+".zip")
        zipslist = zipsfile.namelist()
        for f in zipslist:
            zipsfile.extract(f, "C:/Program Files/"+pkg)
            zipsfile.close()
cache.close()
pkgr.close()
pkgl.commit()
pkgl.close()
print "INSTALLATION COMPLETE!"
