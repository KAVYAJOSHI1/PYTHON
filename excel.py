
import openpyxl
loc=("C:\\Users\\KAVYA JOSHI\\OneDrive\\Documents\\tryexcel.xlsx")
wb=openpyxl.load_workbook(loc)
sheet_name="Sheet1"
sheet=wb[sheet_name]
print(sheet.cell(row=1,column=1).value)
