## 1. Requirements:
- Remote Syslog core or other syslog listener must be running as minimum
- Python script below has the same path as the running python script

## 2. Instruction of usage:

### 2.1 Usage:
Remote Syslog rslogger can be used to write important lines of informational logging from a python script to a remote syslog server. We found it usefull as we run multiple scripts on different hosts. With this we track the given info on a central / remote server. Example use case: automation scripts for device configuration.

Install the python socket module using the following command:
```
pip install socket
```

Get a local copy of this repo:
```
git clone https://github.com/tslenter/rslogger
cd rslogger
#On Windows:
copy rslogger <Directory of the project>
#On Linux
cp rslogger <Directory of the project>
```

### 2.2 Use case example
The following is a demo example that extracts data from a Cisco DNA controller and sends the data string to a syslog socket: 
```
import requests
import os
from requests.auth import HTTPBasicAuth
import urllib3
import argparse
from rslogger import syslog
from rslogger import fcl
from rslogger import lvl

#Disable HTTPS validation
urllib3.disable_warnings()

#Set variables to None
hostname = None
username = None
password = None

#Create HTTP header
headers = {
              'content-type': "application/json",
              'x-auth-token': ""
          }

#Global information
print('Running from directory: ', os.getcwd())

#Add arguments
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--hostname',  help='Enter a hostname or ip of the Cisco DNA Controller', required=True)
parser.add_argument('-u','--username', help='Add a username', required=True)
parser.add_argument('-p', '--password', help='Add a password', required=True)
args = parser.parse_args()

#Extract variables from namespace to global
globals().update(vars(args))

#Generate token for DNA Controller
def dnac_login(host, passwrd, user):
    # Generate token
    BASE_URL = 'https://' + host
    AUTH_URL = '/dna/system/api/v1/auth/token'
    USERNAME = user
    PASSWORD = passwrd

    response = requests.post(BASE_URL + AUTH_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)
    token = response.json()['Token']
    return token

#Extract data from DNA controller
def network_device_list(token, host):
    url = "https://" + host + "/api/v1/network-device"
    headers["x-auth-token"] = token
    response = requests.get(url, headers=headers, verify=False)
    data = response.json()
    for item in data['response']:
        #Feel free to list more information: item["hostname"],item["platformId"],item["softwareType"],item["softwareVersion"],item["upTime"], item["serialNumber"], item["managementIpAddress"]
        message = str("hostname: ")+item["hostname"]
        syslog(message, level=lvl['notice'], facility=fcl['log_audit'], host='172.16.201.2', port=514)

#Login to DNA Controller
if hostname or username or password != None:
    print("Started session on: " + hostname)
    print("Started session with user: " + username)
    login = dnac_login(hostname, password, username)
    network_device_list(login, hostname)
else:
    print("Did you use the parameters to run this command?")
```

### 3.2 Available facility:
kern, user, mail, daemon, auth, syslog, lpr, news, uucp, cron, authpriv, ftp, ntp, log_audit, log_alert, clock_daemon, local0, local1, local2, local3, local4, local5, local6, local7

### 2.3 Available levels:

emerg, alert, crit, err, warning, notice, info, debug

### 2.4 How to add:
```
from rslogger import syslog
from rslogger import fcl
from rslogger import lvl

#Run test message to localhost (a syslog server is needed)
syslog()

#Expected output:
#Jul  5 17:02:21 localhost daemon: notice: Test is RS test message to localhost

#With variables:
message=str('Hello world')
syslog(message, level=lvl['notice'], facility=fcl['log_audit'], host='172.16.201.2', port=514)

#Expected output (syslog server):
#Jul  5 17:02:21 comp0001.remotesyslog.com log_audit: notice: Hello world
```

## 3. Donation

Crypto:

```
XRP/Ripple: rHdkpJr3qYqBYY3y3S9ZMr4cFGpgP1eM6B
BTC/Bitcoin: 1JVmexqGBQyGv9fVkSynHapi2U6ZCyjTUJ
LTC/Litecoin Segwit: MAH8ATCK6X7biiTQrW7jUZ6L9eg1YBo5qS
ETH/Ethereum: 0xd617391076F9bEa628f657606DEAB7a189199AF5
```
PayPal:

[![paypal](https://www.paypalobjects.com/en_US/NL/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=KQKRPDQYHYR7W&currency_code=EUR&source=url)

## 4. Help

To improve the code and functions we like to have you help. Send your idea or code to: info@remotesyslog.com or create a pull request. We will review it and add it to this project.

## 5. License

"rslogger" is a free application that can be used to send syslog messages from python to Remote Syslog.

Copyright (C) 2021 Tom Slenter

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

For more information contact the author:

Name author: Tom Slenter

E-mail: info@remotesyslog.com
