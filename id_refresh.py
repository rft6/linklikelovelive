import json

# load the data
with open('./data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# renumber ids sequentially starting from 1
for idx, item in enumerate(data, start=1):
    item['id'] = idx

# save new file
output_path = './data_out.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

output_path
