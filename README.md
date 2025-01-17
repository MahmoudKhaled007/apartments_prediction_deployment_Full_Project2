
# Project Title

A brief description of what this project does and who it's for

# Apartments Prediction Deployment Full Project

This repository contains a comprehensive project focused on scraping real estate data, performing exploratory data analysis (EDA), building machine learning models for apartment price prediction, and deploying a web application for user interaction.

## Project Structure

The repository is organized as follows:

- **Data Collection and Preprocessing**:
  - `OLX_Data_V1_Latest.ipynb`: Notebook for scraping apartment listings from OLX and initial data preprocessing.
  - `lastKnew.csv`: Dataset containing the scraped and preprocessed apartment data.

- **Exploratory Data Analysis (EDA)**:
  - `final_eda.ipynb`: Notebook performing detailed EDA to uncover patterns, trends, and insights from the dataset.

- **Machine Learning Model Development**:
  - `Machine Learning.ipynb`: Notebook for training and evaluating machine learning models to predict apartment prices.
  - `model.h5`: Saved trained machine learning model.
  - `scaler.h5`: Saved scaler used for feature normalization.
  - `state.pkl`: Serialized state information for model deployment.

- **Web Application Deployment**:
  - `Web App Deployment/`: Directory containing files related to the deployment of the web application.
  - `Website/`: Directory containing the web application's frontend and backend code.
  - `Web_App_Deployment.zip`: Compressed file of the web application deployment package.

- **Notebooks**:
  - `LATESTTT.ipynb`: The latest notebook consolidating all steps from data collection to model deployment.




## Getting Started

To get a local copy of the project up and running, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MahmoudKhaled007/apartments_prediction_deployment_Full_Project2.git
   cd apartments_prediction_deployment_Full_Project2

2. **Install the Required Packages**:

```
pip install -r requirements.txt
```
3. **Run the Web Application**:
```
cd Website
python app.py
```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

