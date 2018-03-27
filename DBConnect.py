from sqlalchemy.ext.automap import automap_base
import sqlalchemy as al
import sqlalchemy.orm as alo
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy_repr import *

class DBConnect():
    def __init__(self,name='postgres',password='1234',host='192.168.32.150',dbase='wade',url='',echo=0, autocommit=1):
        __autocommit = autocommit
        if url == '':
            __url = 'postgres://'+name+':'+password+'@'+host+'/'+dbase
        else:
            __url = url
        __echo = echo
        try:
            self.myEngine= al.create_engine(name_or_url=__url,echo=__echo)
        except:
            print('URL string is not correct!')
            exit(99)
        try:
        #    myEngine = MyEngine()
            self.Base = automap_base()
            self.Base.prepare(self.myEngine, reflect=True)
            self.con = self.myEngine.connect()
            self.S = alo.sessionmaker(bind=self.myEngine, autocommit=__autocommit)
            self.s = self.S()
            self.metadata = al.MetaData(self.myEngine)
            self.metadata.reflect(self.myEngine)


        except:
            raise('not connect!')
            #print('Not connect!')
            exit(98)
