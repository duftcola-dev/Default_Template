def check_200(response:dict):
     if response.status_code == 200:
          return True
     return False

def check_201(response:dict):
     if response.status_code == 201:
          return True
     return False

def check_202(response:dict):
     if response.status_code == 202:
          return True 
     return False

def check_400(response:dict):
     if response.status_code == 400:
          return True
     return False

def check_404(response:dict):
     if response.status_code == 404:
          return True 
     return False

def check_412(response:dict):
     if response.status_code == 412:
          return True 
     return False