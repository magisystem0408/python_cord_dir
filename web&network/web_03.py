# requestsについて


import requests

payload={'key1':'mamushi1','key2':'mamushi2'}

# getの場合
r =requests.get('http://httpbin.org/get',params=payload, timeout=60)
# postの場合
r =requests.post('http://httpbin.org/post',data=payload, timeout=60)

# putの場合
r=requests.put('http://httpbin.org/get',data=payload, timeout=60)

# deleteの場合
# timeout=1とすると1secで結果返って来なかったらエラーが出るようにする
r=requests.delete('http://httpbin.org/get',data=payload,timeout=1)


print(r.status_code)
print(r.text)
print(r.json())
