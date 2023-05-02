#!/usr/bin/env python3

# Released under MIT License
'''
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to
do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Written by Rick Kauffman
Github: https://github.com/xod442/zero.git

Note: Example code For testing purposes only
vSphere Python SDK program to perform snapshot operations
'''

import sys
#from tools import cli, pchelper, service_instance
from pyVmomi import vim
from pyVim.task import WaitForTask
from pyVim.connect import SmartConnect, Disconnect
import ssl
import os

host="192.168.229.245"
user="arubatm@vsphere.local"
password="Aruba123!@#"
port="443"

sslContext = ssl._create_unverified_context()

def main():
    # connect to vSphere
    si = SmartConnect(
        host=host,
        user=user,
        pwd=password,
        port=port,
        sslContext=sslContext
    )
    print(si.CurrentTime())

    # get the datacenter object
    dc_name = 'vlan229appl.hpevlabs.org'
    content = si.RetrieveContent()
    dc = content.rootFolder.childEntity[0]

    # get all virtual machines in the datacenter
    vm_view = content.viewManager.CreateContainerView(
        container=dc,
        type=[vim.VirtualMachine],
        recursive=True
    )
    vms = vm_view.view
    #vm_view.Destroy()
    for v in vms:
        print(v)

# Start program
if __name__ == "__main__":
    main()
