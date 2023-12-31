import threading
import requests

def make_http_request(url):
    response = requests.get(url)
    print(f"URL: {url}, Status Code: {response.status_code}")

if __name__ == "__main__":
    urls = ["www.abc.com"]

    threads = []

    for url in urls:
        thread = threading.Thread(target=make_http_request, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    print("Hoàn thành")
