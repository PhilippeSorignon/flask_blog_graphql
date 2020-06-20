import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from blog.post.models import Post as PostModel


class Post(SQLAlchemyObjectType):
    class Meta:
        model = PostModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    
    all_posts = SQLAlchemyConnectionField(Post.connection)

schema = graphene.Schema(query=Query)
