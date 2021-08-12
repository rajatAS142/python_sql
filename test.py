import psycopg2
import pandas as pd
from openpyxl.workbook import Workbook
db = psycopg2.connect(database="AssignmentPythonSQL", user="postgres", password="Rajat@98")

#indent was not proper in code
try:
    data = pd.read_sql("SELECT e.empno ,e.ename, m .ename manager FROM emp e LEFT  JOIN emp m   ON m.empno = e.mgr", con=db)  # Storing Query result in DataFrames
    data.to_excel("Output1.xlsx")  # Converting DataFrame to Excel file
except:
    print("Error")





