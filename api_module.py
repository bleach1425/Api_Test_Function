import requests
import json
import os
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
                print("Runtime:", run + 1)
                print(r.status_code, r.text)
                print("Response Code: ",  r.status_code)
                print("Response Text: ",  r.text)

        elif self.method == "POST":
            for run in range(int(self.runtime)):
                r = requests.post(self.url, data= self.data, files=self.file, headers= self.header, json=self.json, params=self.param)
                print("Runtime:", run + 1)
                print("Response Code: ",  r.status_code)
                print("Response Text: ",  r.text)

    
    @staticmethod
    def api_test_json(Url, Method, Header, Data, Json, Param, File, Runtime):
        print("Method: ", Method)
        print("")
        if Method == "GET":
            for run in range(int(Runtime)):
                print("Runtime:", run + 1)
                r = requests.get(Url, data= Data, files=File, headers=Header, json=Json, params=Param)
                print(r.status_code, r.text)
                print("Response Code: ",  r.status_code)
                print("Response Text: ",  r.text)
                print("")

        elif Method == "POST":
            for run in range(int(Runtime)):
                print("Runtime:", run + 1)
                r = requests.post(Url, data= Data, files=File, headers=Header, json=Json, params=Param)
                print("Response Code: ",  r.status_code)
                print("Response Text: ",  r.text)
                print("")


def mkdir_example():
    with open('./api_test.json', mode='w') as f:
        data = {
            "Url":"",
            "Method": "",
            "Header": {},
            "Json": {},
            "Param": {},
            "Data": {},
            "Runtime": 1
        }
        json.dump(data, f)
        f.close()


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
            5. [send params]
            6. file  
            7. runtime
            '''
            data = json.load(f)
            print("data: ", data)
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
