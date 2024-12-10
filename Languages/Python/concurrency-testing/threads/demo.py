import threading
import random
import time
from typing import List
import uuid

def download(filename:str) -> bool:
    print("inside download()")
    time.sleep(random.randint(0,1))
    print("Finishing download()")
    return random.choice([True, False])

def sign_for_docment(name:str, token:str) -> bool:
    print("inside sign_for_docment()")
    time.sleep(random.randint(0,1))
    print("Finishing sign_for_docment()")
    return random.choice([True, False])

def get_file_urls(filenames:List[str], result:List[str]) -> List[str]:
    print("inside get_file_urls()")
    time.sleep(random.randint(4,15))
    for file in filenames:
        result.append(f"/path/to/{file}")
    print("Finishing get_file_urls()")
    return result

def download_files(fileURLs:list[str]):
    print("inside download_files()")
    for url in fileURLs:
        download(url)
    print("Finishing download_files()")

def sign(name:str, token:str) -> bool:
    print("inside sign()")
    isValid = sign_for_docment(name, token)
    print("Finishing sign()")
    return isValid

def ask_user_for_name() ->str:
    print("inside ask_user_for_name()")
    print("Finishing ask_user_for_name()")
    return "name"
    
def get_token_by_name(name:str) -> str:
    print("inside get_token_by_name()")
    print("Finishing get_token_by_name()")
    return str(uuid.uuid4())
    
if __name__ == "__main__":
    filenames = ["file1.png", "file2.jpg", "file3.docx"]
    result = []
    thread = threading.Thread(target=get_file_urls, args=(filenames,result))
    thread.start()
    print("thread is running!")
    name = ask_user_for_name()
    token = get_token_by_name(name)
    valid = sign(name, token)
    if valid:
        thread.join()
        print("thread is done!")
        download_files(result)
    else:
        raise Exception("Unable to sign for files")