import datetime
import requests
import random
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

def main():
    while True:
        light = round(2000 + random.random() * 2000, 0)
        temperature = round(-20 + random.random() * 55, 0)
        humidity = round(20 + random.random() * 60, 0)
        noise = round(30 + random.random() * 70, 0)
        co = round(1 + random.random() * 9, 0)
    
        url = 'https://223.171.78.159:1337/sensor-data-input?robot_id=512345&light={0}&temperature={1}&humidity={2}&noise={3}&co={4}'.format(light, temperature, humidity, noise, co)
        try:
            request_text = "Requested: " + url
            print(bcolors.WARNING + request_text + bcolors.ENDC)
            res = requests.get(url, verify=False)
            if str(res.status_code) == "200":
                print(bcolors.OKGREEN + "Transmission Succeeded: " + str(res.status_code) + bcolors.ENDC)
            else:
                print(bcolors.FAIL + 'Verify Result Code: ' + str(res.status_code) + bcolors.ENDC)
            print(bcolors.OKCYAN + res.text + bcolors.ENDC)
            print('Waiting for New Dataset ...')
        except (Exception) as error:
            print('Failed')
            print(error)
            break
        time.sleep(5)

main()
