from urllib import request, parse
import time
import json
import sys
import hashlib

class Corezoid():
        def __init__(self, apiToken, convId, convUserId, issync, overridedUrl = None):
                self._convId=convId
                self._convUserId=convUserId
                self._apiToken=apiToken
                if overridedUrl is None:
                    if (issync):
                        self._url='https://sync-api.corezoid.com/api/1/json/'
                    else:
                        self._url='https://api.corezoid.com/api/1/json/'
                else:
                    self._url=overridedUrl

        def unixtime(self):
                return int(time.time())

        def dataPreparator(self, datain):
                data=json.dumps(datain)
                data=str(data)
                utime=self.unixtime()
                rawsign=(str(utime) + self._apiToken + data + self._apiToken).encode('utf-8')
                return data.encode('utf-8'), hashlib.sha1(rawsign).hexdigest(), str(utime)

        def sendRequest(self, data, sign, t):
                query=request.Request('{}{}/{}/{}'.format(self._url,self._convUserId,t,sign), data=data)
                query.add_header('Content-Type', 'application/json')
                response=request.urlopen(query)
                return json.loads(response.read().decode('utf-8'))

        def getconvid(self):
                return self._convId
