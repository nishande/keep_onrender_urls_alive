import time
import requests
import json

def call_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Successfully called the URL: {url}")
    except requests.RequestException as e:
        print(f"Error occurred: {e}")

def main():
    with open('urls.json', 'r') as file:
        data = json.load(file)
        urls = data['urls']

    while True:
        for url in urls:
            call_url(url)
        time.sleep(60 * 60)  # Wait for 60 minutes before the next set of calls

if __name__ == "__main__":
    main()
