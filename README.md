## 1. License

"Syslog-Python" is a free application that can be used to view syslog messages.

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

## 2. Add to scripts as following:
'''
from rspython import syslog
from rspython import fcl
from rspython import lvl
'''

#Run the function:
#Run test to local host as default
syslog()

#Output:
Jul  5 17:02:21 localhost daemon: notice: Test is RS test message to localhost

#Run test to server

message=str('Hello world')

syslog(message, level=lvl['notice'], facility=fcl['log_audit'], host='172.16.201.2', port=514)

#Output:

Jul  5 17:02:21 comp0001.remotesyslog.com log_audit: notice: Hello world
