# Life Expectancy Predictor

Copy

![Web Application Screenshot](webpagess.png)




This project creates an end-to-end machine learning model that predicts life expectancy based on 20 parameters. The project includes data preprocessing, exploratory data analysis, and model training using XGBoost and CatBoost algorithms.

## File Structure

The following files and folders are included in this project:

- `EDA.ipynb`: Jupyter Notebook containing exploratory data analysis
- `Model_Training.ipynb`: Jupyter Notebook containing XGBoost and CatBoost model training
- `catboost_info`: folder containing CatBoost model training information
- `catboost_withoutencoding.ipynb`: Jupyter Notebook containing CatBoost model training without encoding categorical features
- `data_preprocessing.ipynb`: Jupyter Notebook containing data preprocessing
- `df_preprocessed.csv`: preprocessed data file
- `predictor_model.pkl`: trained model file
- `templates`: folder containing HTML, CSS, and JavaScript files for web application
- `webpagess.PNG`: screenshot of the web application
- `app.py`: Python file containing Flask web application code
- `.ipynb_checkpoints`: folder containing Jupyter Notebook checkpoints

## Running the Web Application

To run the web application, run the following command:

```bash
python app.py
This will start the Flask server and you can access the web application at http://localhost:5000/.

## Dependencies

This project requires the following Python libraries:

- pandas
- numpy
- matplotlib
- seaborn
- xgboost
- catboost
- scikit-learn
- flask

You can install these libraries by running the following command:

```bash
pip install pandas numpy matplotlib seaborn xgboost catboost scikit-learn flask
