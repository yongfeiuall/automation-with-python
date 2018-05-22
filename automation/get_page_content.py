import requests


r = requests.get('http://localhost:8000')

print(r.status_code)
print(r.text)

assert r.status_code == 200
assert 'Hello World!' in r.text