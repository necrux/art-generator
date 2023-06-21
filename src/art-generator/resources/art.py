import configparser
import openai
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from bs4 import BeautifulSoup

blp = Blueprint("Resume", __name__, description="CSS Art Generator")

AUTH_FILE = "/app/.keys"

config = configparser.RawConfigParser()
config.read(AUTH_FILE)

api_key = config["openai"]["key"]
openai.api_key = api_key


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
        prompt = f"Generate a {subject} in a {style} style using purely HTML and CSS. " \
                 f"The code must be fully functional."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
                {"role": "system", "content": "You are and expert on CSS art "
                                              "and your responses only contain valid HTML code."}
            ]
        )
        #soup = BeautifulSoup(response.choices[0].message.content, "html.parser")
        #html = soup.find(name="html")
        #return html
        return response.choices[0].message.content
