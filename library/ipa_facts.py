#!/usr/bin/python
# coding: utf-8 -*-

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

import ConfigParser

DOCUMENTATION = '''
---
module: ipa_facts
short_description:
version_added:
options:
  path:
    required: false
    description: Path of the ipa config file, if not using the default
'''

EXAMPLES = '''
- name: Gather information about a enrolled server
  ipa_facts:

- name: Display the Kerberos realm
  debug: msg="Realm is {{ ipa_realm }}"
'''

RETURN = '''
ipa_realm:
    description: Kerberos realm of the system
    type: string
    returned: always
ipa_basedn
    description: Base DN of the directory
    type: string
    returned: always
ipa_domain
    description: IPA Domain
    type: string
    returned: always
ipa_server
    description: Main IPA server
    type: string
    returned: always
ipa_xmlrpc_uri
    description: IPA XMLRPC URI
    type: string
    returned: always
'''


def main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=False, type='path',
                      default='/etc/ipa/default.conf')
        ),
    )
    params = module.params

    config = ConfigParser.ConfigParser()
    config.read(params['path'])
    ansible_facts = {}
    for (k, v) in config.items('global'):
        ansible_facts['ipa_' + k] = v
    module.exit_json(changed=False, ansible_facts=ansible_facts)

# this is magic, see lib/ansible/module_common.py
from ansible.module_utils.basic import *
main()
