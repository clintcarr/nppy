import requests
from requests_ntlm import HttpNtlmAuth
import json

requests.packages.urllib3.disable_warnings()

headers = {"Accept": "application/json",
            "Content-Type": "application/json"}

session = requests.session()

class ConnectnPrinting:
    """
    Instantiates the nPrinting connection class
    """

    def __init__(self, server, root = False
        , userid = False, credential = False, password = False):
        """
        Establishes connectivity with Qlik Sense Repository Service
        :param server: servername.domain:4242
        :param userid: user to use for queries
        :param credential: domain\\username for Windows Authentication
        :param password: password of windows credential
        """
        self.server = server
        self.root = root
        self.credential = credential
        self.password = password

    def get(self,endpoint):
        if self.credential is not False:
            session.auth = HttpNtlmAuth(self.credential, self.password, session)
            headers['User-Agent'] = 'Windows'   
            response = session.get('https://{0}/{1}'.format (self.server, endpoint),
                                        headers=headers, verify=self.root)
            return response.content

    def delete(self,endpoint):     
        response = session.delete('https://{0}/{1}'.format (self.server, endpoint),
                                    headers=headers, verify=self.root)
        print (response.url)
        return response.content

    def post(self, endpoint, data=None):

        response = session.post('https://{0}/{1}'.format (self.server, endpoint),
                                    headers=headers, verify=self.root, data=data)
        return response.status_code

    def auth(self):
        path = 'login/ntlm'
        return json.loads(self.get(path))
        
    def get_apps(self, appid = None):
        path = 'apps'
        if appid:
            path += '/{0}'.format (appid)
        return json.loads(self.get(path))

    def get_filters(self, filterid = None):
        path = 'filters'
        if filterid:
            path += '/{0}'.format (filterid)
        return json.loads(self.get(path))

    def get_ondemandrequests(self, requestid = None, result = None):
        path = 'ondemand/requests'
        if requestid:
            path += '/{0}'.format (requestid)
            if result:
                path += '/result'
        return json.loads(self.get(path))

    def get_reports(self, reportid = None):
        path = 'reports'
        if reportid:
            path += '/{0}'.format (reportid)
        return json.loads(self.get(path))   

    def delete_ondemandrequest(self,requestid):
        path = 'ondemand/requests/{0}'.format(requestid)
        return self.delete(path)

    def post_ondemandrequest(self, reportid):
        path = 'ondemand/requests'
        data = {'type': 'report',
                'config': {'reportId': reportid},
                            'outputFormat': 'PDF'}
        json_data = json.dumps(data)
        return self.post(path, data)

if __name__ == '__main__':
    np = ConnectnPrinting(server='np1.qliklocal.net:4993/api/v1', 
                    credential='qliklocal\\administrator',
                    password='Qlik1234')
    
    np.auth()


