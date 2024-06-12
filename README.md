# Implementasi One-Time Password dan Digital Signature RSA-PKCS#1 v1.5 pada Physical Gift Card


<p align="center">
Rozan Ghosani 18221121
<br>
Program Studi Sistem dan Teknologi Informasi
<br>
Sekolah Teknik Elektro dan Informatika
<br>
Institut Teknologi Bandung, Jalan Ganesha 10 Bandung
<br>
18221121@std.stei.itb.ac.id
</p>


Sistem produksi dan penggunaan gift card yang memiliki lapisan keamanan dan autentikasi tambahan untuk melindungi konsumen dan perusahaan dari penyalahgunaan gift card.

<p align="center">
  <a href="#about">About</a> |
  <a href="#system-requirements">System Requirements</a> |
  <a href="#how-to-run">How to Run</a> |
  <a href="#features">Features</a>
</p>

# About

Gift card umumnya hanya diamankan dengan menggunakan lapisan penutup goresan pada bagian belakang kartu untuk memastikan bahwa kode pada kartu tersebut belum pernah digunakan sebelumnya . Berdasarkan situasi ini, siapa pun yang memiliki kode pada gift card dapat menukarkan uang tersebut. Seiring dengan lemahnya pengamanan pada gift card, kebutuhan akan mekanisme keamanan yang lebih kuat menjadi sangat penting.

Permasalahan keamanan ini dapat diatasi dengan menerapkan dua mekanisme keamanan, yaitu One-Time Password (OTP) dan digital signature. OTP adalah kode unik yang dihasilkan secara acak dan hanya berlaku untuk satu kali transaksi atau dalam jangka waktu yang sangat singkat [2]. Penerapan OTP pada aktivasi gift card diharapkan dapat mencegah penggunaan yang tidak sah atau pencurian pada gift card. Di sisi lain, Digital signature berfungsi sebagai verifikasi keaslian dan integritas data. Dengan menggunakan digital signature, setiap transaksi atau aktivasi gift card dapat diverifikasi keasliannya, sehingga mencegah manipulasi atau pemalsuan data.

# System Requirements

- Python 3.8 atau lebih baru.
- Library Flet versi terbaru, didapatkan melalui `pip install flet`
- Library cryptography, didapatkan melalui `pip install cryptography`
- Library cv2, didapatkan melalui `pip install opencv-python`
- Library qrcode, didapatkan melalui `pip install qrcode`

# How to Run

### Cloning repository
1. Pada halaman utama repository [GitHub](https://github.com/zshnrg/secured-gift-card), buka menu **Clone** lalu salin URL dari repository
2. Buka Terminal
3. Pindah ke direktori yang diinginkan
4. Ketikan `git clone`, lalu tempelkan URL yang telah disalin tadi 
   ```sh
   git clone https://github.com/zshnrg/secured-gift-card.git
   ```

### Running the app
1. Pindah ke directory `secured-gift-card`
2. Install depedencies yang diperlukan
   ```sh
   pip install -r requirements.txt
   ```
3. Jalankan app dengan cara 
    Aplikasi dijalankan pada peramban (browser) secara langsung
    ```sh
    flet run --web
    ```

# Features

Program ini memiliki fitur:
- Pembuatan kode gift card yang diamankan dengan tanda tangan digital
- Autentikasi gift card dengan menggunakan tanda tangan digital
- Aktivasi gift card dengan menggunakan One-Time Password (OTP)
- Penukaran gift card dengan menggunakan pengamanan OTP
