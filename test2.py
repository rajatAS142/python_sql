import psycopg2
import pandas as pd
from openpyxl.workbook import Workbook
db = psycopg2.connect(database="AssignmentPythonSQL", user="postgres", password="Rajat@98")

try:
    data = pd.read_sql("select emp.ename, dept.dname, emp.empno ,(case when enddate is not null then ((enddate-startdate+1)/30)*jobhist.sal else ((current_date-startdate+1)/30)*jobhist.sal end)as Total_Compensation,(case when enddate is not null then ((enddate-startdate+1)/30) else ((current_date-startdate+1)/30) end)as Months_Spent from jobhist, dept, emp where jobhist.deptno=dept.deptno and jobhist.empno=emp.empno",con=db)  # Storing Query result in DataFrames
    data.to_excel("Output2.xlsx")  # Converting DataFrame to Excel filey
except:
    print("Error")

