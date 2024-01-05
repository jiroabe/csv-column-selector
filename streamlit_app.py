import streamlit as st
import pandas as pd

# ストリームリットページのタイトル
st.title('CSV Column Selector')

# CSVファイルのアップロード
uploaded_file = st.file_uploader("Choose a CSV file", type='csv')

# 列の選択を行う
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # テキスト入力で列名を入力する
    columns_input = st.text_input('Enter column names separated by commas (e.g., サービス日付,曜日)')

    if st.button('Execute'):
        # 入力された列名をカンマで分割してリストにする
        selected_columns = [column.strip() for column in columns_input.split(',') if column.strip() in df.columns]

        # 選択された列のみを含む新しいDataFrameを作成
        if selected_columns:
            new_df = df[selected_columns]
            # データフレームを表示
            st.write(new_df)

            # CSVとしてダウンロード可能にする
            csv = new_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name='selected_columns.csv',
                mime='text/csv',
            )
        else:
            st.error("Please enter valid column names.")
