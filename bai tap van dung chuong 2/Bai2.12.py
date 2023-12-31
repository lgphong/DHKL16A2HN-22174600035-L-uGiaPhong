
import requests

url = "https://jsonplaceholder.typicode.com/comments?postId=1"

response = requests.get(url)

if response.status_code == 200:
    print("Yêu cầu thành công!")
else:
    print("Có lỗi xảy ra!")

data = response.json()

data = sorted(data, key=lambda x: x["name"])


data = data[:3]
for post in data:
    print(f"id: {post['id']}")
    print(f"name: {post['name']}")
    print(f"email: {post['email']}")
    print(f"body: {post['body']}")
    print("-" * 20)
