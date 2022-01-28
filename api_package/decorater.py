from functools import wraps
import time

def runtime_check(program, coder):
    # 第二層回傳帶入func
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            """""""""
            args[0] = url
            args[1] = GET or POST  //required//
            args[2] = [send value(data)]
            args[3] = [send value(json)]
            args[4] = [send params]
            args[5] = file
            args[6] = file_path
            args[7] = runtime
            """""""""
            # Input Param First
            print(f"Coder: {coder}")
            print('')
            print('*' * 8)
            while True:
                work_type = input("請輸入測試類型(`json` or `handinput`): ")
                if work_type:
                    if work_type != 'handinput' and work_type != 'json':
                        print('請輸入 `handinput` or `json` 兩種測試類型二選一')
                    else:
                        break
                else:
                    print('您輸入的值為空請在試一次')

            if work_type == 'handinput':
                url = input("測試網址: ")
                while True:
                    method = input("接收方式(GET or POST): ")
                    if method:
                        if method != 'GET' and method != 'POST':
                            print('請輸入 `GET` or `POST` 兩種測試類型二選一')
                        else:
                            break
                    else:
                        print('您輸入的值為空請在試一次')
                
                while True:
                    header = input("header參數: ")    
                    data = input("data參數: ")
                    json = input("json參數: ")
                    params = input("params參數: ")
                    try:
                        check = lambda x: '{"default":"value"}' if ( x is '') else x
                        check_params = lambda x: '' if (x is '') else x
                        header = check(header)
                        data = check(data)
                        json = check(json)
                        params = check(params)
                        
                        header = eval(header)
                        data = eval(data)
                        json = eval(json)
                        params = eval(params)
                        break
                    except Exception as e:
                        print(e)
                        print('參數格式錯誤 Ex: {"Key": "Value"}')
                
                if not params:
                    params = ''

                files = input("files參數: ")
                runtime = input("請輸入要執行次數: ")
                print('*' * 8)
                print('')
                # Start Program
                start = time.time()
                func(work_type, url, method, header, data, json, params, files, runtime)
                end = time.time()
                print(f"{program}: 用時 {round(end - start, 2)} 秒")
                return "OK"

            elif work_type == 'json':
                print('*' * 8)
                print('')
                # Start Program
                start = time.time()
                func(work_type)
                end = time.time()
                print('')
                print('*'*8)
                print(f"{program}: 用時 {round(end - start, 2)} 秒")
                return "OK"
        return inner_wrapper
    return wrapper