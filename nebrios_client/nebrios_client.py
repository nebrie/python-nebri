import requests


class NebriOSClient:

    def __init__(self, instance_name):
        self.instance_name = instance_name

    def api_request(self, api_module, view_name, method='GET', payload=None, files=None):
        """
        :param api_module: the api module instantiated on the given instance
        :param view_name: a view in the given api module
        :param method: the HTTP request method. defaults to GET
        :param payload: any data that needs to be sent to the view. defaults to None. should be a dict
        :return: returns the response content or json depending on the response content-type
        """
        url = 'https://%s.nebrios.com/api/v1/%s/%s' % (self.instance_name, api_module, view_name)
        r = None
        if method == 'POST':
            r = requests.post(url, data=payload, files=files)
        elif method == 'GET':
            r = requests.get(url, params=payload)
        elif method == 'PUT':
            r = requests.put(url, data=payload)
        elif method == 'DELETE':
            r = requests.delete(url)
        elif method == 'HEAD':
            r = requests.head(url)
        elif method == 'OPTIONS':
            r = requests.options(url)
        else:
            return 'Incorrect Method.'
        if 'application/json' in r.headers['content-type']:
            return r.json()
        return r.content
