import requests


class NebriOSClient(object):

    def __init__(self, instance_name):
        self.instance_name = instance_name

    def api_request(self, api_module, view_name, method='GET', headers=None, payload=None, files=None):
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
            r = requests.post(url, data=payload, files=files, headers=headers)
        elif method == 'GET':
            r = requests.get(url, params=payload, headers=headers)
        elif method == 'PUT':
            r = requests.put(url, data=payload, headers=headers)
        elif method == 'DELETE':
            r = requests.delete(url, headers=headers)
        elif method == 'HEAD':
            r = requests.head(url, headers=headers)
        elif method == 'OPTIONS':
            r = requests.options(url, headers=headers)
        else:
            return 'Incorrect Method.'
        if 'application/json' in r.headers['content-type']:
            return r.json()
        return r.content
