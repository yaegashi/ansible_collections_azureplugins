# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from msrestazure.tools import parse_resource_id, is_valid_resource_id

# Azure SDK parse_resource_id reference:
# https://docs.microsoft.com/en-us/python/api/msrestazure/msrestazure.tools?view=azure-python#parse-resource-id-rid-


def azure_rids(rid, query='', alias='azure_rids'):
    if not is_valid_resource_id(rid):
        raise AnsibleFilterError(
            alias + ': invalid Azure resource id: %s' % rid)
    results = parse_resource_id(rid)
    if query:
        if query not in results:
            raise AnsibleFilterError(
                alias + ': unknown Azure resource id component: %s' % query)
        return results[query]
    return results


class FilterModule(object):
    '''Azure resource id split filter'''

    def filters(self):
        return {
            'azure_rids': azure_rids,
        }
