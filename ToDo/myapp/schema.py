import graphene
from graphene_django.types import DjangoObjectType
from .models import ToDoList



class ToDoListType(DjangoObjectType):
    class Meta:
        model = ToDoList


class Query(graphene.ObjectType):
    all_todo = graphene.List(ToDoListType)

    def resolve_all_todo(self,info,**kwargs):
        return ToDoList.objects.all()