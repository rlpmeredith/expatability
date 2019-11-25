from flask import jsonify, request
from flask import render_template
from flask import current_app as app

from . import db
from .models import *


@app.route('/api/citylist', methods=['GET'])
def get_cityList():

    order = request.args.get('order')

    cityreturnlist = []

    if order == "cost":
        citylist = Cost.query.order_by(Cost.price_index.desc())
        for row in citylist:
            citydict = {row.capital: row.price_index}
            cityreturnlist.append(citydict)
    elif order == "daylength":
        citylist = Sun.query.order_by(Sun.shortest_day.desc())
        for row in citylist:
            citydict = {row.capital: row.shortest_day}
            cityreturnlist.append(citydict)
    elif order == "weather":
        citylist = AvgWeather.query.order_by(AvgWeather.jan_avg.desc())
        for row in citylist:
            citydict = {row.capital: row.jan_avg}
            cityreturnlist.append(citydict)
    elif order == "migrants":
        citylist = Migrant.query.order_by(Migrant.index.desc())
        for row in citylist:
            citydict = {row.country: row.index}
            cityreturnlist.append(citydict)
    elif order == "happiness":
        citylist = Happiness.query.order_by(Happiness.score.desc())
        for row in citylist:
            citydict = {row.country: row.score}
            cityreturnlist.append(citydict)

    return jsonify(cityreturnlist)




# @ChatApi.route('/<chat_id>/messages', methods=['GET'])
# def get_chatmessages(chat_id):
#
#     chat_messages = Message.query.filter(Message.chat_id == chat_id).order_by(Message.message_id).all()
#     if len(chat_messages) == 0:
#         return "No messages found", 404
#     return jsonify([x.to_dict() for x in chat_messages]), 200



#@ToDoApi.route('/<name>')
#def get_task(name):
#    task = ToDoItem.query.filter(ToDoItem.name == name).first()
#    if task is None:
#        return 'task not found', 404
#    return jsonify(task.to_dict()), 200