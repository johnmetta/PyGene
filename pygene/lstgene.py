#!/usr/bin/env python
from gene import BaseGene,FloatGene

class ListGene(BaseGene):
   
    size = 3
    value  = None
    item = None
    mutProb = 1.0

    def copy(self):

        cls = self.__class__()
        cls.value = [v.copy() for v in self.value]
        return cls

    def __add__(self,other):
        return map(lambda x,y:x+y,self.value,other.value)

    def mutate(self):
        map(lambda s:s.mutate(),self.value)

    def randomValue(self):
        return [self.item() for i in range(self.size)]

    def flat_values(self):
        return [v.value for v in self.value]

       
class ListFloatGene(ListGene):
    item = FloatGene

