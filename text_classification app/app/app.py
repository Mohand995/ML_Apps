import json
from flask import Flask,jsonify,request
from utility import predict_pipe


app=Flask(__name__)

@app.route("/predict",methods=['POST'])
def predict():
    data=request.json
    try:
        sample=data['text']
    except KeyError:
        return  jsonify({'error':'NO text sent'})
    
    sample=[sample]
    preds=predict_pipe(sample)
    try:
        result=jsonify(preds[0])
    except TypeError as e:
        result=jsonify({'error',str(e)})

    return  result

if __name__=='__main__':
    app.run(debug=True)



