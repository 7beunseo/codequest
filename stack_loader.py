import json

file_path = 'codequest/stack.json'


with open(file_path, 'r', encoding='utf-8') as f:
    # 파일을 UTF-8로 읽고, 디코딩하여 JSON으로 로드
    stack_list = json.loads(f.read())

new_list = []
for stack in stack_list:
    new_data = {'model': 'filter.stack'}
    new_data['fields'] = {}
    new_data['fields']['title'] = stack
    new_list.append(new_data)

print(new_list)

with open('codequest/stack_data.json','w',encoding='utf-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)
