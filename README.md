## 1. License

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

## 2. Requirements:
- Remote Syslog core or other syslog listener must be running as minimum
- Python script below has the same path as the running python script

## 3. Instruction of usage:

### 3.1 Usage:
Python rslogger can be used to write important lines of informational logging from a python script to a remote syslog server. We found it usefull as we run multiple scripts on different hosts. With this we track the given info on a central / remote server.

### 3.2 Available facility:
kern, user, mail, daemon, auth, syslog, lpr, news, uucp, cron, authpriv, ftp, ntp, log_audit, log_alert, clock_daemon, local0, local1, local2, local3, local4, local5, local6, local7

### 3.3 Available levels:

emerg, alert, crit, err, warning, notice, info, debug

### 3.4 How to add:
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

## 4. Donation

Crypto:

```
XRP/Ripple: rHdkpJr3qYqBYY3y3S9ZMr4cFGpgP1eM6B
BTC/Bitcoin: 1JVmexqGBQyGv9fVkSynHapi2U6ZCyjTUJ
LTC/Litecoin Segwit: MAH8ATCK6X7biiTQrW7jUZ6L9eg1YBo5qS
ETH/Ethereum: 0xd617391076F9bEa628f657606DEAB7a189199AF5
```
PayPal:

[![paypal](https://www.paypalobjects.com/en_US/NL/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=KQKRPDQYHYR7W&currency_code=EUR&source=url)

## 5. Help

To improve the code and functions we like to have you help. Send your idea or code to: info@remotesyslog.com or create a pull request. We will review it and add it to this project.
