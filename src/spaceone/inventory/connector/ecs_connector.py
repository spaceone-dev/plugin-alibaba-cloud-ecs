__all__ = ["ECSConnector"]

import logging
from spaceone.core.error import *
from spaceone.core import utils
from spaceone.core.connector import BaseConnector

_LOGGER = logging.getLogger(__name__)


class ECSConnector(BaseConnector):

    def __init__(self, transaction=None, config=None, **kwargs):
        super().__init__(transaction, config, **kwargs)
        self.client = None

    def verify(self, secret_data, region_name):
        self.set_connect(secret_data, region_name)
        return "ACTIVE"

    def set_connect(self, secret_data, region_name, service=""):
        pass

    def set_client(self, secret_data, region_name):
        self.client = None

    def list_regions(self, **query):
        # SAMPLE
        response = self.client.list_regions(**query)
        return response

    def list_instances(self, **query):
        ec2_instances = []
        return ec2_instances
