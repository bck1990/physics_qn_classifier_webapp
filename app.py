import flask
import pickle
#import urllib


# Use pickle to load in the pre-trained model.
with open(f'model/tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)
    
with open(f'model/classifier.pkl', 'rb') as f:
    classifier = pickle.load(f)

def predict_topic(text):
    result = classifier.predict(tfidf_vectorizer.transform([text]))
    return(result[0])
    
#print(predict_topic('a ball travels with velocity')) #for debugging

app = flask.Flask(__name__, template_folder='templates')
    
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        question_text = ' '
        question_text = flask.request.form['question_text']
        prediction = predict_topic(question_text)
        return flask.render_template('main.html',
                                     original_input={'Question Text':question_text},
                                     result=prediction,
                                     )
        
if __name__ == '__main__':
    
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
