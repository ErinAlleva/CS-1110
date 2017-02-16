# Alex Hicks (awh4kc)

import requests
import json

customerId = 'your customerId here'
apiKey = '75ca43c1c9a8ea978abcc0c4bf5f56d7'

url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
payload = {
  "type": "Savings",
  "nickname": "test",
  "rewards": 10000,
  "balance": 10000,
}
# Create a Savings Account
response = requests.post(
	url,
	data=json.dumps(payload),
    headers={'content-type':'application/json'},
	)

if response.status_code == 201:
    print('account created')

