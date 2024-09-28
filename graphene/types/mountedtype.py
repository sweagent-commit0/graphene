from ..utils.orderedtype import OrderedType
from .unmountedtype import UnmountedType

class MountedType(OrderedType):

    @classmethod
    def mounted(cls, unmounted):
        """
        Mount the UnmountedType instance
        """
        pass