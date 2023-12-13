from database.models import User, Questions
from flask import request, jsonify, session
from flask_restful import Resource


class UserAuthentication(Resource):
    def post(self):
        try:
            data = request.get_json()
            print(data)
            user = User.objects(**data)
            if len(user) > 0:
                session["admin"] = True
                return jsonify({
                    "code": 200,
                })
            else:
                return jsonify({
                    "code": 300,
                })
        except Exception as e:
            return jsonify({
                "error": str(e),
                "code": 500,
            })


class QuestionsApi(Resource):
    def get(self):
        questions = Questions.objects()
        return jsonify(questions)

    def post(self):
        try:

            data = request.get_json()
            question = Questions(**data).save()
            return jsonify({
                "code": 200
            })
        except Exception as e:
            print(e)
            return jsonify({
                "code": 300,
            })

    def put(self):
        try:
            data = request.get_json()
            id = data["id"]
            print(id)
            print(data)
            question = Questions.objects(id=id).update(**data)
            return jsonify({
                "code": 200
            })
        except Exception as e:
            return jsonify({
                "code": 300,
            })

    def delete(self):
        try:
            data = request.get_json()
            id = data["id"]
            Questions.objects(id=id).delete()
            return jsonify({
                "code": 200
            })
        except Exception as e:
            print(e)
            return jsonify({
                "code": 300,
            })
