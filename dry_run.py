from py5paisa import FivePaisaClient
import inf
cred={
    "APP_NAME": inf.APP_NAME,
    "APP_SOURCE": inf.APP_SOURCE,
    "USER_ID": inf.USER_ID,
    "PASSWORD": inf.PASSWORD,
    "USER_KEY": inf.USER_KEY,
    "ENCRYPTION_KEY": inf.ENCRYPTION_KEY,
    }

client = FivePaisaClient(email=inf.email, passwd=inf.passwd, dob=inf.dob,cred=cred)
client.login()
# print(client.margin())