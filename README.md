<h1 align="center">💳 Credit Card Fraud Detection Web App</h1>

<p align="center">
  <b>Machine Learning + Flask Deployment Project</b><br>
  Detect fraudulent transactions in real-time using ML
</p>

<hr>
<h2>📊 Dataset</h2>
<p>
This project uses the Credit Card Fraud Detection dataset from Kaggle.<br>
<a href="https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud" target="_blank">
Download Dataset from Kaggle
</a>
</p>
<hr>


<h2>📌 Project Overview</h2>
<p>
This project is an end-to-end machine learning application that detects fraudulent credit card transactions.
It uses a trained <b>Logistic Regression model</b> and deploys it using <b>Flask</b> with a user-friendly web interface.
</p>

<hr>

<h2>🎯 Objectives</h2>
<ul>
  <li>Detect fraudulent transactions</li>
  <li>Handle imbalanced dataset</li>
  <li>Deploy ML model using Flask</li>
  <li>Provide real-time predictions</li>
</ul>

<hr>

<h2>📊 Dataset</h2>
<ul>
  <li>Tabular dataset</li>
  <li>PCA transformed features (V1–V28)</li>
  <li><b>Amount</b> – Transaction value</li>
  <li><b>Class</b> – Target (0 = Normal, 1 = Fraud)</li>
</ul>

<hr>

<h2>⚙️ Tech Stack</h2>
<ul>
  <li>Python</li>
  <li>Pandas, NumPy</li>
  <li>Scikit-learn</li>
  <li>Flask</li>
  <li>HTML & CSS</li>
</ul>

<hr>

<h2>🧠 Machine Learning Model</h2>
<ul>
  <li>Logistic Regression</li>
  <li>StandardScaler (Feature Scaling)</li>
</ul>

<hr>

<h2>📈 Evaluation Metrics</h2>
<ul>
  <li>Precision</li>
  <li>Recall</li>
  <li>F1-Score</li>
</ul>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>Real-time prediction</li>
  <li>Simple UI</li>
  <li>Flask backend</li>
</ul>

<hr>

<h2>🏗️ Workflow</h2>
<pre>
Data → Preprocessing → Model Training → Evaluation → Deployment → Prediction
</pre>

<hr>

<h2>📁 Project Structure</h2>
<pre>
project/
│
├── app.py
├── classification.pkl
├── scalar.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
</pre>

<hr>

<h2>▶️ How to Run</h2>
<ol>
  <li>Clone the repository</li>
  <li>Install dependencies</li>
</ol>

<pre>pip install -r requirements.txt</pre>

<ol start="3">
  <li>Run the app</li>
</ol>

<pre>python app.py</pre>

<p>Open browser: <b>http://127.0.0.1:5000/</b></p>

<hr>

<h2>🔮 Future Improvements</h2>
<ul>
  <li>Use advanced models (XGBoost, DL)</li>
  <li>Add probability score</li>
  <li>Deploy on cloud</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>
<p><b>Tamil Arasan</b></p>

<hr>

<p align="center">⭐ If you like this project, give it a star!</p>
