from flask import Flask, render_template, jsonify, request, send_file
from src.exception import CustomException
from src.logger import logging as lg
import os,sys


from src.pipeline.train_pipeline import TrainingPipeline
from src.pipeline.predict_pipeline import PredictionPipeline


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to my application"




@app.route("/train")
def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()


        return "Training Completed."


    except Exception as e:
        raise CustomException(e,sys)


@app.route('/predict', methods=['POST', 'GET'])
def upload():
    try:
        if request.method == 'POST':

            prediction_pipeline = PredictionPipeline(request)

            #  DataFrame return 
            result_df = prediction_pipeline.run_pipeline()

            # Target column (qualit)
            result_df.reset_index(inplace=True)

            # index ko sensor number bana do
            result_df['Sensor'] = result_df['index'] + 1

            results = result_df[['Sensor', 'quality']].values.tolist()

            lg.info("prediction completed. Showing results on UI.")

            return render_template(
            'upload_file.html',
            results=results,
            download_link="prediction/prediction_file.csv"
            )

        else:
            return render_template('upload_file.html')

    except Exception as e:
        raise CustomException(e, sys)
    
    
@app.route('/download')
def download_file():
    try:
        file_path = os.path.join("prediction", "prediction_file.csv")

        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return "File not found. Please run prediction first."

    except Exception as e:
        raise CustomException(e, sys)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug= True)