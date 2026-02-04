import requests

# r = requests.put("https://httpbin.org/put" , data = {'key':'value'})
# print(r.text)

# r = requests.delete("https://httpbin.org/delete" , data = {'key':'value'})
# print(r.text)

# r = requests.head("https://httpbin.org/get")
# print(r.headers)   


r = requests.options("https://httpbin.org/get")
print(r.options)

