# Python Nebrios

The simple and easy-to-use package for making NebriOS api requests from a python application.

This app is intended for use with a NebriOS instance. Visit https://nebrios.com to sign up for free!

<h2>Installation</h2>
This app can be installed via pip:

```
pip install python-nebrios
```

<h2>Usage</h2>
In order to use this component to make NebriOS api requests, you must instantiate the class.
```
nebri = NebriOSClient('instance_name')
```
- instance name is your NebriOS instance name. i.e. https://<strong>instance_name</strong>.nebrios.com

<h2>Public Functions</h2>
Currently, this client only supports making api requests.

<strong>NebriOSClient.api_request</strong>
- api_module: the name of the api module stored on your NebriOS instance
- view_name: the name of the target function contained in the given api module
- method: the desired HTTP request method
- headers (optional): any custom headers you would like added to your request
- payload (optional): an object containing params and values
- files (optional): any files that you would like to upload via a POST request

<h2>Example</h2>
```
from nebrios_client import NebriOSClient


client = NebriOSClient('instance_name')
client.api_request('api_module', 'view_name', payload=json_payload)
# outputs api response
```
