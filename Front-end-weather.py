import random
import joblib
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Predict Your Weather",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/Kuasawan-Murbawan',
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.write("For more information, visit [Husyairi](https://github.com/Kuasawan-Murbawan).")
st.title("Weather Prediction")


choice = st.selectbox("Choose your area",["Seattle"])
st.write("Predicting weather for", choice)


col1, col2= st.columns(2)

precipitation = col1.slider("Precipitation (Water that is falling out of the sky)", 0.0, 55.9, 0.0)
temp_max = col2.slider("Max Temperature", -1.6, 35.6, 0.0)
temp_min = col1.slider("Min Temperature", -7.1, 18.3, 0.0)
wind = col2.slider("Wind Speed", 0.4, 9.5, 0.0)


df_pred = pd.DataFrame([[precipitation,temp_max,temp_min,wind]],
columns= ['precipitation','temp_max','temp_min','wind'])

model = joblib.load("weather_rf_model.pkl")

prediction = model.predict(df_pred)

pred="___"

if st.button('Predict'):
    if(prediction[0]=='rain'):
        pred = "raining"

    elif(prediction[0]=='sun'):
        pred = "sunny"

    elif(prediction[0]=='fog'):
        pred = "foggy"

    elif(prediction[0]=='drizzle'):
        pred = "drizzling"

    elif(prediction[0]=='snow'):
        pred = "snowing"
        
st.divider()

result = "It is expected to be " + pred + " today."
st.title(result)



col1, col2, col3 = st.columns(3)
average_temp = str(round((temp_max+temp_min)/2, 1)) + "°C"
randum = str(round(random.uniform(0,6),1))+ "°C"

winddisplay = str(round(wind,1)) + " m/s"

precipitationDisplay = str(round(precipitation,1)) + "%"

col1.metric("Temperature", average_temp, randum)
col2.metric("Wind", winddisplay, "-8%")
col3.metric("Precipitation", precipitationDisplay, "4%")

#st.write("Streamlit version:", st.__version__#Streamlit version: 1.21.0
#st.write("Pandas version:", pd.__version__)  #Pandas version: 1.5.3
#st.write("Joblib version:", joblib.__version__)# Joblib version: 1.1.1