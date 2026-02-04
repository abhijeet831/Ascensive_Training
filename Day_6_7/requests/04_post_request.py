import requests

r = requests.post('https://httpbin.org/post?a=b' , data={'abhijeet':'value'})
print(r.text)