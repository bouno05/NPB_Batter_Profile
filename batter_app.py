import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import pandas as pd
import numpy as np

#デザインCSS
button_css = f"""
<style>
  div.stButton > button:first-child  {{
    font-weight  : 900                ;/* 文字：太字*/
  }}
</style>
"""
st.markdown(button_css, unsafe_allow_html=True)
#辞書

#タイトル
st.title("NPB Bat Profiler - β ver.")
st.write("Developed by bouno05")

# 年度を選択
selected_year = st.selectbox("Select Year", list(data.keys()))

# 選択した年度のリーグを取得
if selected_year:
    leagues = data[selected_year]
    selected_league = st.selectbox("Select League", list(leagues.keys()))

    # 選択したリーグの球団を取得
    if selected_league:
        teams = leagues[selected_league]
        selected_team = st.selectbox("Select Team", ["ALL Teams"]+list(teams.keys()),index=0)

        # 選択した球団の選手名を取得
        if selected_team:
            if selected_team=="ALL Teams":
                for i in range(len(list(teams.keys()))):
                    name=list(teams.keys())[i]
                    if i==0:
                        team_players = teams[name]
                    else:
                        team_players.update(teams[name])
            else:
                team_players = teams[selected_team]
            selected_player = st.selectbox("Select or Input a Player", list(team_players.keys()),index = None,
    placeholder="Input a player...")

#ボタン
button=st.button(" Generate ! ", icon=":material/stylus_note:",type="primary")
#タブ
tab1, tab2 = st.tabs(["Basic Stats", "Pitch Type"])
#実行
if button:
    try:
        urls = team_players[selected_player]
        response = requests.get(urls[0])
        image1 = Image.open(BytesIO(response.content))
        with tab1:
            st.image(image1, use_column_width=True)
        response = requests.get(urls[1])
        image2 = Image.open(BytesIO(response.content))
        with tab2:
            st.image(image2, use_column_width=True)
    except:
        pass

#注意事項
with st.container(height=250):
     st.markdown(":gray[・「Generate」ボタンをクリックすると打者プロフィールが生成されます。]")
     st.markdown(":gray[・ローマ字は表記ゆれがある場合がございます。ご了承ください。]")
     st.markdown(":gray[・本データは@bouno05によって独自に収集・計算されたものです。]")
     st.markdown(":gray[・同一選手が複数球団でプレーした場合、成績は所属球団ごとに集計されます。]")
     st.markdown(":gray[・指標に関しての詳細はこちらをご参照ください。]")
     st.page_link("https://bo-no05.hatenadiary.org/entry/2010/01/01/000000_1",label="https://bo-no05.hatenadiary.org/entry/2010/01/01/000000_1")
