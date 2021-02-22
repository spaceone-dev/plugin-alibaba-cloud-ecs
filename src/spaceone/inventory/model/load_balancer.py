from schematics import Model
from schematics.types import StringType, IntType, DictType, ListType, ModelType


class LoadBalancerTags(Model):
    pass


class LoadBalancer(Model):
    type = StringType(choices=('application', 'network'))
    endpoint = StringType()
    port = ListType(IntType())
    name = StringType()
    protocol = ListType(StringType())
    scheme = StringType(choices=('internet-facing', 'internal'))
    tags = ModelType(LoadBalancerTags, default={})
