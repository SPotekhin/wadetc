from DBConnect import *
import os, re

db = DBConnect(url='postgres://postgres:postgres@localhost/wclocal', autocommit=0)

ENT = db.Base.classes.entity
PRP = db.Base.classes.property
SDT = db.Base.classes.statdata

wdir = 'c:/recovery_data/tec2/new/'


for fls in os.scandir(wdir):
    if fls.is_file():
        f = open(wdir+fls.name,'r')
        name, ext = fls.name.split('.')
        prop = name[2:]
        try:
            q = db.s.query(PRP).filter(PRP.name == prop).first()
            propid = q.id
            print(propid, prop)
        except:
            print(prop, 'not found!')
            continue

        for i,r in enumerate(f):
            _, dt, dat = r.split(';')
            sdt = SDT()
            sdt.dt = dt
            if dat != 'None\n':
                sdt.datafloat = float(dat)
            else:
                sdt.datafloat = None
            sdt.propertyid = propid
            sdt.datastring = None
            # print(sdt.propertyid, sdt.datafloat, sdt.datastring, sdt.dt)
            db.s.add(sdt)
            if i > 0 and i % 10000 == 0:
                try:
                    db.s.commit()
                    print(i)
                except Exception as e:
                    db.s.rollback()
                    print('error write bd!')
                    print(e)
                    exit(100)
        db.s.commit()
