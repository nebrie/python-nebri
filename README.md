# Python Nebrios

The simple and easy-to-use package for making NebriOS api requests from a python application.

This app is intended for use with a NebriOS instance. Visit https://nebrios.com to sign up for free!

<h2>Installation</h2>
This app can be installed via PyPi:

```
pip install python-nebrios
```

<h2>Usage Example</h2>
```
from nebrios_client.nebrios_client import NebriOSClient


client = NebriOSClient('demo')
response = client.api_request('greeting_api', 'start_greeting', payload={'greeting':'hello'})
print response
# prints {u'message': u'Hi! How are you?', u'identifier': u'fbbd578a8f1d46d483efb5992e32b265', u'greeting': u'hello'}
```
