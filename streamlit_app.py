import streamlit as st
import pandas as pd

# ストリームリットページのタイトル
st.title('CSV Column Selector and Exporter')

# CSVファイルのアップロード
uploaded_file = st.file_uploader("Choose a CSV file", type='csv')

# 列の選択を行う
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    all_columns = df.columns.tolist()
    selected_columns = st.multiselect('Select columns', all_columns, default=all_columns[:min(10, len(all_columns))])

    # 出力形式の選択
    file_format = st.selectbox('Select output file format', ['CSV', 'JSON'])

    if st.button('Execute'):
        # 選択された列のみを含む新しいDataFrameを作成
        new_df = df[selected_columns]

        if file_format == 'CSV':
            # CSVプレビューを表示
            st.write(new_df)

            # CSVとしてダウンロード可能にする
            csv = new_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name='selected_columns.csv',
                mime='text/csv',
            )
        elif file_format == 'JSON':
            # JSON形式に変換
            json_data = new_df.to_json(orient='records', lines=False, indent=2)

            # JSONプレビューを表示
            st.text_area('JSON Preview', json_data, height=300)

            # JSONとしてダウンロード可能にする
            st.download_button(
                label="Download JSON",
                data=json_data,
                file_name='selected_columns.json',
                mime='application/json',
            )
