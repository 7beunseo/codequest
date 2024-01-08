import json
file_path = 'codequest/stack.json'

with open(file_path, 'r', encoding='utf-8') as f:
    # 파일을 UTF-8로 읽고, 디코딩하여 JSON으로 로드
    stack_list = json.loads(f.read())

with open("codequest/codequest.json","r", encoding='utf-8') as f:
    codequests=json.load(f)

new_list=[]
for codequest in codequests:
    new_data={'model':'filter.codequest'}

    if codequest['stacks']:
        # 리스트로 변환 
        stacks=[stack.strip() for stack in codequest['stacks'].split(',')]
        print(stack_list)
        # 둘 사이를 연결할 때 리스트의 이름값이면 안됨 -> id값이어야 한다 
        stack_int_list=[]
        for stack in stacks:
            # 스택에 해당하는 인덱스 값을 찾음 
            stack_int=stack_list.index(stack)+1
            stack_int_list.append(stack_int)
        codequest['stacks']=stack_int_list
    else:
        codequest['stacks']=[]
    new_data['fields']=codequest
    new_list.append(new_data)

print(new_list)

with open('codequest/codequest.json','w',encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)
