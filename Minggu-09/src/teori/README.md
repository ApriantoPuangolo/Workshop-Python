# 12. Virtual Environments and Packages (Lingkungan dan Paket Virtual)

***12.1. Perkenalan***

Aplikasi Python sering kali menggunakan paket dan modul yang tidak disertakan sebagai bagian dari perpustakaan standar. Aplikasi kadang-kadang membutuhkan versi perpustakaan tertentu, karena aplikasi mungkin memerlukan bug tertentu yang telah diperbaiki atau aplikasi mungkin ditulis menggunakan versi usang dari antarmuka perpustakaan.

Artinya, satu instalasi Python mungkin tidak dapat memenuhi persyaratan setiap aplikasi. Jika aplikasi A membutuhkan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka persyaratan tersebut bertentangan dan menginstal versi 1.0 atau 2.0 akan membuat satu aplikasi tidak dapat berjalan.

Solusi untuk masalah ini adalah membuat lingkungan virtual, pohon direktori mandiri yang berisi instalasi Python untuk versi Python tertentu, ditambah sejumlah paket tambahan.

Aplikasi yang berbeda kemudian dapat menggunakan lingkungan virtual yang berbeda. Untuk mengatasi contoh konflik persyaratan sebelumnya, aplikasi A dapat memiliki lingkungan virtualnya sendiri dengan versi 1.0 diinstal sementara aplikasi B memiliki lingkungan virtual lain dengan versi 2.0. Jika aplikasi B memerlukan perpustakaan ditingkatkan ke versi 3.0, hal ini tidak akan mempengaruhi lingkungan aplikasi A.

***12.2. Membuat Lingkungan Virtual***

Modul yang digunakan untuk membuat dan mengelola lingkungan virtual disebut venv. venv biasanya akan menginstal versi terbaru Python yang Anda miliki. Jika Anda memiliki beberapa versi Python di sistem Anda, Anda dapat memilih versi Python tertentu dengan menjalankan python3 atau versi apa pun yang Anda inginkan.

Untuk membuat lingkungan virtual, tentukan direktori tempat Anda ingin meletakkannya, dan jalankan modul venv sebagai skrip dengan jalur direktori:

    python -m venv tutorial-env

Ini akan membuat direktori tutorial-env jika tidak ada, dan juga membuat direktori di dalamnya yang berisi salinan interpreter Python dan berbagai file pendukung.

Lokasi direktori umum untuk lingkungan virtual adalah .venv. Nama ini membuat direktori biasanya tersembunyi di shell Anda dan dengan demikian tidak menghalangi sambil memberinya nama yang menjelaskan mengapa direktori tersebut ada. Itu juga mencegah bentrok dengan file definisi variabel lingkungan .env yang didukung beberapa perkakas.

Setelah Anda membuat lingkungan virtual, Anda dapat mengaktifkannya.

Di Windows, jalankan:

    tutorial-env\Scripts\activate.bat


Di Unix atau MacOS, jalankan:

    source tutorial-env/bin/activate

(Skrip ini ditulis untuk bash shell. Jika Anda menggunakan csh atau fish shell, ada skrip alternatif activation.csh dan activation.fish yang sebaiknya Anda gunakan.)

Mengaktifkan lingkungan virtual akan mengubah perintah shell Anda untuk menunjukkan lingkungan virtual apa yang Anda gunakan, dan memodifikasi lingkungan sehingga menjalankan python akan memberi Anda versi dan instalasi Python tertentu. Misalnya:

    $ source ~/envs/tutorial-env/bin/activate
    (tutorial-env) $ python
    Python 3.5.1 (default, May  6 2016, 10:59:36)
      ...
    >>> import sys
    >>> sys.path
    ['', '/usr/local/lib/python35.zip', ...,
    '~/envs/tutorial-env/lib/python3.5/site-packages']
    >>>

Untuk menonaktifkan lingkungan virtual, ketik:

    deactivate

ke dalam terminal.

***12.3. Mengelola Paket dengan pip***

Anda dapat menginstal, mengupgrade, dan menghapus paket menggunakan program bernama pip. Secara default pip akan menginstal paket dari Indeks Paket Python. Anda dapat menelusuri Indeks Paket Python dengan membukanya di browser web Anda.

pip memiliki sejumlah subperintah: “install”, “uninstall”, “freeze”, dll. (Lihat panduan Menginstal Modul Python untuk dokumentasi lengkap untuk pip.)

Anda dapat menginstal versi terbaru suatu paket dengan menentukan nama paket:

    (tutorial-env) $ python -m pip install novas
    Collecting novas
      Downloading novas-3.1.1.3.tar.gz (136kB)
    Installing collected packages: novas
      Running setup.py install for novas
    Successfully installed novas-3.1.1.3


Anda juga dapat menginstal versi paket tertentu dengan memberikan nama paket diikuti dengan == dan nomor versi:

    (tutorial-env) $ python -m pip install requests==2.6.0
    Collecting requests==2.6.0
      Using cached requests-2.6.0-py2.py3-none-any.whl
    Installing collected packages: requests
    Successfully installed requests-2.6.0

Jika Anda menjalankan kembali perintah ini, pip akan melihat bahwa versi yang diminta telah diinstal dan tidak melakukan apa pun. Anda dapat memberikan nomor versi yang berbeda untuk mendapatkan versi tersebut, atau Anda dapat menjalankan python -m pip install --upgrade untuk memutakhirkan paket ke versi terbaru:

    (tutorial-env) $ python -m pip install --upgrade requests
    Collecting requests
    Installing collected packages: requests
      Found existing installation: requests 2.6.0
        Uninstalling requests-2.6.0:
          Successfully uninstalled requests-2.6.0
    Successfully installed requests-2.7.0

python -m pip uninstall diikuti dengan satu atau lebih nama paket akan menghapus paket dari lingkungan virtual.

python -m pip show akan menampilkan informasi tentang paket tertentu:

    (tutorial-env) $ python -m pip show requests
    ---
    Metadata-Version: 2.0
    Name: requests
    Version: 2.7.0
    Summary: Python HTTP for Humans.
    Home-page: http://python-requests.org
    Author: Kenneth Reitz
    Author-email: me@kennethreitz.com
    License: Apache 2.0
    Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
    Requires:

python -m pip list akan menampilkan semua paket yang diinstal di lingkungan virtual:

    (tutorial-env) $ python -m pip list
    novas (3.1.1.3)
    numpy (1.9.2)
    pip (7.0.3)
    requests (2.7.0)
    setuptools (16.0)

python -m pip freeze akan menghasilkan daftar paket terinstal yang serupa, tetapi outputnya menggunakan format yang diharapkan python -m pip install. Konvensi umum adalah meletakkan daftar ini dalam file persyaratan.txt:

    (tutorial-env) $ python -m pip freeze > requirements.txt
    (tutorial-env) $ cat requirements.txt
    novas==3.1.1.3
    numpy==1.9.2
    requests==2.7.0


Requirement.txt kemudian dapat dikomit ke kontrol versi dan dikirim sebagai bagian dari aplikasi. Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan install -r:

    (tutorial-env) $ python -m pip install -r requirements.txt
    Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
      ...
    Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
      ...
    Collecting requests==2.7.0 (from -r requirements.txt (line 3))
      ...
    Installing collected packages: novas, numpy, requests
      Running setup.py install for novas
    Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0

pip memiliki lebih banyak opsi. Konsultasikan panduan Instalasi Modul Python untuk dokumentasi lengkap untuk pip. Saat Anda telah menulis sebuah paket dan ingin membuatnya tersedia di Indeks Paket Python, bacalah panduan pengguna pengemasan Python.
