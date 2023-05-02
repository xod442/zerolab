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

from pyVmomi import vim
from pyVim.task import WaitForTask
from pyVim.connect import SmartConnect, Disconnect
import ssl
from utility.reset_afc import reset_afc
from utility.reset_psm import reset_psm

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
    #dc_name = 'vlan229appl.hpevlabs.org'
    content = si.RetrieveContent()
    #dc = content.rootFolder.childEntity[0]

    vm_list = content.viewManager.CreateContainerView(content.rootFolder,
                                                     [vim.VirtualMachine],
                                                     True)
    vm_data = vm_list.view

    # Get a list of all snapshots for each VM
    afc_default_snapshot = "Base-with-licenses-ip-address"
    psm_default_snapshot = "Pensando-02-clean-freshboot"


    for vm in vm_data:
        if vm.snapshot:
            snapshot_list = vm.snapshot.rootSnapshotList
            if snapshot_list:
                for snapshot in snapshot_list:
                    if snapshot.name == afc_default_snapshot:
                        message = reset_afc(snapshot.snapshot)
                        print(message)
                    if snapshot.name == psm_default_snapshot:
                        message = reset_psm(snapshot.snapshot)
                        print(message)





# Start program
if __name__ == "__main__":
    main()
