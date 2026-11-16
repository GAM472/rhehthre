<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>แบบฝึกสร้างแอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'IBM Plex Sans Thai', sans-serif;
      background-color: #00a896;
      margin: 0;
      padding: 0;
    }
    .header {
      background-color: #ffb870;
      padding: 25px 20px;
      text-align: center;
      font-size: 36px;
      font-weight: 700;
      color: #000000;
    }
    .container {
      max-width: 1150px;
      margin: 20px auto;
      padding: 0 15px;
    }
    .instruction-box {
      background-color: #ffffff;
      padding: 12px 20px;
      margin-bottom: 20px;
      font-size: 20px;
      font-weight: 700;
      color: #c1121f;
    }
    .instruction-box u {
      text-decoration: underline;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      background-color: #ffffff;
    }
    th, td {
      border: 1px solid #808080;
      padding: 12px 15px;
      vertical-align: middle;
    }
    th {
      background-color: #a8f9ff;
      font-size: 20px;
      font-weight: 700;
      color: #000000;
      text-align: center;
    }
    .col-code {
      width: 48%;
      font-size: 16px;
      font-weight: 600;
      color: #000000;
    }
    .col-algo {
      width: 22%;
      background-color: #fefae0;
      color: #0000ff;
      font-size: 16px;
      font-weight: 700;
      text-align: center;
    }
    .col-result {
      width: 30%;
      font-size: 16px;
      font-weight: 600;
      color: #000000;
    }
    .gray-cell {
      background-color: #9e9e9e;
      height: 24px;
    }
    .red-text {
      color: #d90429;
    }
  </style>
</head>
<body>

  <div class="header">
    แบบฝึกสร้างแอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%
  </div>

  <div class="container">
    <div class="instruction-box">
      <u>ขั้นตอนที่ 4 :</u> นำตัวเลือกโค้ดด้านซ้ายมือ ไปวางเรียงลำดับตามอัลกอรีทึม ลงในช่องโค้ดที่เรียงสำเร็จ
    </div>

    <table>
      <thead>
        <tr>
          <th>ตัวเลือกโค้ด</th>
          <th>อัลกอรีทึม</th>
          <th>โค้ดที่เรียงสำเร็จ</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="col-code">st.title("🛒 แอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%")</td>
          <td class="col-algo">ระบุคำสั่ง import</td>
          <td class="col-result"></td>
        </tr>
        <tr>
          <td class="col-code">vat = price * 0.07</td>
          <td class="col-algo">แสดงชื่อแอปพลิเคชัน</td>
          <td class="col-result"></td>
        </tr>
        <tr>
          <td class="col-code">st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")</td>
          <td class="col-algo">สร้างช่องรับข้อมูล<br>ตัวเลขราคา</td>
          <td class="col-result"></td>
        </tr>
        <tr>
          <td class="col-code gray-cell"></td>
          <td class="col-algo">ตัวแปร vat คำนวณ 7%</td>
          <td class="col-result"></td>
        </tr>
        <tr>
          <td class="col-code">import streamlit as st</td>
          <td class="col-algo">ตัวแปร net_price<br>คำนวณราคา - vat</td>
          <td class="col-result"></td>
        </tr>
        <tr>
          <td class="col-code">price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)</td>
          <td class="col-algo">แสดงจำนวน Vat</td>
          <td class="col-result"></td>
        </tr>
        <tr>
          <td class="col-code">net_price = price - vat</td>
          <td class="col-algo">แสดงราคาสุทธิ</td>
          <td class="col-result"></td>
        </tr>
        <tr>
          <td class="col-code">st.write("<span class="red-text">นางสาวดีใจ ยิ้มแย้ม เลขที่ 5 ม.4/5</span>")</td>
          <td class="col-algo">สร้างเส้นกั้น</td>
          <td class="col-result">st.divider()</td>
        </tr>
        <tr>
          <td class="col-code">st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")</td>
          <td class="col-algo">แสดงข้อมูลนักเรียน</td>
          <td class="col-result"></td>
        </tr>
      </tbody>
    </table>
  </div>

</body>
</html>
