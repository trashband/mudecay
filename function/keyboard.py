import sys
sys.path.insert(0, '/root/mudecay/')
import func

def event_keyboards(data):
    i=0
    result = ''
    while i <= len(func.event):
        i+=1
        if data in func.event[i]['name']:
            result += func.event[i]['FullName'] + '\n'
        if(i==42):
            break
    return result
    


print(event_keyboards('Selupan'))