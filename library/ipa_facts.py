#!/usr/bin/python
#coding: utf-8 -*-

# (c) 2016, Michael Scherer <mscherer@redhat.com>
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''

'''

EXAMPLES = '''

'''
import ConfigParser

def main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=False, type='path', default='/etc/ipa/default.conf')
        ),
    )
    params = module.params

    config = ConfigParser.ConfigParser()
    config.read(params['path'])
    ansible_facts = {} 
    for (k,v) in config.items('global'):
        ansible_facts['ipa_' +k] = v
    module.exit_json(changed=False, ansible_facts=ansible_facts)

# this is magic, see lib/ansible/module_common.py
from ansible.module_utils.basic import *
from ansible.module_utils.openstack import *
main()

