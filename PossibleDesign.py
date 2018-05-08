import requests
import xml.etree.ElementTree as ET
from functools import wraps
from pprint import pprint

def encode_to_ascii(text):
        """encode text to ascii"""
        return text.encode('ascii', errors="backslashreplace").decode('utf-8')

# --- max upload size for single request
FILESIZE_LIMIT = 1024 * 1024 * 64

# --- larger workbooks need to be split
CHUNK_SIZE = 1024 * 1024 * 5


##################################
###### Memory Storage Class ######
class MemoryStruct:
    """storage class"""
    # --- must be updated as new versions are released
    VERSION = {"8.3": "2.0", "9.0": "2.0", "9.1": "2.0",
               "9.2": "2.1", "9.3": "2.2",
               "10.0": "2.3", "10.1": "2.4", "10.2": "2.5",
               "10.3": "2.6", "10.4": "2.7", "10.5": "2.8"}
    URL_STEM = "http://"
    xmlns = {'t': 'http://tableau.com/api'}

    AUTH = dict()
    SITES = dict()
    TOKENS = dict()
    PROJECTS = dict()
    REVISIONS = dict()
    WORKBOOKS = dict()
    PERMISSIONS = dict()
    DATASOURCES = dict()
    USER_GROUPS = dict()
    SUBSCRIPTIONS = dict()
    JOBS_TASKS_SCHEDULES = dict()

    @classmethod
    def check(cls, dict_name: str):
            if dict_name in list(__class__.__dict__.keys()):
                    print("{} found in {}".format(dict_name,
                                                  __class__.__name__))
            else:
                    print("{} not in {}".format(__class__.__name__))

    @classmethod
    def updateMemoryStruct(*args, name: str, keyname: str):
            if name in list(__class__.__dict__.keys()):
                    print("{} found in {}".format(name,
                                                  __class__.__name__))
                    __class__.__dict__.get(str(name)).update({str(keyname):
                                                           a for a in args})
            else:
                    print("{} not in {}".format(__class__.__name__))

##########################
###### Server class ######
class Server(MemoryStruct):
    """Server class"""

    def __init__(self, server: str, username: str, password: str):
        self.server_ = server
        self.username_ = username
        self.password_ = password
        self.temp_url = None
        self.temp_xml = None
        self.version = None

        super().__init__()

    def signin(self, version: str):
             """sign into specified tableau server"""
             url = self.URL_STEM + "{}/api/{}/auth/signin".format(self.server_,
                                                self.VERSION.get(version))
             self.temp_url = url
             self.version = self.VERSION.get(version)
             self.updateMemoryStruct(url,name='AUTH', keyname='sign_in url')

    def generate_xml(self, contenturl=None):
            """create xml string that will be passed to the REST api"""
            xml_request = ET.Element('tsRequest')
            credentials = ET.SubElement(xml_request, 'credentials',
                                        name=self.username_,
                                        password=self.password_)
            ET.SubElement(credentials, 'site', contentUrl='')
            sign_in_xml = ET.tostring(xml_request)
            self.temp_xml = sign_in_xml
            self.updateMemoryStruct(sign_in_xml, name='AUTH',
                                    keyname='sign_in xml')

    # --- log into server
    def loginRequest(self):
             """make login request to tableau server"""
             global encode_to_ascii
             #encoded_response = encode_to_ascii()

             # --- response should be 200 status code for login success
             server_response = requests.post(self.AUTH.get('sign_in url'),
                                             data=self.AUTH.get('sign_in xml'))
             if server_response.status_code == 200:
                     print("login successful: status code[{}]".format(server_response.status_code))
                     encoded_response = encode_to_ascii(server_response.text)
                     parsed_response = ET.fromstring(encoded_response)
                     auth_token = parsed_response.find('t:credentials', namespaces=self.xmlns).get('token')
                     site_token = parsed_response.find('.//t:site', namespaces=self.xmlns).get('id')
                     uid_token = parsed_response.find('.//t:user', namespaces=self.xmlns).get('id')
                     self.updateMemoryStruct(auth_token, name='AUTH', keyname='auth token')
                     self.updateMemoryStruct(site_token, name='AUTH', keyname='site token')
                     self.updateMemoryStruct(uid_token, name='AUTH', keyname='uid token')
             else:
                     print("login failed: status code[{}]".format(server_response.status_code))
                     exit(1)

    # --- logout of server
    def logoutRequest(self):
        """logout of the tableau server"""
        sign_out_url = self.URL_STEM + "{}/api/{}/auth/signout".format(self.server_,
                                                                       self.version)
        server_response = requests.post(sign_out_url,
                                         headers={'x-tableau-auth':
                                                  self.AUTH.get('auth token')})
        if server_response.status_code == 204:
            print("logout successful: status code[{}]".format(server_response.status_code))



##################################
###### Workbook Class ############
def Workbooks():

    def __init__(self):
        self.n = N
        m = MemoryStruct()




















def main():
        srvr = Server(server='172.31.32.54', username='Administrator',
                      password='=%vT8AFMj$')

        srvr.signin(version="10.3")
        srvr.generate_xml()
        srvr.loginRequest()     # --- 200 status made
        srvr.logoutRequest()

        w = Workbooks()
        m = MemoryStruct()
        pprint(m.AUTH)

