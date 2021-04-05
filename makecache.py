# -*- coding:utf-8 -*-
import os,shutil,zipfile,sqlite3
if os.path.exists("E:/reponsitory/pkgr.db")=True:
    shutil.copy("E:/reponsitory/pkgr.db",'C:/ProgramData/pkgr.db')
    print "MAKECACHE COMPLETE"
else print "FAILED"
