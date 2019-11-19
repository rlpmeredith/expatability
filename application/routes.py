from flask import current_app as app
from flask import render_template
from flask import request


from .models import *

# from .expatability import ChatApi
#
#
# app.register_blueprint(ChatApi, url_prefix='/api/chats')


@app.route('/', methods=['GET'])
def chat():
    user_id = request.args['user_id']
    my_user = User.query.filter(User.user_id == user_id).first()
    username = my_user.first_name
    #return username

