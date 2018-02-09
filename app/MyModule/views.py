from . import my_bp

from models import *
from flask import jsonify, request

@my_bp.route('/', methods=['GET'])
def test():
    return jsonify({"msg" : "welcome to my module"})

@my_bp.route('/myroute', methods=['POST'])
def myroute():
   pass




@my_bp.route('/addPerson', methods=['POST'])
def addPerson():

    requestObject =  request.get_json()

    #print requestObject['name']

    try:

        mytableobject = MyTable()

        mytableobject.import_data(requestObject)

        db.session.add(mytableobject)

        db.session.commit()

        return jsonify({"message": "success"})

    except Exception as e:

        print str(e)

        db.session.rollback()

        return jsonify({"message": "error"})


@my_bp.route('/searchPerson', methods=['POST'])
def searchPerson():

    requestObject = request.get_json()

    try:

        tuples = MyTable.query.filter(MyTable.name==requestObject['name'])

        #num of results
        print tuples.count()


        TEMP_API_PARAMETERS = {


            "SEARCH_RESPONSE" : {

                "id": "",
                "name": ""

            }

        }

        results_list = []

        response_settings = TEMP_API_PARAMETERS['SEARCH_RESPONSE']

        for person in tuples :

            temp = {}

            for key in response_settings:
                temp[key] = getattr(person,key)

            results_list.append(temp)


        return jsonify({"message": "success",
                        "results" : results_list })

    except Exception as e:

        print str(e)

        return jsonify({"message": "error"})