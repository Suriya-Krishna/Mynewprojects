import sqlite3

conn = sqlite3.connect('hos2_new.db')
query = """CREATE TABLE HOSPITAL(HOSPITAL_ID INT PRIMARY KEY NOT NULL, HOSPITAL_NAME CHAR(200) NOT NULL, BED_COUNT INT NOT NULL)"""
conn.execute(query)
query1 = """CREATE TABLE DOCTOR(DOCTOR_ID INT PRIMARY KEY NOT NULL, DOCTOR_NAME CHAR(100) NOT NULL, HOSPITAL_ID INT NOT NULL, JOINING_DATE DATE NOT NULL, SPECIALITY CHAR(200) NOT NULL, SALARY INT NOT NULL, EXPERIENCE CHAR(20), FOREIGN KEY(HOSPITAL_ID) REFERENCES HOSPITAL(HOSPITAL_ID))"""
conn.execute(query1)
conn.execute("INSERT INTO HOSPITAL(HOSPITAL_ID, HOSPITAL_NAME, BED_COUNT)""VALUES(1,'MAYO CLINIC',200)")
conn.execute("INSERT INTO HOSPITAL(HOSPITAL_ID, HOSPITAL_NAME, BED_COUNT)""VALUES(2,'CLEAVELAND CLINIC',400)")
conn.execute("INSERT INTO HOSPITAL(HOSPITAL_ID, HOSPITAL_NAME, BED_COUNT)""VALUES(3,'JOHNS HOPKINS',1000)")
conn.execute("INSERT INTO HOSPITAL(HOSPITAL_ID, HOSPITAL_NAME, BED_COUNT)""VALUES(4,'UCLA MEDICAL CENTER',1500)")
conn.execute("INSERT INTO DOCTOR(DOCTOR_ID,DOCTOR_NAME,HOSPITAL_ID,JOINING_DATE,SPECIALITY,SALARY,EXPERIENCE)""VALUES(101,'DAVID',1,2005-02-10,'PEDIATRIC',40000,NULL)")
conn.execute("INSERT INTO DOCTOR(DOCTOR_ID,DOCTOR_NAME,HOSPITAL_ID,JOINING_DATE,SPECIALITY,SALARY,EXPERIENCE)""VALUES(102,'MICHAEL',1,2018-07-23,'ONCOLOGIST',20000,NULL)")
conn.execute("INSERT INTO DOCTOR(DOCTOR_ID,DOCTOR_NAME,HOSPITAL_ID,JOINING_DATE,SPECIALITY,SALARY,EXPERIENCE)""VALUES(103,'SUSAN',2,2016-05-19,'GARNACOLOGIST',25000,NULL)")
conn.execute("INSERT INTO DOCTOR(DOCTOR_ID,DOCTOR_NAME,HOSPITAL_ID,JOINING_DATE,SPECIALITY,SALARY,EXPERIENCE)""VALUES(104,'ROBERT',2,2017-12-28,'PEDIATRIC',28000,NULL)")
conn.execute("INSERT INTO DOCTOR(DOCTOR_ID,DOCTOR_NAME,HOSPITAL_ID,JOINING_DATE,SPECIALITY,SALARY,EXPERIENCE)""VALUES(105,'LINDA',3,2004-06-04,'GARNACOLOGIST',42000,NULL)")
conn.execute("INSERT INTO DOCTOR(DOCTOR_ID,DOCTOR_NAME,HOSPITAL_ID,JOINING_DATE,SPECIALITY,SALARY,EXPERIENCE)""VALUES(106,'WILLIAM',3,2012-09-11,'DERMATOLOGIST',30000,NULL)")
conn.execute("INSERT INTO DOCTOR(DOCTOR_ID,DOCTOR_NAME,HOSPITAL_ID,JOINING_DATE,SPECIALITY,SALARY,EXPERIENCE)""VALUES(107,'RICHARD',4,2014-08-21,'GARNACOLOGIST',32000,NULL)")
conn.execute("INSERT INTO DOCTOR(DOCTOR_ID,DOCTOR_NAME,HOSPITAL_ID,JOINING_DATE,SPECIALITY,SALARY,EXPERIENCE)""VALUES(108,'KAREN',4,2011-10-17,'RADIOLOGIST',30000,NULL)")
conn.commit()
cursor = conn.execute("SELECT * from DOCTOR where SPECIALITY ='PEDIATRIC' AND SALARY > 30000")
print(cursor.fetchall())
id_opt = int(input("Enter the desired hospital id"))
cursor = conn.execute(f"SELECT * from DOCTOR INNER JOIN HOSPITAL where DOCTOR.HOSPITAL_ID= {id_opt} AND DOCTOR.HOSPITAL_ID = HOSPITAL.HOSPITAL_ID")
print(cursor.fetchall())
conn.commit()

conn.close()