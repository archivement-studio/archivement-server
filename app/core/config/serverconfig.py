import os
import yaml

class ServerConfig():
    def __init__(self, build):
        file_path = "resources/env/application-"+build+".yml"
        with open(file_path, 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            server = data['server']
            server_status = server['status']
            server_url = server['url']
            
            os.environ['server_status'] = server_status 
            os.environ['server_url'] = server_url
