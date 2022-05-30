from enum import Enum


class Code(Enum):
    CODE_ANALOG = 'CODE_ANALOG'
    CODE_DIGITAL = 'CODE_DIGITAL'
    CODE_CUSTOM = 'CODE_CUSTOM'
    CODE_LIMITSET = 'CODE_LIMITSET'
    CODE_SINGLENOE = 'CODE_SINGLENOE'
    CODE_MULTIPLENODE = 'CODE_MULTIPLENODE'
    CODE_CONSUMER = 'CODE_CONSUMER'
    CODE_SOURCE = 'CODE_SOURCE'

    def __str__(self):
        return self.name


Codes = [Code.CODE_ANALOG.name, Code.CODE_DIGITAL.name, Code.CODE_CUSTOM.name, Code.CODE_LIMITSET.name,
         Code.CODE_SINGLENOE.name, Code.CODE_MULTIPLENODE.name, Code.CODE_CONSUMER.name, Code.CODE_SOURCE.name]
