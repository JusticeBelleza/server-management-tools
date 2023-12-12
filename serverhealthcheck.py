import os
import psutil
import requests

def check_server(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Server {url} is up and running.")
        else:
            print(f"Server {url} is up but returned status code {response.status_code}.")
    except requests.RequestException:
        print(f"Server {url} is down.")

def check_system_health():
    cpu_usage = psutil.cpu_percent(1)
    memory_usage = psutil.virtual_memory().percent
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")

if __name__ == "__main__":
    SERVER_URL = "http://yourserver.com"
    check_server(SERVER_URL)
    check_system_health()
