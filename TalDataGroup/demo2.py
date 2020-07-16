from TalDataGroup.replace_by_folders import FilesReader
import os

ProjectPath = os.path.abspath('..')

path_org = [ProjectPath + '/everyday_hr_document_directory_mysql2/']

# path = ProjectPath + '/test/'
for path in path_org:
    file = os.listdir(path)
    print(file)

    if '.DS_Store' in file:
        file.remove('.DS_Store') #去除.DS_Store文件
    else:
        pass

    reader1 = FilesReader(path)
    #
    # reader1.replace_in_path('jdbc:oracle:thin:@192.168.11.194:1521:linxesbi2', 'jdbc:mysql://192.168.13.42:3336/xesbi', False)
    # reader1.replace_in_path('--password-file hdfs://turinghdfs:8020/user/hdfs/password/SQOOP_HAXESBI/password.file', '--password-file hdfs://turinghdfs:8020/user/hdfs/password/SQOOP_MYSQL/password.file', False)



    reader1.replace_in_path('&#47;data&#47;downf&#47;', '&#47;data&#47;downf&#47;mysqlfile&#47;', False)


    # reader1.replace_in_path('--username xesbi', '--username xesbi_readonly', False)
    # reader1.replace_in_path('--password R8GKsW3ZlMnF', '--password-file hdfs://turinghdfs:8020/user/hdfs/password/SQOOP_XESBI_MYSQL/password.file', False)
    # #
    # reader1.replace_in_path('Oracle', 'MySql', False)
    # reader1.replace_in_path('bi_income_others', 'bi_income_others', False)
