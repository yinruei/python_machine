import zipfile
import xml.etree.ElementTree as ET


listinfo = zipfile.ZipFile('F-D0047-093.zip', 'r')
# print(listinfo.namelist())

# for xml_file in listinfo.namelist():
#     print(xml_file)
#     tree = ET.parse(xml_file)
#     root = tree.getroot()
for name in listinfo.namelist():
    # print(name)
    # if name.endswith('/'):
    #     continue

    # if '' in name:
    f = listinfo.open(name)
    # print(f.name)
    file = ['09020_72hr_CH.xml', '10002_72hr_CH.xml']
    if f.name in file:
        print('innn')
        tree = ET.parse(f)
        root = tree.getroot()
        
        for elem in root.iter():
            _station_info = {}
            _weather_element_info = {}
            if 'location' in elem.tag:
                for location_elem in elem:
                    # parse station
                    # _station_info.update(parse_station(location_elem))

                    #parse weather element
                    # _weather_element_info.update(parse_weather_element(location_elem))

                    print('location_elem--->', location_elem)



# def parse_station(location_elem):