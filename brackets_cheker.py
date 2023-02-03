import random

def gen():
    return ['(' if x>0.5  else ')' for x in [random.random() for _ in range(6)]]
class Stack:
    def __init__(self, txt):
        self._prev = list()
        self.result = self.valid(txt)
        
    def valid(self, txt):
        for k, v in enumerate(txt):
            res = self.checker(k, v, len(txt))
            if not res:
                return False
        return True
            
    def checker(self, ind, val, _len):
        if ind == _len-1 and val == '(': return False
        elif len(self._prev)>1 and ind == _len-1: return False
        elif not len(self._prev) and val == ")":
            return 0
        elif val == '(':
            self._prev.append(1)
            return 1
        else:
            self._prev.pop()
            return 1                 

attempts = 0      

while True:
    attempts += 1
    if Stack(a:=gen()).result:
        print(f'Match! it take just {attempts} attempts')
        print(*a)
        break
