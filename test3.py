import logging

import pandas as pd
import psycopg2
class Employees:

 def fetched_data(self):

  try:
    conn = psycopg2.connect(database="AssignmentPythonSQL", user="postgres", password="Rajat@98")
    cur=conn.cursor()
    df=pd.read_excel('Output2.xlsx')


    cur.execute("""Create table  some_table( empname varchar(250),
                                            Dname varchar(250),
                                            empno numeric,
                                            tot_comp numeric, months Integer);""")

    conn.commit()
    cur.execute(
        "select emp.ename, dept.dname, emp.empno ,(case when enddate is not null then ((enddate-startdate+1)/30)*jobhist.sal else ((current_date-startdate+1)/30)*jobhist.sal end)as Total_Compensation,(case when enddate is not null then ((enddate-startdate+1)/30) else ((current_date-startdate+1)/30) end)as Months_Spent from jobhist, dept, emp where jobhist.deptno=dept.deptno and jobhist.empno=emp.empno")

    row = cur.fetchall()


    for r in row:

        cur.execute("insert into some_table values ('{}','{}','{}','{}','{}');".format(r[0],r[1],r[2],r[3],r[4]))


    #   empname=df['ename'][d]
    #   Dname=df['dname'][d]
    #   empno=df['empno'][d]
    #   total_comp=df['Total_compensation'][d]
    #   months= df['Months_spent'][d]
    #
    # values = (empname, Dname, empno, total_comp, months)

      # storing values in tuple
      # values.to_sql(openpyxl, 'Compensation', if_exists='append', index=False)


    conn.commit()

  except Exception as e:

      # if exception thrown in try block
      logging.error("Error", e)
  finally:
      # after completion of above block,closing the connection and commiting to the database
     if conn is not None:
       cur.close()
       conn.close()







if __name__ == '__main__':
    conn = None
    cur = None
    emp = Employees()
    emp.fetched_data()