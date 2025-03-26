# Laporan Proyek Mechine Learning - Shinta Arum Imaniyah

## Domain Proyek 

Pada proyek ini saya melihat tutorial yt tentang sentimen yang membuat sebuah sentimen toko bangunan
Ulasan pelanggan memiliki peran yang sangat penting dalam menentukan reputasi dan keberlanjutan suatu bisnis, termasuk toko ritel maupun e-commerce. Konsumen semakin mengandalkan ulasan dari pelanggan lain sebelum membuat keputusan pembelian. . Oleh karena itu, pemahaman terhadap sentimen yang terkandung dalam ulasan pelanggan menjadi sangat krusial bagi pemilik bisnis untuk meningkatkan kualitas layanan dan produk yang ditawarkan.
Proyek ini bertujuan untuk membangun sistem analisis sentimen ulasan toko guna mengklasifikasikan ulasan pelanggan ke dalam kategori positif dan negatif. Dengan adanya sistem ini, pemilik toko dapat lebih mudah memantau kepuasan pelanggan dan mengambil keputusan yang berbasis data untuk meningkatkan pengalaman berbelanja. Selain itu, hasil analisis dapat digunakan sebagai alat evaluasi untuk mengidentifikasi kelebihan dan kekurangan layanan yang diberikan.

## Business Understanding
 
### Problem Statements
 - Sulitnya mengidentifikasi dan mengelompokkan ulasan pelanggan berdasarkan sentimen yang terkandung di dalamnya secara otomatis.
 -  Pemilik toko kesulitan dalam memahami aspek layanan atau produk manakah ulasan yang lebih banyakn apakah ulasan negatif atau posfitif 

### Goals
 - Mengembangkan sistem berbasis NLP yang dapat secara otomatis mengklasifikasikan ulasan pelanggan ke dalam kategori positif dan negatif.
 - membandingkan apakah lebih banyak mendapatkan ulasan positif dan negatif

## Data Understanding
Data yang saya gunakan adalah data ulasan sebuah toko di marketplace
https://drive.google.com/file/d/1XP2qUV9ftVpYqJFcrNp7HCFc2M52PKly/view?usp=sharing
###variabel 
- ulasan
- rating
- kategori
- nama produk

## Data Preparation
- Crawling Data = Proses mengumpulkan data dari internet secara otomatis menggunakan bot atau web scraper.
- Labeling = Proses memberikan label atau kategori pada data.
- Normalisasi = Proses standarisasi data agar lebih seragam.
- Stopwords = Kata-kata umum yang sering muncul tetapi tidak terlalu berpengaruh dalam analisis, seperti "yang", "di", "dan" dalam bahasa Indonesia.
- Tokenize (Tokenisasi) = Proses memecah teks menjadi kata atau frasa yang lebih kecil (token).
- Stemming = Proses mengubah kata menjadi bentuk dasar.
- dua atribut atau fitur digabungkan untuk memperkaya informasi.

## Modeling
  - Menghitung Kata dengan TF-IDF
  - Visualisasi (NLP)
    ![image](https://github.com/user-attachments/assets/d7f4c4a6-f727-487e-a945-959fb72521eb)
    ![image](https://github.com/user-attachments/assets/68becb9b-7b9b-4a31-8d46-8890661281bc)
    ![image](https://github.com/user-attachments/assets/f929ea7d-1645-4331-abe2-a4fc17493532)

## Evaluasi 
Confusion Matrix
![image](https://github.com/user-attachments/assets/7c400c8b-beae-42af-9a8f-eaf1dc078982)
![image](https://github.com/user-attachments/assets/84056304-f5a5-456e-94c6-28df8f70c7d4)
akurasi = 0.49

---Ini adalah bagian akhir laporan--
