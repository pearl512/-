import requests

url = "https://fanyi.baidu.com/sug"

s = input("please input the English word:")
dat = {
    "kw": s
}

resp = requests.post(url, data=dat)
print(resp.json())
 