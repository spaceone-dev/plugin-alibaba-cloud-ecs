from schematics import Model
from schematics.types import StringType, IntType, BooleanType, ModelType, FloatType


class DiskTags(Model):
    pass


class Disk(Model):
    device_index = IntType()
    device = StringType()
    disk_type = StringType(default="EBS")
    size = FloatType()
    tags = ModelType(DiskTags, default={})
