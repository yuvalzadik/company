from flask import  Flask, jsonify, request, json
import requests, os
api_v1 = Flask (__name__)

workers_api = os.environ.get("WORKERS_API")

orders = [
    {
        "id":1,
        "company": "pizza prego",
         "date": "01/01/2020 16:00",
        "task": "python",
        "workers-ids": [12,11]
    },

    {
        "id": 2,
        "company": "macdonals",
        "date": "01/02/2020 16:00",
        "task": "disk",
        "workers-ids": [13]
    },

    {
        "id": 3,
        "company": "dominos",
        "date": "01/01/2022 10:00",
        "task": "py",
        "workers-ids": [12, 11,13]
    }
]

@api_v1.route('/orders', methods = ['GET'])
def get_orders ():
    return jsonify(orders)


@api_v1.route('/orders', methods = ['POST'])
def add_order ():
    order = request.json # מכניס לאובייקט order את ההזמנה החדשה
    orders.append(order) # מוסיף לרשימה של ההזמנות את ההזמנה החדשה
    ids = order["workers-ids"] # מכניס לתוך האובייקט ids את הwokers_ids מההזמנה החדשה.
    for worker_id in ids: # רץ על הwoker_ids מההזמנה החדשה ומעדכן את ההזמנה החדשה תחת אות הworker
        body = {    # מכניס לתוך משנה order את הid של ההזמנה החדשה מתוך מה שסיפקנו
            "order": request.json["id"]
        }
        # שולח בקה מסוג put לurl לפי אותו הworker id על מנת לעדכן את ההזנה תחתיו
        req = requests.put(url=f"http://{workers_api}/workers/{worker_id}",
                           data=json.dumps(body),
                           headers={'Content-type': 'application/json'})
        if req.status_code == 404:
            return jsonify({"error": f"worker not fount {worker_id}"})
    response = {
        "msg": "success",
        "orders":orders
    }
    return jsonify(response)

@api_v1.route('/orders/<int:id>', methods = ['DELETE'])
def del_orders (id):
    deleteed_order = {}
    for order in orders:
        if order["id"] == id:
            deleteed_order = order
            orders.remove(order)
    if deleteed_order == {}:
        return jsonify({"error" : "not found id" }), 404
    response = {
        "deleted":id,
        "orders": orders
    }
    return jsonify(response)

@api_v1.route('/orders/<int:id>', methods = ['GET'])
def get_order (id):
    get_order = {}
    for order in orders:
        if order["id"] == id:
            get_order = order
    if get_order == {}:
        return jsonify({"error" : "not found id" }), 404
    response = {

        "order": get_order
    }
    return jsonify(response)


if __name__ == "__main__":
    api_v1.run(debug=True, port=4000, host="0.0.0.0")