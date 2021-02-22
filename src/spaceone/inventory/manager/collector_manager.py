__all__ = ['CollectorManager']

import time
import logging
from spaceone.core.manager import BaseManager
from spaceone.inventory.connector import ECSConnector
from spaceone.inventory.manager.ec2 import EC2InstanceManager, AutoScalingGroupManager, LoadBalancerManager, \
    DiskManager, NICManager, VPCManager, SecurityGroupManager, CloudWatchManager
from spaceone.inventory.manager.metadata.metadata_manager import MetadataManager
from spaceone.inventory.model.server import Server, ReferenceModel
from spaceone.inventory.model.region import Region
from spaceone.inventory.model.cloud_service_type import CloudServiceType


_LOGGER = logging.getLogger(__name__)


class CollectorManager(BaseManager):

    def __init__(self, transaction):
        super().__init__(transaction)

    def verify(self, secret_data, region_name):
        """ Check connection
        """
        ec2_connector = self.locator.get_connector('EC2Connector')
        r = ec2_connector.verify(secret_data, region_name)
        # ACTIVE/UNKNOWN
        return r

    def list_regions(self, secret_data, region_name):
        ecs_connector: ECSConnector = self.locator.get_connector('ECSConnector')
        ecs_connector.set_client(secret_data, region_name)

        return ecs_connector.list_regions()

    def list_instances(self, params):
        server_vos = []
        ecs_connector: ECSConnector = self.locator.get_connector('ECSConnector')
        ecs_connector.set_client(params['secret_data'], params['region_name'])

        # TODO

        return server_vos

    def list_resources(self, params):
        start_time = time.time()

        try:
            resources = self.list_instances(params)
            print(f'   [{params["region_name"]}] Finished {time.time() - start_time} Seconds')
            return resources

        except Exception as e:
            print(f'[ERROR: {params["region_name"]}] : {e}')
            raise e

    @staticmethod
    def list_cloud_service_types():
        cloud_service_type = {
            'tags': {
                'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/aws-ec2.svg',
            }
        }
        return [CloudServiceType(cloud_service_type, strict=False)]

    @staticmethod
    def get_region_from_result(result):
        REGION_INFO = {
            # TODO: Fill-out region info
            'us-east-1': {'name': 'US East (N. Virginia)', 'tags': {'latitude': '39.028760', 'longitude': '-77.458263'}},
        }

        match_region_info = REGION_INFO.get(getattr(result.data.compute, 'region_name', None))

        if match_region_info is not None:
            region_info = match_region_info.copy()
            region_info.update({
                'region_code': result.data.compute.region_name
            })

            return Region(region_info, strict=False)

        return None
