import configparser
import openai
import requests
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("Resume", __name__, description="CSS Art Generator")

AUTH_FILE = "/app/.keys"

config = configparser.RawConfigParser()
config.read(AUTH_FILE)

api_key = config["openai"]["key"]


@blp.route("/")
class Welcome(MethodView):
    def get(self):
        return {"message": "Welcome. Be sure to review the Swagger docs: /swagger-ui"}


#@blp.route("/resume")
#class Resume(MethodView):
#    def get(self):
#        return resume
#
#    def delete(self):
#        global resume
#        resume = {}
#        return resume
#
#
#@blp.route("/resume/refresh")
#class Refresh(MethodView):
#    def get(self):
#        global resume
#        try:
#            response = requests.get(url=RESUME_ENDPOINT)
#            response.raise_for_status()
#        except requests.exceptions.HTTPError:
#            abort(500, message="Failed to update resume content. Please try again.")
#        else:
#            resume = yaml.safe_load(response.text)
#            return "Grabbed the latest resume."


@blp.route("/art/v1/<string:subject>/<string:style>")
class Section(MethodView):
    def get(self, subject, style):
        prompt = f"Generate a {subject} in a {style} style using purely HTML and CSS."
        return api_key
