import streamlit as st

lst = ["焼き鳥丼", "しらす丼", "牛丼", "ロコモコ丼"]

with st.echo():
    st.write(lst)
    st.write(f"**lst** → {lst}")
    st.write(f"**lst の第1要素だけを表示** → {lst[1]}")

    lst.append("チーズカツ丼")
    st.write(f"**lst（チーズカツ丼 を追加）** → 要素数 {len(lst)}", lst)

    lst = lst + ["まぐろネギ丼", "二色そぼろ丼", "サーモンいくら丼"]
    st.write(f"**リストの加算** → 要素数 {len(lst)}", lst)
    lst = lst + ["豚丼"]
    st.write(f"**加算による 豚丼 の追加** → 要素数 {len(lst)}", lst)

    lst.remove("牛丼")
    st.write(f"**牛丼を lst から削除:** → 要素数 {len(lst)}", lst)

    st.write("**文字列を文字に分解する**", list(lst[4]))
