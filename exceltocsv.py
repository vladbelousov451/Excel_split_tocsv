# importe required libraries
import openpyxl
import csv

from pip._vendor.distlib.compat import raw_input

SHEETNAME = raw_input("print SheetName")
# open given workbook
# and store in excel object
excel = openpyxl.load_workbook(f"{SHEETNAME}.xlsx" )

# select the active sheet
sheets = excel.worksheets

for sheet in sheets:
	name = sheet.title
	# writer object is created
	col = csv.writer(open(f"{name}.csv",
						'w',
						newline=""))

	# writing the data in csv file
	for r in sheet.rows:
		# row by row write
		# operation is perform
		col.writerow([cell.value for cell in r])

