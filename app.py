# cd Documents/streamlit/praise
# streamlit run app.py

import numpy as np
import pandas as pd
import re
import streamlit as st

p_df = pd.read_csv('title_lyrics.csv', encoding='utf-8').dropna()


def search_praise(word):
    dic = {}

    for index, row in p_df.iterrows():
        
        text_ls = re.split("(?<=。)", row['body'].replace("\n", "").replace("\t", "").replace("\r", "").replace("\u3000", ""))

        for i in range(0, len(text_ls)):
            if text_ls[i].find(word) >= 0:
                dic[index] = {
                    'title' : row['title']
                    , 'body' : row['body']
                    }

    return pd.DataFrame(data=dic).T.sort_values('body')


try:
        
    st.title('検索')
    search_word = st.text_input('**検索ワード**', '')
    if search_word != '':
        s_df = search_praise(search_word)
        for index, row in s_df.iterrows():
            st.write('タイトル: ', row['title'])
            st.write('歌詞:')
            st.write(row['body'])
            st.write('------------------------------------------------------------')

except KeyError:
    st.error('検索が引っかからなかったようです。', icon="🤷‍♀️")

