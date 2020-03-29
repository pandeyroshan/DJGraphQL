import graphene
import json
from datetime import datetime


class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime(required=False)





class Query(graphene.ObjectType):
    users = graphene.List(User,first=graphene.Int())

    def resolve_users(self,info,first):
        return [
            User(username='roshan',last_login=datetime.now()),
            User(username='priya',last_login=datetime.now()),
            User(username='rohan',last_login=datetime.now()),
        ][:first]

schema = graphene.Schema(query=Query,auto_camelcase=False)

result = schema.execute(
    '''
    {
        users(first:2)
        {
            username
            last_login
        }
    }
    '''
)

items = dict(result.data.items())

print(json.dumps(items,indent=4))