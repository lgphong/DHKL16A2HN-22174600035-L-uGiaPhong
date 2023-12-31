import json

json_data = '{"name": "John", "age": 30, "city": "New York"}'

python_obj = json.loads(json_data)

print("Đối tượng Python:", python_obj)
name = python_obj['name']
age = python_obj['age']
city = python_obj['city']

# In các giá trị
print("Tên:", name)
print("Tuổi:", age)
print("Thành phố:", city)
