from spaceone.core.manager import BaseManager
from spaceone.inventory.model.metadata.metadata import ServerMetadata
from spaceone.inventory.model.metadata.metadata_dynamic_layout import ItemDynamicLayout, TableDynamicLayout, \
    ListDynamicLayout
from spaceone.inventory.model.metadata.metadata_dynamic_field import TextDyField, EnumDyField, ListDyField, \
    DateTimeDyField, SizeField

ecs_instance = ItemDynamicLayout.set_fields('ECS Instance', fields=[
    TextDyField.data_source('Instance ID', 'data.compute.instance_id'),
])

ecs_vpc = ItemDynamicLayout.set_fields('VPC', fields=[
    TextDyField.data_source('VPC ID', 'data.vpc.vpc_id', reference={
        'resource_type': 'inventory.CloudService',
        'reference_key': 'data.vpc_id'
    }),

])

ecs_asg = ItemDynamicLayout.set_fields('Auto Scaling Group', fields=[
    TextDyField.data_source('Auto Scaling Group', 'data.auto_scaling_group.name', reference={
        'resource_type': 'inventory.CloudService',
        'reference_key': 'data.auto_scaling_group_name'
    }),
])

ecs = ListDynamicLayout.set_layouts('AWS EC2', layouts=[ecs_instance, ecs_vpc, ecs_asg])

disk = TableDynamicLayout.set_fields('Disk', root_path='disks', fields=[
    TextDyField.data_source('Index', 'device_index'),
])

nic = TableDynamicLayout.set_fields('NIC', root_path='nics', fields=[
    TextDyField.data_source('Index', 'device_index'),
])

security_group = TableDynamicLayout.set_fields('Security Groups', root_path='data.security_group', fields=[
    EnumDyField.data_source('Direction', 'direction', default_badge={
        'indigo.500': ['inbound'], 'coral.600': ['outbound']
    }),
])

elb = TableDynamicLayout.set_fields('ELB', root_path='data.load_balancer', fields=[
    TextDyField.data_source('Name', 'name', reference={
        'resource_type': 'inventory.CloudService',
        'reference_key': 'data.load_balancer_name'
    }),
])

tags = TableDynamicLayout.set_fields('AWS Tags', root_path='data.aws.tags', fields=[
    TextDyField.data_source('Key', 'key'),
    TextDyField.data_source('Value', 'value'),
])

metadata = ServerMetadata.set_layouts([ecs, tags, disk, nic, security_group, elb])


class MetadataManager(BaseManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.metadata = metadata

    def get_metadata(self):
        return self.metadata
