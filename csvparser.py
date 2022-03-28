import xlrd
import csv
import xlsxwriter
import openpyxl
from pathlib import Path

def populate_data_in_xls_file(data):
    """
        It will create a xls sheet
    :param data: 
    :return: 
    """
    workbook = xlsxwriter.Workbook("sample.csv")
    worksheet = workbook.add_worksheet("jobs")

    worksheet.write('A1', 'FactId')
    worksheet.write('B1', 'FACTName')
    worksheet.write('C1', 'BussinessApp')
    worksheet.write('D1', 'VeracodeApp')
    worksheet.write('E1', 'VeracodeTEAMSName')
    worksheet.write('F1', 'SonarAppName')
    worksheet.write('G1', 'Technology')
    worksheet.write('H1', 'GitRepo')
    worksheet.write('I1', 'DeploymentType')
    worksheet.write('J1', 'ENV_Props_Folder')
    worksheet.write('K1', 'Environment')
    worksheet.write('L1', 'JobType')
    worksheet.write('M1', 'ArtifactoryUploadPath')
    worksheet.write('N1', 'GitBranch')
    worksheet.write('O1', 'server')
    worksheet.write('P1', 'credential')

    row_index = 2
    for user_detail in data:
        worksheet.write('A' + str(row_index), user_detail['FactId'])
        worksheet.write('B' + str(row_index), user_detail['FACTName'] )
        worksheet.write('C' + str(row_index), user_detail['BussinessApp'])
        worksheet.write('D' + str(row_index), user_detail['VeracodeApp'])
        worksheet.write('E' + str(row_index), user_detail['VeracodeTEAMSName'])
        worksheet.write('F' + str(row_index), user_detail['SonarAppName'])
        worksheet.write('G' + str(row_index), user_detail['Technology'])
        worksheet.write('H' + str(row_index), user_detail['GitRepo'])
        worksheet.write('I' + str(row_index), user_detail['DeploymentType'])
        worksheet.write('J' + str(row_index), user_detail['ENV_Props_Folder'])
        worksheet.write('K' + str(row_index), user_detail['Environment'])
        worksheet.write('L' + str(row_index), user_detail['JobType'])
        worksheet.write('M' + str(row_index), user_detail['ArtifactoryUploadPath'])
        worksheet.write('N' + str(row_index), user_detail['GitBranch'])
        worksheet.write('O' + str(row_index), user_detail['server'])
        worksheet.write('P' + str(row_index), user_detail['credential'])

        row_index += 1

    workbook.close()
    print("success")

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
