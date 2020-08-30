import requests
from threadpool import ThreadPool

def my_func(url):
    with requests.Session() as r:
        r.get(url)
ThreadPool(128).map(my_func, open('urls.txt'))