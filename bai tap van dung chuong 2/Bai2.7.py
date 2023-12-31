import json
python_objs = {'name':'John',
                'age':30,
                'city':'New York'}

json_data=json.dumps(python_objs,indent=2)
print("Chuoi JSON la:\n",json_data)
print('\n In tat ca cac gia tri :')
for key,value in python_objs.items():
    print(f'{key}:{value}')