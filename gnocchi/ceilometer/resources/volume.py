#
# Copyright 2015 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ceilometer.openstack.common import log

from gnocchi.ceilometer.resources import base

LOG = log.getLogger(__name__)


class Volume(base.ResourceBase):
    @staticmethod
    def get_resource_extra_attributes(sample):
        metadata = sample['resource_metadata']
        params = {
            "display_name": metadata['display_name'],
        }
        return params

    @staticmethod
    def get_metrics_names():
        return ['volume',
                'volume.size',
                'volume.create',
                'volume.delete',
                'volume.update',
                'volume.resize',
                'volume.attach',
                'volume.detach',
                ]
