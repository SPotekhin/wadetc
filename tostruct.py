import asyncio, asyncpg, re, uuid

async def main():
    dbcon = await asyncpg.connect(host='192.168.32.10', user='postgres',
                                  password='2900477', database='wadeu')

    tname = 'nyhealth'

    qline = f'select a.attname, a.attnum from pg_catalog.pg_attribute a ' \
            f'join pg_catalog.pg_class c on c.relfilenode = a.attrelid ' \
            f'where c.relname = \'{tname}\' and a.attnum > 0;'
    # qline = f'select * from {tname} limit 1;'
    #print(qline)
    cols = {}
    try:
        q = await dbcon.fetch(qline)
        #print(q)
        for r in q:
            cols.update({r['attnum']:r['attname']})

    except Exception as e:
        print(e)
    props = {}
    ptype = {}
    qline = 'select id, name, ptype from property where entityid = 14;'
    q = await dbcon.fetch(qline)
    for r in q:
        aname = r['name'].split(' ')
        pname = '_'.join(aname).lower()
        props.update({pname: r['id']})
        ptype.update({pname: r['ptype']})
    print(props)
    qline = 'select * from nyhealth;'
    try:
        q = await dbcon.fetch(qline)
        # async with tr = dbcon.transaction():
        tr = dbcon.transaction()
        await tr.start()
        for i, r in enumerate(q):

            ouuid = uuid.uuid1()
            iqline = f'insert into dobj (objuid) values (\'{ouuid}\') RETURNING id;'
            iq = await dbcon.fetchrow(iqline)
            objid = iq['id']
            dsql = ''
            for f in props:
                if not r[f]:
                    continue
                if ptype[f] == 0:
                    tn = 'dint'
                    pdata = r[f]
                elif ptype[f] == 1:
                    tn = 'dnumber'
                    pdata = r[f]
                elif ptype[f] == 2:
                    tn = 'dstring'
                    pdata = '\''+r[f]+'\''
                else:
                    continue
                propid = props[f]
                dsql = dsql + f'insert into {tn} (data, propid, objid) ' \
                       f'values ({pdata},{propid},{objid}); '
            try:
                await dbcon.execute(dsql)
            except Exception as e:
                print(e)
                # print(dsql)
            # finally:
            #     await tr.commit()
            if i % 1000 == 0:
                print(objid)
                await tr.commit()
                tr = dbcon.transaction()
                await tr.start()
                    # print(props[f], f, r[f])
                # print(r)
                # for f in r:
                #     print(f)

                # print('id of obj = ',iq['id'])
    except Exception as e:
        print(e)
        exit(333)
    await dbcon.close()

asyncio.get_event_loop().run_until_complete(main())
