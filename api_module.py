import requests
import json
from api_package.decorater import runtime_check


class Api:
    def __init__(self, *args):
        """""""""
        args[0] = url
        args[1] = GET or POST  //required//
        args[2] = [send value(data)]
        args[3] = [send value(json)]
        args[4] = [send params]
        args[5] = file  
        args[6] = runtime
        """""""""

        print("args: ", args)

        self.url = args[0]
        self.method = args[1]
        self.header = args[2]

        if args[3]:
            self.data = args[3]
        else:
            self.data = ''

        if args[4]:
            self.json = args[4]
        else:
            self.json = ''
        
        if args[5]:
            self.param = args[5]
        else:
            self.param = ''

        if args[6]:
            self.file = {"file": open(args[6], 'rb')}
        else:
            self.file = ''

        if args[7]:
            self.runtime = args[7]
        else:
            self.runtime = 1


    def api_test_handinput(self):
        if self.method == "GET":
            for run in range(int(self.runtime)):
                r = requests.get(self.url, data= self.data, files=self.file, headers= self.header, json=self.json, params=self.param)
                print(r.status_code, r.text)

        elif self.method == "POST":
            for run in range(self.runtime):
                r = requests.post(self.url, data= self.data, files=self.file, headers= self.header, json=self.json, params=self.param)
                print(r.status_code, r.text)

    
    @staticmethod
    def api_test_json(Url, Method, Header, Data, Json, Param, File, Runtime):
        if Method == 'GET':
            for n in range(int(Runtime)):
                r = requests.post(Url, data= Data, files=File, headers=Header, json=Json, params=Param)
                print(r.status_code, r.text)

        elif Method == "POST":
            for n in range(int(Runtime)):
                r = requests.post(Url, data= Data, files=File, headers=Header, json=Json, params=Param)
                print(r.status_code, r.text)



@runtime_check(program='Api測試', coder='John')
def main(*params):
    if params[0] == 'handinput':
        work = Api(params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8])
        print('*'*8)
        print("測試結果:")
        work.api_test_handinput()
        print('*'*8)
        print('')

    elif params[0] == 'json':
        with open('api_test.json', newline='') as f:
            '''
            # Get Params
            1. url
            2. GET or POST  //required//
            3. [send value(data)]
            4. [send value(json)]
            5. = [send params]
            6. = file  
            7. = runtime
            '''
            data = json.load(f)
            # -------------------------- #
            Url = data.get('Url')
            Method = data.get('Method')
            Header = data.get('Header')
            Data = data.get('Data')
            Json = data.get('Json')
            Param = data.get("Param")
            File = data.get("File")
            Runtime = data.get('Runtime')
            # -------------------------- #

            Api.api_test_json(Url, Method, Header, Data, Json, Param, File, Runtime)

if __name__ == '__main__': 
    main()