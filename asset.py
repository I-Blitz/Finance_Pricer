import numpy as np

#### class asset ####

class asset:
    ## S_t = S_0 * exp( (r-sigma**2/2)*T + sigma*W_T )
    def __init__(self,r = 0.01, sigma = 0.2, S0 = 100):
        self.r = r
        self.sigma = sigma
        self.S0 = S0

        
    def get_r(self):
        return(self.r)
    
    def get_sigma(self):
        return(self.sigma)
    
    def get_S0(self):
        return(self.S0)
    
    def show(self):
        S0 = self.get_S0()
        r = self.get_r()
        sigma = self.get_sigma()
        
        print("S0 = {}".format(S0))
        print("r = {}".format(r))
        print("sigma = {}".format(sigma))
    
    def get_price(self,t,G = np.random.normal()):
        S0 = self.get_S0()
        r = self.get_r()
        sigma = self.get_sigma()
        
        return(S0*np.exp((r-sigma**2/2)*t + sigma*np.sqrt(t)*G))

        
        
        