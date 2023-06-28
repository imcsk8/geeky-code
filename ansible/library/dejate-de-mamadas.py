#!/usr/bin/python

# Copyright: (c) 2022, Iván Chavero <ichavero@chavero.com.mx>
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
# from ansible.module_utils.basic import *
from ansible.module_utils.basic import AnsibleModule
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dejate-de-mamadas

short_description: Módulo de broma para código de playera

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: Módulo de broma para código de playera

options:
    name:
        description: This is the message to send to the test module.
        required: true
        type: str
    value:
        description: Just a value
        required: true
        type:  str

author:
    - Iván Chavero (@imcsk8)
'''

EXAMPLES = r'''
# Show message as warning
  - name: A ver pinche Ansible
    dejate-de-mamadas:
      name: Quiero que jale
      value: y hazle como puedas
'''

RETURN = r'''
# These are examples of possible return values, and in general should use
# other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
'''


def run_module():
    module_args = dict(
        name=dict(type='str', required=True),
        value=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        original_message=module_args['name'],
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True, no_log=False
    )
    if module.check_mode:
        module.exit_json(**result)

    result['message'] = f"{module.params['name']} y {module.params['value']}"
    result['changed'] = True
    module.warn(result['message'])
    module.warn("Soy ansible y fallaré aunque no lo indique en rojo")
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
