from schematics import Model
from schematics.types import ModelType, StringType, BooleanType, ListType


class Tags(Model):
    key = StringType(deserialize_from='Key')
    value = StringType(deserialize_from='Value')


class AlibabaCloud(Model):
    tags = ListType(ModelType(Tags))
