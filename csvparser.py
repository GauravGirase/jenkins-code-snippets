import xlrd
import csv
import xlsxwriter
import openpyxl
from pathlib import Path

xlsx_file = 'FACT0804_JenkinsJobs.xlsx'
wb_obj = openpyxl.load_workbook(xlsx_file)
sheet = wb_obj.worksheets[1]
data = []
heading1 = []
heading2 = []

for count, values in enumerate(sheet.values, 1):
    dic = {}
    if count == 1:
        for j in values:
            heading1.append(j.strip())
    if count > 1:
        for i in range(len(values)):
            if i == 7:
                dic[heading1[i]] = values[i]
                dic[heading1[i]] = f"https://github.tfs.toyota.com/EAS-Channel-Access-Services/{dic['BussinessApp'].strip()}.git"
            else:
                dic[heading1[i]] = values[i]

        sheet2 = sheet = wb_obj.worksheets[2]
        for count2, values2 in enumerate(sheet2.values, 1):
            if count2 == 1:
                for k in values2:
                    heading2.append(k.strip())

            if count2 > 1:
                for i in range(len(values2)):
                    if i == 2:
                        dic[heading2[i]] = values2[i]
                        dic[heading2[i]] = f"https://artifactory.tfs.toyota.com/artifactory/easc-maven-prod-local/artifacts/{'-'.join(dic['BussinessApp'].split('-')[3:]).strip().lower()}.jar"
                    else:
                        dic[heading2[i]] = values2[i]

    if dic:
        data.append(dic)
print(data)

# populate_data_in_xls_file(data)
with open('output.csv', 'w', newline='') as f:
    wr = csv.DictWriter(f, delimiter=",", fieldnames=list(data[0].keys()))
    wr.writeheader()
    wr.writerows(data)
