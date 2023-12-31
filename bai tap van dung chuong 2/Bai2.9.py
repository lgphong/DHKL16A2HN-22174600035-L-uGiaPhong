
import json

with open("company.json", "r") as f:
    data = json.load(f)

company_name = data["name"]
company_address = data["address"]
total_employees = data["total_employees"]

print(f"Tên công ty: {company_name}")
print(f"Địa chỉ: {company_address}")
print(f"Tổng số nhân viên: {total_employees}")
