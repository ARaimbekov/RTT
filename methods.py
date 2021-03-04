import time
import requests
import socket


url = 'https://google.com'

# def results_table()

def find_ip():
    url_to_ip = url[8::]
    print("IP:", socket.gethostbyname(url_to_ip))


def rtt(): #simple rtt
    initial_time = time.time()
    request = requests.get(url)
    ending_time = time.time()
    elapsed_time = str(ending_time - initial_time)
    print("The Round Trip Time for {} is {}".format(url, elapsed_time))


def rtt_over_proxy():
    proxies = {
        "https": "142.4.203.248:3128"
    }
    initial_time = time.time()
    request = requests.get(url, proxies=proxies)
    ending_time = time.time()
    elapsed_time = str(ending_time - initial_time)
    print("The Round Trip Time for {} over proxy is {}".format(url, elapsed_time))


# def rtt_