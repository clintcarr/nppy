# qrspy (Qlik Sense Repository Python)
Python wrapper for nPrinting APIs.

# Instructions
1. ensure requests is installed (pip install requests)
2. ensure requests_ntlm is installed (pip install requests_ntlm)
3. export the qlik sense certificates in PEM format to a local folder
4. launch python
5. import nppy

#Examples

## Instantiate the nPrinting Connect class
- parameter1 = server and port
- parameter5 = userid
- parameter6 = credential (windows domain and userid)
- parameter7 = password (windows password)

### Windows authenticate with Windows Authentication (NTLM)
```
np = nppy.ConnectnPrinting(server = 'np1.qliklocal.net:4993/api/v1', 
                        credential = 'qliklocal\\administrator', 
                        password = 'Qlik1234')
```

## display a list of nPrinting reports
```
print (np.get_reports())
```
## display a single nPrinting report
- parameter1 = reportid
```
print (np.get_reports(guid))
```

## APIs available:


get_reports

get_reports(id) 

get_apps

get_apps(id) 

get_filters

get_filters(id)

delete_ondemandrequest

post_ondemandrequests
