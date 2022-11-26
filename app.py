import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import pydeck as pdk

image = Image.open('images.jfif')
st.image(image, width=400)

st.title('My First App')
st.caption('これは地域実践演習用のアプリです')
st.subheader('入力情報')
st.write('以下の項目を入力してください')

with st.form(key='info_form'):

 name = st.text_input('名前')
 address = st.text_input('住所')
 st.selectbox("好きな動物",("犬", "鳥", "牛"))
 st.checkbox("チェックボックス")

 submit_btn = st.form_submit_button('送信')
 cancel_btn = st.form_submit_button('キャンセル')
 if submit_btn:
    st.text(f'ようこそ！{address}にお住まいの{name}さん！！')
    
df = pd.read_csv('data.csv', index_col='月')
st.dataframe(df)
st.table(df)
st.line_chart(df)
st.bar_chart(df['2020年'])

chart_data = pd.DataFrame(
    np.random.randn(30, 2) / [3000, 3000] + [34.7989379019412, 135.24694876864245],
    columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=34.7989379019412, 
        longitude=135.24694876864245,
        zoom=16,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=chart_data,
            get_position='[lon, lat]',
            radius=5,
            elevation_scale=4,
            elevation_range=[0, 10],
            pickable=True,
            extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=6,
        ),
    ],
))