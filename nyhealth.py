import asyncio, asyncpg
import csv
import re
isint = re.compile('^\d+\.?\d*$')
ismoney = re.compile('^\$\d')
file = 'c:/Temp/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv'
sqline = 'INSERT into nyhealth (health_service_area, ' \
         'hospital_county, ' \
         'operating_certificate_number, ' \
         'faciliti_id, ' \
         'faciliti_name, ' \
         'age_group, ' \
         'zip_code, ' \
         'gender, ' \
         'race, ' \
         'ethnicity, ' \
         'length_of_stay, ' \
         'type_of_admission, ' \
         'patient_disposition, ' \
         'discharge_year, ' \
         'ccs_diagnosis_code, ' \
         'ccs_diagnosis_description, ' \
         'ccs_procedure_code, ' \
         'css_procedure_discription, ' \
         'apr_drg_code, ' \
         'apr_drg_discription, ' \
         'apr_mdc_code, ' \
         'apr_mdc_discription, ' \
         'apr_severiti_of_illiness_code, ' \
         'apr_severiti_of_illiness_discription, ' \
         'apr_risk_of_mortality, ' \
         'apr_medical_surgical_description, ' \
         'payment_typology_1, ' \
         'payment_typology_2, ' \
         'payment_typology_3, ' \
         'Attending_Provider_License_Number, ' \
         'operating_Provider_License_Number, ' \
         'other_Provider_License_Number, ' \
         'birth_weight, ' \
         'abortion_edit_indicator, ' \
         'emergency_department_indicator, ' \
         'total_charges, ' \
         'total_cost) VALUES  ({})'

async def main():

    dbcon = await asyncpg.connect(host='192.168.32.10', user='postgres',
                        password='2900477', database='wadeu')
    with open(file, 'r') as cf:
        rdr = csv.reader(cf, delimiter=',')
        for i, row in enumerate(rdr):
            if not i:
                head = row.copy()
                print(len(head))
                for h in head:
                    print(h)
            else:
                # print(len(row))
                val = ''
                for r in row:
                    if r:
                        if re.match(isint, r):
                            val = val + ',' + r
                        elif re.match(ismoney, r):
                            val = val + ',' + r[1:]
                        else:
                            val = val + ', \'' + r + '\''
                    else:
                        val = val + ', Null'
                qline = sqline.format(val[1:])
                try:
                    await dbcon.execute(qline)
                except Exception as e:
                    # print(e)
                    continue
                # print(qline)
            # if i:
            #     break
            if not i % 1000:
                print(i)
    await dbcon.close()

asyncio.get_event_loop().run_until_complete(main())



