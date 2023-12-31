import json

python_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "job": "Developer"
}

json_data = json.dumps(python_dict, indent=4)

print("Chuỗi JSON với thụt lề 4:")
print(json_data)