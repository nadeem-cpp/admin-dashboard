from .resource import UserAuthentication, QuestionsApi


def init_routes(api):
    api.add_resource(UserAuthentication, "/user/login")
    api.add_resource(QuestionsApi, "/questions")

