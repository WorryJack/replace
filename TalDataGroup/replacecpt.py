from TalDataGroup.replace_by_folders import FilesReader
import os
import xml.etree.ElementTree as ET
#获取父目录路径
ProjectPath = os.path.abspath('..')

# path_org = [ProjectPath + '/cptfile/', ProjectPath + '/bi_detail/']

path_org = [ProjectPath + '/demo/']
for path in path_org:
    file = os.listdir(path)
    print(file)

    if '.DS_Store' in file:
        file.remove('.DS_Store') #去除.DS_Store文件
    else:
        pass

    reader1 = FilesReader(path)

    reader1.replace_in_path('Key:data_time', 'Key:run_time', False)
    reader1.replace_in_path('Key:RUN_TIME', 'Key:run_time', False)
    reader1.replace_in_path('xesbidw', 'newbi_mysql', False)
    reader1.replace_in_path('haxesbi.', '', False)
    reader1.replace_in_path('--', '-- ', False)
    reader1.replace_in_path('NVL', 'ifnull', False)

    for i in file:
        tree = ET.parse(path + i)# 读取xml文件
        print(i)
        root = tree.getroot()
        child = root.find('ReportParameterAttr')
        if child is None:
            pass
        else:
           child = child.find('ParameterUI')
        if child is None:
            pass
        else:
           child = child.find('Layout')
        if child is None:
            pass
        else:
           child = child.findall('Widget')
        if child is None:
            pass
        else:
            for child2 in child:
                child3 = child2.find('InnerWidget').find('Dictionary')
                if child3 is None:
                    pass
                else:
                    addr = child3.find('FormulaDictAttr')
                    if addr is None:
                        pass
                    else:
                        kiName = child3.find('FormulaDictAttr').get('kiName')
                        viName = child3.find('FormulaDictAttr').get('viName')
                        if kiName is None and viName is None:
                            pass
                        else:
                            newkiName = kiName.lower()
                            newviName = viName.lower()
                            old_kistr = "kiName=\"" + kiName +"\""
                            old_vistr = "viName=\"" + viName +"\""
                            new_kistr = "kiName=\"" + newkiName +"\""
                            new_vistr = "viName=\"" + newviName +"\""
                            reader1.replace_in_path(old_kistr, new_kistr, False)
                            reader1.replace_in_path(old_vistr, new_vistr, False)
                            # 采用字符串替换，直接写xml文件会破坏cpt文件结构
