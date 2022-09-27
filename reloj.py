

def inicio():
    h = 0
    m = 0
    s = 0
    return h, m, s
    
    
def validar():
    h,m,s = inicio()
    limites = 59
    limitem = 60
    limiteh = 24
    
    while h < limiteh:
        if s == limites:
            s = 0
            m = m + 1
            if m == limitem:
                m = 0
                h = h + 1 
                
        s = s + 1
        if  h < limiteh:
            
           print(f'la hora es:  {h}:{m}:{s}')                
                
        
    
if __name__ == '__main__':
    validar()