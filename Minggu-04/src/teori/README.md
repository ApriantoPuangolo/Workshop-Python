# BAB 6
# Modules (Modul)
Modul adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran .py ditambahkan. Di dalam modul, nama modul (sebagai string) tersedia sebagai nilai variabel global __name__. Misalnya, gunakan editor teks favorit Anda untuk membuat file bernama fibo.py di direktori saat ini dengan konten berikut:

    #Fibonacci numbers module

    def fib(n):    # write Fibonacci series up to n
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()

    def fib2(n):   # return Fibonacci series up to n
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result
Sekarang masukkan juru bahasa Python dan impor modul ini dengan perintah berikut:

    >>> import fibo
Ini tidak menambahkan nama fungsi yang didefinisikan di fibo langsung ke namespace saat ini (lihat Python Scopes dan Namespaces untuk detail lebih lanjut); itu hanya menambahkan nama modul fibo di sana. Menggunakan nama modul Anda dapat mengakses fungsi:

    >>>fibo.fib(1000)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
    >>>fibo.fib2(100)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    >>>fibo.__name__
    'fibo'
Jika Anda ingin sering menggunakan suatu fungsi, Anda dapat menetapkannya ke nama lokal:

    >>>fib = fibo.fib
    >>>fib(500)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
# More on Modules (Lebih lanjut tentang Modul)
Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Mereka dieksekusi hanya saat pertama kali nama modul ditemukan dalam pernyataan impor. 1 (Mereka juga dijalankan jika file dijalankan sebagai skrip.)

Setiap modul memiliki ruang nama pribadinya sendiri, yang digunakan sebagai ruang nama global oleh semua fungsi yang ditentukan dalam modul. Dengan demikian, pembuat modul dapat menggunakan variabel global di dalam modul tanpa khawatir tentang bentrokan yang tidak disengaja dengan variabel global pengguna. Di sisi lain, jika Anda tahu apa yang Anda lakukan, Anda dapat menyentuh variabel global modul dengan notasi yang sama yang digunakan untuk merujuk fungsinya, modname.itemname.

Modul dapat mengimpor modul lain. Merupakan kebiasaan tetapi tidak diharuskan untuk menempatkan semua pernyataan impor di awal modul (atau skrip, dalam hal ini). Nama modul yang diimpor, jika ditempatkan di tingkat atas modul (di luar fungsi atau kelas apa pun), ditambahkan ke ruang nama global modul.

Ada varian dari pernyataan impor yang mengimpor nama dari modul langsung ke ruang nama modul pengimpor. Misalnya:

    >>>from fibo import fib, fib2
    >>>fib(500)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
Ini tidak memperkenalkan nama modul dari mana impor diambil di namespace lokal (jadi dalam contoh, fibo tidak ditentukan).

Bahkan ada varian untuk mengimpor semua nama yang ditentukan modul:

    >>>from fibo import *
    >>>fib(500)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
Ini mengimpor semua nama kecuali yang dimulai dengan garis bawah (_). Dalam banyak kasus, pemrogram Python tidak menggunakan fasilitas ini karena fasilitas ini memperkenalkan serangkaian nama yang tidak diketahui ke dalam juru bahasa, mungkin menyembunyikan beberapa hal yang telah Anda tetapkan.

Perhatikan bahwa secara umum praktik mengimpor * dari modul atau paket tidak disukai, karena sering menyebabkan kode sulit dibaca. Namun, tidak apa-apa menggunakannya untuk menghemat pengetikan dalam sesi interaktif.

Jika nama modul diikuti dengan as, maka nama yang mengikuti as terikat langsung ke modul yang diimpor.

    Catatan : Untuk alasan efisiensi, setiap modul hanya diimpor satu kali per sesi juru bahasa. 
    Oleh karena itu, jika Anda mengubah modul, Anda harus memulai ulang penerjemah – atau, jika hanya satu modul yang ingin Anda uji secara interaktif, gunakan importlib.reload(), mis. 
    impor importlib; importlib.reload(namamodul).
# Executing modules as script (Menjalankan modul sebagai skrip)
Saat Anda menjalankan modul Python dengan :

    python fibo.py <arguments>
kode dalam modul akan dieksekusi, sama seperti jika Anda mengimpornya, tetapi dengan "__ name __" disetel ke " __ main __" . Itu artinya dengan menambahkan kode ini di akhir modul Anda:

    if __name__ == "__main__":
        import sys
        fib(int(sys.argv[1]))

Anda dapat menjadikan file tersebut dapat digunakan sebagai skrip dan juga sebagai modul yang dapat diimpor, karena kode yang mem-parsing baris perintah hanya berjalan jika modul dijalankan sebagai file "utama":

    $ python fibo.py 50
    0 1 1 2 3 5 8 13 21 34
Jika modul diimpor, kode tidak dijalankan:

    >>>import fibo
    >>>
Ini sering digunakan baik untuk menyediakan antarmuka pengguna yang mudah digunakan ke modul, atau untuk tujuan pengujian (menjalankan modul saat skrip menjalankan rangkaian pengujian).
# The Module Search Path (Jalur Pencarian Modul)
Saat modul bernama spam diimpor, interpreter pertama-tama akan mencari modul bawaan dengan nama tersebut. Nama modul ini tercantum dalam sys.builtin_module_names. Jika tidak ditemukan, ia akan mencari file bernama spam.py di daftar direktori yang diberikan oleh variabel sys.path. sys.path diinisialisasi dari lokasi berikut:

Direktori yang berisi skrip input (atau direktori saat ini ketika tidak ada file yang ditentukan).

PYTHONPATH (daftar nama direktori, dengan sintaks yang sama dengan variabel shell PATH).

Default yang bergantung pada penginstalan (berdasarkan konvensi termasuk direktori paket situs, ditangani oleh modul situs).

Lebih jelasnya ada di Inisialisasi jalur pencarian modul sys.path.

    Catatan Pada sistem file yang mendukung symlink, direktori yang berisi skrip masukan dihitung setelah symlink diikuti. 
    Dengan kata lain direktori yang berisi symlink tidak ditambahkan ke jalur pencarian modul.
Setelah inisialisasi, program Python dapat memodifikasi sys.path. Direktori yang berisi skrip yang sedang dijalankan ditempatkan di awal jalur pencarian, di depan jalur pustaka standar. Ini berarti skrip di direktori itu akan dimuat alih-alih modul dengan nama yang sama di direktori perpustakaan. Ini adalah kesalahan kecuali penggantian dimaksudkan. Lihat bagian Modul Standar untuk informasi lebih lanjut.
# “Compiled” Python files (File Python yang "dikompilasi")
Untuk mempercepat pemuatan modul, Python meng-cache versi terkompilasi dari setiap modul di direktori __pycache__ dengan nama module.version.pyc, di mana versi menyandikan format file yang dikompilasi; umumnya berisi nomor versi Python. Misalnya, dalam rilis CPython 3.3, versi spam.py yang dikompilasi akan di-cache sebagai __ pycache__/spam.cpython-33.pyc. Konvensi penamaan ini memungkinkan modul yang dikompilasi dari rilis yang berbeda dan versi Python yang berbeda untuk hidup berdampingan.

Python memeriksa tanggal modifikasi sumber terhadap versi yang dikompilasi untuk melihat apakah sudah kedaluwarsa dan perlu dikompilasi ulang. Ini adalah proses yang sepenuhnya otomatis. Selain itu, modul yang dikompilasi tidak bergantung pada platform, sehingga pustaka yang sama dapat digunakan bersama di antara sistem dengan arsitektur yang berbeda.

Python tidak memeriksa cache dalam dua keadaan. Pertama, selalu mengkompilasi ulang dan tidak menyimpan hasil modul yang dimuat langsung dari baris perintah. Kedua, tidak memeriksa cache jika tidak ada modul sumber. Untuk mendukung distribusi non-sumber (hanya dikompilasi), modul yang dikompilasi harus berada di direktori sumber, dan tidak boleh ada modul sumber.
# Standard Modules (Modul Standar)
Python hadir dengan pustaka modul standar, dijelaskan dalam dokumen terpisah, Referensi Pustaka Python (“Referensi Pustaka” selanjutnya). Beberapa modul dibangun ke dalam juru bahasa; ini memberikan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke primitif sistem operasi seperti panggilan sistem. Kumpulan modul tersebut adalah opsi konfigurasi yang juga bergantung pada platform yang mendasarinya. Misalnya, modul winreg hanya tersedia di sistem Windows. Satu modul tertentu patut mendapat perhatian: sys, yang dibangun di setiap juru bahasa Python. Variabel sys.ps1 dan sys.ps2 mendefinisikan string yang digunakan sebagai prompt primer dan sekunder:

    >>>import sys
    >>>sys.ps1
    '>>> '
    >>>sys.ps2
    '... '
    >>>sys.ps1 = 'C> '
    C> print('Yuck!')
    Yuck!
    C>
# The dir() Function (Fungsi dir())
Fungsi built-in dir() digunakan untuk mengetahui nama mana yang didefinisikan oleh modul. Ini mengembalikan daftar string yang diurutkan:

    >>>import fibo, sys
    >>>dir(fibo)
    ['__name__', 'fib', 'fib2']
    >>>dir(sys)  
    ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
     '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
     '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
     '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
     '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
     'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
     'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
     'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
     'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
     'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
     'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
     'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
     'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
     'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
     'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
     'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
     'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
# Packages (Paket)
Paket adalah cara menyusun ruang nama modul Python dengan menggunakan "nama modul bertitik". Misalnya, nama modul A.B menunjuk submodule bernama B dalam sebuah paket bernama A. Sama seperti penggunaan modul menyelamatkan penulis modul yang berbeda dari keharusan khawatir tentang nama variabel global masing-masing, penggunaan nama modul bertitik menghemat penulis paket multi-modul seperti NumPy atau Pillow karena harus mengkhawatirkan nama modul masing-masing.

Misalkan Anda ingin merancang kumpulan modul ("paket") untuk penanganan file suara dan data suara yang seragam. Ada banyak format file suara yang berbeda (biasanya dikenali dari ekstensinya, misalnya: .wav, .aiff, .au), jadi Anda mungkin perlu membuat dan memelihara koleksi modul yang terus bertambah untuk konversi antara berbagai format file. Ada juga banyak operasi berbeda yang mungkin ingin Anda lakukan pada data suara (seperti mencampur, menambahkan gema, menerapkan fungsi equalizer, membuat efek stereo buatan), jadi selain itu Anda akan menulis aliran modul tanpa henti untuk dilakukan. operasi ini. Berikut adalah kemungkinan struktur untuk paket Anda (dinyatakan dalam sistem file hierarkis):

    sound/                          Top-level package
          __init__.py               Initialize the sound package
          formats/                  Subpackage for file format conversions
                  __init__.py
                  wavread.py
                  wavwrite.py
                  aiffread.py
                  aiffwrite.py
                  auread.py
                  auwrite.py
                  ...
          effects/                  Subpackage for sound effects
                  __init__.py
                  echo.py
                  surround.py
                  reverse.py
                  ...
          filters/                  Subpackage for filters
                  __init__.py
                  equalizer.py
                  vocoder.py
                  karaoke.py
                  ...
Saat mengimpor paket, Python mencari melalui direktori di sys.path untuk mencari subdirektori paket.

File __init__.py diperlukan untuk membuat Python memperlakukan direktori yang berisi file tersebut sebagai paket. Ini mencegah direktori dengan nama umum, seperti string, menyembunyikan modul valid secara tidak sengaja yang muncul kemudian di jalur pencarian modul. Dalam kasus yang paling sederhana, __init__.py bisa berupa file kosong, tetapi juga dapat mengeksekusi kode inisialisasi untuk paket atau menyetel variabel __all__, yang akan dijelaskan nanti.

Pengguna paket dapat mengimpor modul individual dari paket, misalnya:

    import sound.effects.echo
Ini memuat submodule sound.efek.echo. Itu harus dirujuk dengan nama lengkapnya.

    sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
Cara alternatif mengimpor submodule adalah:

    from sound.effects import echo
Perhatikan : bahwa saat menggunakan dari item impor paket, item tersebut dapat berupa submodul (atau subpaket) dari paket, atau beberapa nama lain yang ditentukan dalam paket, seperti fungsi, kelas, atau variabel. Pernyataan impor pertama-tama menguji apakah item tersebut didefinisikan dalam paket; jika tidak, dianggap sebagai modul dan mencoba memuatnya. Jika gagal menemukannya, pengecualian ImportError dimunculkan.


    FootNotes :
    1.Sebenarnya definisi fungsi juga merupakan 'pernyataan' yang 'dieksekusi'; 
    eksekusi definisi fungsi tingkat modul menambahkan nama fungsi ke namespace global modul.
