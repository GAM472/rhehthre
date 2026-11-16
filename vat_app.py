import streamlit as st

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600;700&display=swap');

html, body, [class*="css"], h1, h2, h3, p, div, span, input {
    font-family: 'IBM Plex Sans Thai', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🛒 แอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%")

price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0, value=0.0)

vat = price * 0.07
net_price = price - vat

st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")

st.divider()

st.write("นางสาวธัญพิมล แสนใจพรม เลขที่ 14 ม.4/5")
