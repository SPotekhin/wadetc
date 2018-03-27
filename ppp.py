import csv

file = 'c:/Temp/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv'

with open(file,'r') as cf:
    rdr = csv.reader(cf, delimiter=',')
    fo = open('c:/temp/tdata.txt','w')
    for i, row in enumerate(rdr):
        if not i:
            head = row.copy()

        else:
            for j,fld in enumerate(row):
                print(head[j],' ----> ', fld)
                fo.write(f'{head[j]} : {fld}\n')
        print(60*'=*')
        if i :
            break