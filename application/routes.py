from flask import jsonify, request
from flask import render_template
from flask import current_app as app

from . import db
from .models import *



# @app.route('/', methods=['GET'])
# def chat():
#     user_id = request.args['user_id']
#     my_user = User.query.filter(User.user_id == user_id).first()
#     username = my_user.first_name
    #return username


@ExpatabilityApi.route('/', methods=['GET'])
def get_happinessList():

    happinessList =  Happiness.query.filter(Happiness.capital == capital).order_by(City.capital).all()
    if len(happinessList) == 0:
        return "No messages found", 404
    return jsonify([x.to_dict() for x in happinessList]), 200




@ChatApi.route('/<chat_id>/messages', methods=['GET'])
def get_chatmessages(chat_id):

    chat_messages = Message.query.filter(Message.chat_id == chat_id).order_by(Message.message_id).all()
    if len(chat_messages) == 0:
        return "No messages found", 404
    return jsonify([x.to_dict() for x in chat_messages]), 200



#@ToDoApi.route('/<name>')
#def get_task(name):
#    task = ToDoItem.query.filter(ToDoItem.name == name).first()
#    if task is None:
#        return 'task not found', 404
#    return jsonify(task.to_dict()), 200