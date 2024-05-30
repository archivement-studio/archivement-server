# Server
from app.main import create_app

# Setting
import sys
import uvicorn
from typing import Optional
import os
from app.core.config.serverconfig import ServerConfig

# Test
from test.base import testFunc

# Test
from app.test.base import testFunc

def run_server(host: Optional[str] = None, port: Optional[int] = None, build:str = "dev") -> None:
    ServerConfig(build)

    host = host or "0.0.0.0"
    port = port or 8080
    app = create_app()

    print("host:",host,"port:",port);
    uvicorn.run(app, host=host, port=port)

def test():
    testFunc()

def main():
    input_ = sys.argv
    
    prompt = "_".join(input_[1:])
    
    #runserver
    if prompt == "runserver": run_server()
        
    #runserver prod
    if prompt == "runserver_prod": run_server(build=input_[2])

    if prompt == "test": test()

    #other
    else: raise Exception('Not Command')


if __name__=="__main__":
    main()