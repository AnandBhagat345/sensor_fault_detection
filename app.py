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

            # DataFrame return
            result_df = prediction_pipeline.run_pipeline()

            # Index reset for sensor numbering
            result_df = result_df.copy()
            result_df.reset_index(drop=True, inplace=True)

            # Sensor 1, Sensor 2, Sensor 3 ...
            result_df['Sensor'] = [f"Sensor {i + 1}" for i in range(len(result_df))]

            # Table data
            results = result_df[['Sensor', 'quality']].values.tolist()

            # Dashboard counts
            good_count = int((result_df['quality'] == 'good').sum())
            bad_count = int((result_df['quality'] == 'bad').sum())
            total_count = int(len(result_df))

            lg.info("prediction completed. Showing results with dashboard on UI.")

            return render_template(
                'upload_file.html',
                results=results,
                good_count=good_count,
                bad_count=bad_count,
                total_count=total_count
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