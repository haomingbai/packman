# -*- coding:utf-8 -*-
import os,shutil,zipfile,sqlite3
pkg=raw_input("what to install:")
print "INSTALLING "+pkg
#pkg is the package to be installed
pkgl=sqlite3.connect('C:/ProgramData/pkgl.db')
pkgl.execute('create table '+pkg+'(id integer primary key autoincrement not null,dep text not null)')
pkgr=sqlite3.connect('E:/repository/pkgr.db')
#pkgl has saved the name of installed pkgs pkgr has saved the name of pkgs in repository
cache=pkgr.execute("select dep from "+pkg+" where id>0")
result=cache.fetchall()
#to read the dependences need to be installed
for re in result:
    dep=re[0]
    zipsfile=zipfile.ZipFile("E:/repository/dep/"+dep+".zip")
    zipslist = zipsfile.namelist()
    for f in zipslist:
        zipsfile.extract(f, "C:/Dependences/"+dep)
        zipsfile.close()
    pkgl.execute("insert into "+pkg+" (dep) values ('"+(dep)+"')")
    print "INSTALLING "+dep
#dependences insallation complete
zipsfile=zipfile.ZipFile("E:/repository/pkg/"+pkg+".zip")
zipslist = zipsfile.namelist()
for f in zipslist:
        zipsfile.extract(f, "C:/Program Files/"+pkg)
        zipsfile.close()
#to close files used in the installation
cache.close()
pkgr.close()
pkgl.commit()
pkgl.close()
print "INSTALLATION COMPLETE!"
#the end
