# syslog-python
Remote Syslog Python logger

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

