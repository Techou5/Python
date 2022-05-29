import subprocess
import os
import sys
import requests
import json
import urllib3
import tkinter as tk
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

form = tk.Tk()

form.geometry("800x800")

name_var=tk.StringVar()
email_var=tk.StringVar()
user_var=tk.StringVar()
password_var=tk.StringVar()
accttype_var=tk.StringVar()
domainname_var=tk.StringVar()
#domainid_var=tk.StringVar()
ownerpleskuser_var=tk.StringVar()
ownerpleskpass_var=tk.StringVar()
#ownerservuser_var=tk.StringVar()
#ownerservpass_var=tk.StringVar()

def submit():

    #Define field variables for use in API
    custname=name_var.get()
    custemail=email_var.get()
    user=user_var.get()
    custpassword=password_var.get()
    accttype=accttype_var.get()
    domainname=domainname_var.get()
    #domainid=domainid_var.get()
    ownerpleskuser=ownerpleskuser_var.get()
    ownerpleskpass=ownerpleskpass_var.get()
    #ownerservuser=ownerservuser_var.get()
    #ownerservpass=ownerservpass_var.get()

    #Define API Variables
    
    header={"Accept": "*/*",
                "Content-Type": "application/json"}
                #"X-API-Key": "APIKEY"}
    url="PLESKURL"
    createcusturl="PLESKURL/api/v2/clients"
    custreqbody={
        "name": custname,
        "login": user,
        "status": 0,
        "email": custemail,
        "locale": "en-US",
        "description": "Test",
        "password": custpassword,
        "type": accttype
        }

    response=requests.request('POST', createcusturl, auth=(ownerpleskuser, ownerpleskpass), headers=header,
                         data=json.dumps(custreqbody), verify=False)
    
    api_data=response.json()
    custid=print(api_data['id'])
    custguid=print(api_data['guid'])

    createdomainurl="PLESKURL/api/v2/domains"

    domaincreatebody={

        "name": domainname,
        "hosting_type": "virtual",
        "hosting_settings": {
        "ftp_login": "test_log068430911751",
        "ftp_password": "changeme1Q$**"
        },
        "owner_client": {
        "id": custid,
        "login": user,
        "guid": custguid
        },
        "ip_addresses": [
        "PLESKIP"
        ],
        "ipv4": [
        "PLESKIP"
        ],
        "plan": {
        "name": "Default Domain"
        }
    }

    response=requests.request('POST', createdomainurl, auth=(ownerpleskuser, ownerpleskpass), headers=header,
                         data=json.dumps(domaincreatebody), verify=False)
    
    print(response.status_code)
    print(response.json())
    name_var.set("")
    email_var.set("")
    user_var.set("")
    password_var.set("")
    accttype_var.set("")
    domainname_var.set("")
    #ownerpleskuser_var.set("")
    #ownerpleskpass_var.set("")
    p=subprocess.Popen(["powershell.exe", "C:\\Users\\14699\\Documents\\PythonScripts\\pleskrdp.ps1"], stdout=sys.stdout)
    p.communicate()
    print(user)
    print(custpassword)

#Format Label and Entry fields in form
name_label = tk.Label(form, text='Customer Full Name', font=('calibre', 12, 'bold'))
name_entry = tk.Entry(form,textvariable = name_var, font=('calibre',10,'normal'))

email_label = tk.Label(form, text='Customer Email', font=('calibre', 12, 'bold'))
email_entry = tk.Entry(form,textvariable = email_var, font=('calibre',10,'normal'))

user_label = tk.Label(form, text='Customer Username', font=('calibre', 12, 'bold'))
user_entry = tk.Entry(form,textvariable = user_var, font=('calibre',10,'normal'))

password_label = tk.Label(form, text='Customer Password', font=('calibre', 12, 'bold'))
password_entry = tk.Entry(form,textvariable = password_var, font=('calibre',10,'normal'))

accttype_label = tk.Label(form, text='Customer Account Type', font=('calibre', 12, 'bold'))
accttype_entry = tk.Entry(form,textvariable = accttype_var, font=('calibre',10,'normal'))

domainname_label = tk.Label(form, text='Customer Domain Name', font=('calibre', 12, 'bold'))
domainname_entry = tk.Entry(form,textvariable = domainname_var, font=('calibre',10,'normal'))

#domainid_label = tk.Label(form, text='Customer Domain ID', font=('calibre', 12, 'bold'))
#domainid_entry = tk.Entry(form,textvariable = domainid_var, font=('calibre',10,'normal'))

ownerpleskuser_label = tk.Label(form, text='Owner Plesk Username', font=('calibre', 12, 'bold'))
ownerpleskuser_entry = tk.Entry(form,textvariable = ownerpleskuser_var, font=('calibre',10,'normal'))

ownerpleskpass_label = tk.Label(form, text='Customer Plesk Password', font=('calibre', 12, 'bold'))
ownerpleskpass_entry = tk.Entry(form,textvariable = ownerpleskpass_var, font=('calibre',10,'normal'))

#ownerservuser_label = tk.Label(form, text='Owner Server Username', font=('calibre', 12, 'bold'))
#ownerservuser_entry = tk.Entry(form,textvariable = ownerservuser_var, font=('calibre',10,'normal'))

#ownerservpass_label = tk.Label(form, text='Owner Server Password', font=('calibre', 12, 'bold'))
#ownerservpass_entry = tk.Entry(form,textvariable = ownerservpass_var, font=('calibre',10,'normal'))

sub_btn=tk.Button(form,text = 'Submit', command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
email_label.grid(row=1, column=0)
email_entry.grid(row=1, column=1)
user_label.grid(row=2, column=0)
user_entry.grid(row=2, column=1)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
accttype_label.grid(row=4, column=0)
accttype_entry.grid(row=4, column=1)
domainname_label.grid(row=5, column=0)
domainname_entry.grid(row=5, column=1)
#domainid_label.grid(row=6, column=0)
#domainid_entry.grid(row=6, column=1)
ownerpleskuser_label.grid(row=7, column=2)
ownerpleskuser_entry.grid(row=7, column=3)
ownerpleskpass_label.grid(row=8, column=2)
ownerpleskpass_entry.grid(row=8, column=3)
#ownerservuser_label.grid(row=10, column=2)
#ownerservuser_entry.grid(row=10, column=3)
#ownerservpass_label.grid(row=11, column=2)
#ownerservpass_entry.grid(row=11, column=3)
sub_btn.grid(row=30,column=2)
#Loop form so it stays up
form.mainloop()
