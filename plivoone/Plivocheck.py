import plivo
from plivo import plivoxml
client1 = plivo.RestClient(auth_id='MAODUZYTQ0Y2FMYJBLOW', auth_token= 'Mzk0MzU1Mzc3MTc1MTEyMGU2M2RlYTIwN2UyMzk1')
#before sending message pricing details
response = client1.pricing.get(
    country_iso='US', )
print(response)
#send message
try:
	response = client1.messages.client.messages.create(
    src='17609915566',
    dst='+919632177695',
    text='Hello, world!')
	print(response.__dict__)
	print(str(response['message_uuid']))#print messageUUID
	#get the message detsils using above id
	response = client1.messages.get(
    message_uuid=str(response['message_uuid']), )
	print(response)
except plivo.exceptions.PlivoRestError as e:
	print(e)
	

#after sending message price details we can retive based on message sucess.but due to account expise i am getting credit limit expire error
response = client1.pricing.get(
    country_iso='US', )
print(response)
#after sending message account details
response = client1.account.get()
    
print(response)#we can validate by comparing str(response['cash_credits']) like every attribute

#now from responce restrive the message vallidate the required values.

