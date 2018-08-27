import threading
import requests
def getUrlForStudentList(collegeid):
    url='http://127.0.0.1:8000/onlineapp/studentserialize/'+str(collegeid)
    reqs=requests.get(url)
    print(threading.current_thread().getName(),reqs.json())

class producerThread():
    def __init__(self):
        self.






t1=threading.Thread(target=getUrlForStudentList,args=(2,))
t2=threading.Thread(target=getUrlForStudentList,args=(3,))

t1.start()
t2.start()
t1.join()
t2.join()