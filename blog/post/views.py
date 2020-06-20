from flask import Blueprint
from flask_graphql import GraphQLView
from flask_cors import CORS

from blog import admin, db, SecureView
from blog.post.schema import schema
from blog.post.models import Post

post = Blueprint('poste', __name__)

CORS(post)

post.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

admin.add_view(SecureView(Post, db.session))
