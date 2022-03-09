import twint
import pandas as pd

c = twint.Config()

c.Username = 'dairycom'
c.Custom["tweet"] = ["id"]
c.Custom["user"] = ["bio"]
c.Search = 'dairy'
c.Store_csv = True  
c.Output = ('/home/ranjeet/Desktop/test.csv')
c.Limit = 10
twint.run.Search(c)
#df = pd.read_csv("/home/ranjeet/Desktop/test.csv")