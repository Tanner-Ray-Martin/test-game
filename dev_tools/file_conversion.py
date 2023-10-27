
#convert the xml file of tiles to json
import xml.etree.ElementTree as ET
import json
#xml_path = r"C:\Users\tanner.martin\Desktop\test_game\test_game3\resources\Tiles\tiles_spritesheet.xml"
#json_path = r"C:\Users\tanner.martin\Desktop\test_game\test_game3\resources\Tiles\tiles_spritesheet.json"
#xml_path = r"C:\Users\tanner.martin\Desktop\test_game\test_game3\resources\Items\items_spritesheet.xml"
#json_path = r"C:\Users\tanner.martin\Desktop\test_game\test_game3\resources\Items\items_spritesheet.json"
#xml_path = r"C:\Users\tanner.martin\Desktop\test_game\test_game3\resources\HUD\hud_spritesheet.xml"
#json_path = r"C:\Users\tanner.martin\Desktop\test_game\test_game3\resources\HUD\hud_spritesheet.json"
#tree = ET.parse(xml_path)
#root = tree.getroot()
#data = dict()
#def xml_to_json():
    #for item in root.findall("SubTexture"):
        #<SubTexture name="boxItem_disabled.png" x="0" y="72" width="70" height="70"/>
        #item_data = {k:v for k, v in item.items()}
        #item_name = item_data.get("name")
        #item_data.pop("name")
        #data.update({item_name:item_data})

    #with open(json_path, 'w') as fp:
        #json.dump(data, fp, sort_keys=True, indent=4)

#convert the txt file to json

json_data = {}
txt_files = [r"C:\Users\tanner.martin\Desktop\test_game\test_game3\resources\Players\p1_spritesheet.txt",
             r"C:\Users\tanner.martin\Desktop\test_game\test_game3\resources\Players\p2_spritesheet.txt",
             r"C:\Users\tanner.martin\Desktop\test_game\test_game3\resources\Players\p3_spritesheet.txt",
             r"C:\Users\tanner.martin\Desktop\test_game\test_game3\resources\Enemies\enemies_spritesheet.txt"]

json_files = [r"C:\Users\tanner.martin\Desktop\test_game\test_game3\resources\Players\p1_spritesheet.json",
             r"C:\Users\tanner.martin\Desktop\test_game\test_game3\resources\Players\p2_spritesheet.json",
             r"C:\Users\tanner.martin\Desktop\test_game\test_game3\resources\Players\p3_spritesheet.json",
             r"C:\Users\tanner.martin\Desktop\test_game\test_game3\resources\Enemies\enemies_spritesheet.json"]

def txt_to_json(file_index:int):
    txt_path = txt_files[file_index]
    json_path = json_files[file_index]
    with open(txt_path, 'r') as fp:
        data = fp.read()
    # Split the text into lines and process each line
    lines = data.strip().split('\n')
    for line in lines:
        parts = line.split('=')
        name = parts[0].strip()
        values = parts[1].strip().split()
        
        # Create a dictionary with the specified structure
        json_data[name] = {
            "x": int(values[0]),
            "y": int(values[1]),
            "width": int(values[2]),
            "height": int(values[3])
        }

    #save the json_data
    with open(json_path, 'w') as fp:
        json.dump(json_data, fp, sort_keys=True, indent=4)
    print(f"saved index: {file_index}")

for file_index in range(len(txt_files)):
    txt_to_json(file_index)