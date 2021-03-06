from flask import Flask, request

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'airbnb predictive project'

    @app.route('/predict', methods=['POST'])
    def predict(message=""):
        try:
            # find authorization header
            content = request.get_json(force=True)
            message = f'POST response recieved: {content}'
            # prediction = get_predicted_price(content)
        except Exception as identifier:
            message = f'error: {identifier}'
        return message
    
    return app

#  FLASK_APP=airbnb:APP FLASK_ENV=development flask run 

# def tokenize(text):
#     return [
#         token for token in simple_preprocess(text) if token not in STOPWORDS
#         ]
# @app.route('/', methods=['POST', 'GET'])
# def responses():
#     response = requests.get(
#         'backendurlhere')
#     return str(response.text)
# @app.route('/api', methods=['POST', 'GET'])
# def predict():
#     data = request.get_json(force=True)
#     desc = data['feature'][0]['description']
#     description_length = len(tokenize(desc))
