import os
import string
def readf(filelocation, file_name) :
    os.chdir(filelocation)
    f = open(file_name, 'r')
    rfile = f.read()
    f.close()
    return rfile

def dic(key) :
    Ua = string.ascii_uppercase
    La = string.ascii_lowercase
    dic = {}
    for i in Ua :
        dic[i] = Ua[key]
        dic[i.lower()] = La[key]
        key += 1
        if key > 25 :
            key = 0
    return dic

def encryp(rfile , dic) :
    text = ''
    for i in rfile :
        if i == '\n' or i not in dic:
            text = text+i
        else :
            text += dic[i]
    return text

def save(text , save_location, export_name) :
    os.chdir(save_location)
    f = open(export_name, 'w')
    f.write(text)
    f.close()
    print('encrypted and saved')


def hide(file_name , export_name , key = 0,  filelocation = os.getcwd() , save_location = os.getcwd()  ):
    rf = readf(filelocation, file_name)
    d = dic(key)
    txt = encryp(rf , d )
    save(txt , save_location , export_name)

def appear(file_name , export_name , key = 0 , filelocation = os.getcwd() , save_location = os.getcwd() ) :
    key = -1 * key
    rf = readf(filelocation, file_name)
    d = dic(key)
    txt = encryp(rf , d )
    save(txt , save_location , export_name)
