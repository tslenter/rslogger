#!/bin/python3

#License:
#"rslogger" is a free application that can be used to send syslog messages from python to Remote Syslog.
#Copyright (C) 2021 Tom Slenter
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#For more information contact the author:
#Name author: Tom Slenter
#E-mail: info@remotesyslog.com

import socket

#Create dictionary for facility and log level:
#Log level and facility can be found here:
#https://success.trendmicro.com/solution/TP000086250-What-are-Syslog-Facilities-and-Levels

fcl = {
    'kern': 0, 'user': 1, 'mail': 2, 'daemon': 3,
    'auth': 4, 'syslog': 5, 'lpr': 6, 'news': 7,
    'uucp': 8, 'cron': 9, 'authpriv': 10, 'ftp': 11,
    'ntp': 12, 'log_audit': 13, 'log_alert': 14, 'clock_daemon': 15,
    'local0': 16, 'local1': 17, 'local2': 18, 'local3': 19,
    'local4': 20, 'local5': 21, 'local6': 22, 'local7': 23
}

lvl = {
    'emerg': 0, 'alert':1, 'crit': 2, 'err': 3,
    'warning': 4, 'notice': 5, 'info': 6, 'debug': 7
}

#Function to send stream, by default it send a test message to the localhost => port 514
def syslog(message='Test is RS test message to localhost', level=lvl['notice'], facility=fcl['daemon'], host='localhost', port=514):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    extlvl = (level, (list(lvl.keys())[list(lvl.values()).index(level)]))
    level_num = str(extlvl[0])
    level_str = str(extlvl[1])
    extfct = (facility, (list(fcl.keys())[list(fcl.values()).index(facility)]))
    facility_num = str(extfct[0])
    facility_str = str(extfct[1])
    calc=int(facility_num)*7+int(level_num)+int(facility_num)
    data = '<'+ str(calc) + '>' + 'rslogger' + ': ' + facility_str + ': ' + level_str + ': ' + "rslogger_output: " + message
    sock.sendto(data.encode(), (host, port))
    sock.close()

#Run the function:
#Run test to local host as default
#syslog()

#Run test to server
#message=str('Hello world')
#syslog(message, level=lvl['notice'], facility=fcl['log_audit'], host='172.16.201.2', port=514)
