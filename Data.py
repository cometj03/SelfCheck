import json

# create or modify json file
json_data = {'asdhf': 123, 'test': 'tttt'}

with open('./info.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent='\t')

# load json file
with open('./info.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)
    print(json.dumps(json_data, indent='\t'))