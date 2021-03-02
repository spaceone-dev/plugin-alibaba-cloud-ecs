from schematics import Model
from schematics.types import StringType, ModelType


class AutoScalingGroup(Model):
    name = StringType()
