
import requests
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    print("Yêu cầu thành công!")
else:
    print("Có lỗi xảy ra!")

data = response.json()

print(f"Tổng số bài post: {len(data)}")
for post in data:
    print(f"userID: {post['userId']}")
    print(f"id: {post['id']}")
    print(f"title: {post['title']}")
    print(f"body: {post['body']}")
    print("-" * 20)
