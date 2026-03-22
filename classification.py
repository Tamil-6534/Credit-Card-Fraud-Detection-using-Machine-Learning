import pandas as pd

# Dataset: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
df = pd.read_csv(Dataset)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['Amount'] = scaler.fit_transform(df[['Amount']])

x = df[['Amount','V6','V1','V5','V7','V20','V12','V22','V4','V11','V21']]
y = df['Class']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

from sklearn.linear_model import LogisticRegression
classification = LogisticRegression()
classification.fit(x_train, y_train)

y_pred = classification.predict(x_test)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

inputs = [-0.353229, -1.426545, -2.312227, -0.522188, -2.537387,
          0.126911, -2.899907, -0.035049, 3.997906, 3.202033, 0.517232]

new_data = pd.DataFrame([inputs], columns=x.columns)

prediction = classification.predict(new_data)
print(prediction)

import pickle

pickle.dump(scaler,open('scalar.pkl','wb'))
pickle.dump(classification,open('classification.pkl','wb'))
