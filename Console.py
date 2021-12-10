HEADER = '\033[95m'
OKBLUE = '\033[94m'
SUCCESS = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

def Error(text):
    print(FAIL, text, ENDC)

def Header(text):
    print(OKBLUE, text,ENDC)

def Success(text):
    print(SUCCESS, text, ENDC)

def Warning(text):
    print(WARNING, text, ENDC)
