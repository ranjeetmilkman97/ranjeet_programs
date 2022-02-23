import twint
import pandas as pd

c = twint.Config()

c.Username = 'dairycom'
c.Search = 'dairy'

twint.run.Search(c)


c.Store_csv = True  
c.Output = ('/home/ranjeet/Desktop/test.csv')

df = pd.read_csv("/home/ranjeet/Desktop/test.csv")