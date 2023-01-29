from asset import *
import numpy as np

class option:
    
    def __init__(self,payoff, S = asset(), kind = 'european', path_dependant = False,T = 1, K = 100):
        self.S = S # underlying 
        self.kind = kind # european vs bermudian vs american
        self.path_dependant = path_dependant #true if is not path dependant 
        self.payoff = payoff # payoff
        self.T = T # maturity
        self.K = K # strike
        
    def price(self,t,MC = 1000, method = 'MonteCarlo'):
        if (method == 'MonteCarlo'):
            return(self.pricing_by_MC(t,MC))
        else:
            print("pas encore implémenté")
        
    def pricing_by_MC(self,t, MC = 1000):
        r = self.S.get_r()
        T = self.T
        K = self.K
        
        if (self.path_dependant == False ): ## C_t = np.exp(-r(T-t)) E[payoff(S_T, ...)]
            G = np.random.normal(size = MC)
            ST = self.S.get_price(T,G)
            
            PAYOFF = self.payoff(ST,K)
            s = np.std(PAYOFF)
            price = np.mean( np.exp(-r*(T-t))*PAYOFF )
            IC = [price-1.96*s/np.sqrt(MC),price+1.96*s/np.sqrt(MC)]
            
            return(price,IC)
        else:
            print("pas implémenté")
              