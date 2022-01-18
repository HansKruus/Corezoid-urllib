from corezoidlib import Corezoid


apiToken = 'someverylongtoken'
convId = '66666' #your corezoid convid
convUserId = '33333' #your corezoid convuserid
issync = True #sync or async corezoid api

corezoid = Corezoid(apiToken,convId,convUserId,issync)

timeout = 5
req_type = 2
data = 'some data for corezoid'

dictForCorezoid = {'timeout': timeout, 'ops': [{'type': 'create', 'obj': 'task', 'conv_id': corezoid.getconvid(), 'data': {'req_type': req_type, 'data': data}}]} #this structure could be different, it depends on your corezoid settings or something like this
data,sign,t = self._corezoid.dataPreparator(dictForCorezoid) #here we getting prepared data for corezoid, sign for corezoid and unixtime for corezoid
responce = sendRequest(data,sign,t) #here we sending data to corezoid in correct way, and receiving responce
print(responce)
