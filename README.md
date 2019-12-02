# TST - Aplikasi Transportasi
Aplikasi ini adalah sebuah aplikasi untuk mengecek ketersedian transportasi.\
Mata Kuliah II3160 - Teknologi Sistem Terintegrasi\
Deployed application: [https://transportasi.herokuapp.com/](https://transportasi.herokuapp.com/)

1. Firdausi Aditya Darmawan - 18217001
2. Daeng Muhammad Yusuf Aqsha Alfarabi - 18217045

**Used API**:
1. API crawling dari rental mobil Traveloka(https://tst-adit.herokuapp.com/kota/{kota}), repository: https://github.com/fadityad/Tugas-TST
2. API harga dari transportasi online (https://tstfarabi.herokuapp.com/{asal}/{tujuan}), repository: https://github.com/Farabi99/TST/tree/Tugas-2
3. Mapquestapi - API penyedia jarak dari 2 kota (mapquestapi.com)

## Clone setup (on Windows example)

``` bash
# install environments
$ py -3 -m venv venv
$ venv\Scripts\activate
(venv) $ pip install -r requirements.txt
```

## Running locally (on Windows example)

``` bash
# serve at default http://localhost:5000
$ venv\Scripts\activate
(venv) $ py main.py

# to leave venv
(venv) $ deactivate
```
