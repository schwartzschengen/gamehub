import streamlit as st

dct = {
    "品名": "海老と野菜の上天丼",
    "内容": ["海老x2", "なす", "かぼちゃ", "いんげん", "味噌汁"],
    "価格": "760円"
}

with st.echo():
    st.write(dct)
    st.write(f"**dct** → {dct}")
    st.write(f"**dct の「品名」だけを表示** → {dct['品名']}")

    st.write("**キーのリスト:**", list(dct))
    st.write("**値のリスト:**", list(dct.values()))

    dct["カロリー"] = "674 kcal"
    st.write(f"**dct（「カロリー」を追加）** → 項目数 {len(dct)}", dct)
    dct["価格"] = "780円"
    st.write("既存キーの追加", dct)

    dct = dct | {"タンパク質":"15.6 g", "炭水化物":"109.8 g", "価格":"790円"}
    st.write(f"**辞書の加算（マージ）** → 項目数 {len(dct)}", dct)

    del dct["タンパク質"]
    st.write(f"**「タンパク質」を dct から削除** → 項目数 {len(dct)}", dct)
