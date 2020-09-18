from flask import  Flask, jsonify, request, json
import requests

api_v1 = Flask (__name__)

workers = [
    {
        "name": "yuval zadik ",
        "team" : "vmware & netapp",
        "id" : 10,
        "orders": [1]
    },

    {
        "name": "pavel sorkin ",
        "team": "vmware & netapp",
        "id": 11,
        "orders":[2,3]

    },

    {
        "name": "ben boaron ",
        "team": "microsoft",
        "id": 12,
        "orders": []
    },

    {
        "name": "raz tal ",
        "team": "vmware & netapp",
        "id": 13,
        "orders": []

    }


]

@api_v1.route('/workers', methods = ['GET']) # get all workers list
def get_workers():
    return jsonify(workers)

@api_v1.route('/workers', methods = ['POST']) # add new worker
def add_workers():
    a = request.json
    workers.insert(len(workers),a)
    print(jsonify(workers))
    return jsonify(workers)

@api_v1.route('/workers/<int:id>', methods = ['GET']) # get details on worker with a given id parameter
def id_finder (id):
    for work in workers:
        if work["id"] == id:
            return jsonify(work)

# מקבל id של עובד שנכנסה בשבילו הזמנה חדשה ומעדכן תחת אותו עובד את מספר ההזמנה החדשה
@api_v1.route('/workers/<int:id>', methods= ['PUT'])
def id_change(id):
    new_worker = {} # משתנה לצורך בדיקה שקיים עובד עם הid שנשלח אליו
    for i, work in enumerate(workers): # רץ על כל העובדים ובודק האם נמצא עובד עם id כזה
        if work["id"] == id:
            work["orders"].append(request.json["order"]) # מוסיף לעובד את הערך של האובייקט order שהוא בעצם הערך id של ההזמנה החדשה
            new_worker = work
            workers[i] = work # מעדכן את workers
    if new_worker == {}:
         return jsonify({"error": "not found id"}), 404
    return jsonify(workers)

@api_v1.route('/workers/<int:id>', methods= ['DELETE']) #delete a worker with a given id parameter
def id_delete(id):
    for work in workers:
        if work["id"] == id:
            workers.remove(work)
    return jsonify(workers)

if __name__ == "__main__":
    api_v1.run(debug=True, port=80, host="0.0.0.0")

# to comment press ctrl+?
