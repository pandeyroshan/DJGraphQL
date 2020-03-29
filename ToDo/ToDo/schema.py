import graphene
from myapp.schema import Query as todo_query


class Query(todo_query):
    pass

schema = graphene.Schema(query=Query,auto_camelcase=False)