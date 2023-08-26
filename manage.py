# Server
from app.main import create_app

# Utils
import sys
import uvicorn
from typing import Optional

def run_server(host: Optional[str] = None, port: Optional[int] = None, build:str = "dev") -> None:
    host = host or '0.0.0.0'
    port = port or 8080
    app = create_app()

    print("host:",host,"port:",port);
    uvicorn.run(app, host=host, port=port)

def main():
    input_ = sys.argv
    
    prompt = "_".join(input_[1:])
    
    #runserver
    if prompt == "runserver": run_server()
        
    #runserver prod
    if prompt == "runserver_prod": run_server(build=input_[2])

    #other
    else: raise Exception('Not Command')


if __name__=="__main__":
    main()