import xml.dom.minidom
xml_file = "sample.xml"
dom_tree = xml.dom.minidom.parse(xml_file)
company = dom_tree.documentElement
company_name = company.getElementsByTagName("name")[0].childNodes[0].data
staff_list = company.getElementsByTagName("staff")
print("Company Name:", company_name)
print("Staff Information:")

for staff in staff_list:
    staff_id = staff.getAttribute("id")
    staff_name = staff.getElementsByTagName("name")[0].childNodes[0].data
    staff_salary = staff.getElementsByTagName("salary")[0].childNodes[0].data
    print("Staff ID:", staff_id)
    print("Name:", staff_name)
    print("Salary:", staff_salary)