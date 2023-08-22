# 10. Tur Singkat Perpustakaan Standar (Tur Singkat Perpustakaan Standar)
***10.1. Antarmuka Sistem Operasi***

Modul os menyediakan lusinan fungsi untuk berinteraksi dengan sistem operasi:

    >>>import os
    >>>os.getcwd()      # Return the current working directory
    'C:\\Python311'
    >>>os.chdir('/server/accesslogs')   # Change current working directory
    >>>os.system('mkdir today')   # Run the command mkdir in the system shell
    0

Pastikan untuk menggunakan gaya import os daripada from os import *. Ini akan menjaga os.open() dari membayangi fungsi built-in open() yang beroperasi jauh berbeda.

Fungsi built-in dir() dan help() berguna sebagai bantuan interaktif untuk bekerja dengan modul besar seperti os:

    >>>import os
    >>>dir(os)
    <returns a list of all module functions>
    >>>help(os)
    <returns an extensive manual page created from the module's docstrings>

Untuk tugas manajemen file dan direktori harian, modul shutil menyediakan antarmuka tingkat tinggi yang lebih mudah digunakan:

    >>>import shutil
    >>>shutil.copyfile('data.db', 'archive.db')
    'archive.db'
    >>>shutil.move('/build/executables', 'installdir')
    'installdir'

***10.2. File Wildcard***

Modul glob menyediakan fungsi untuk membuat daftar file dari pencarian wildcard direktori:

    >>>import sys
    >>>print(sys.argv)
    ['demo.py', 'one', 'two', 'three']


Modul argparse menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah. Skrip berikut mengekstrak satu atau lebih nama file dan sejumlah baris opsional yang akan ditampilkan:

    import argparse
    
    parser = argparse.ArgumentParser(
        prog='top',
        description='Show top lines from each file')
    parser.add_argument('filenames', nargs='+')
    parser.add_argument('-l', '--lines', type=int, default=10)
    args = parser.parse_args()
    print(args)

Saat dijalankan pada baris perintah dengan python top.py --lines=5 alpha.txt beta.txt, skrip menyetel args.lines ke 5 dan args.filenames ke ['alpha.txt', 'beta.txt'].

***10.4. Pengalihan Keluaran Kesalahan dan Penghentian Program***

Modul sys juga memiliki atribut untuk stdin, stdout, dan stderr. Yang terakhir berguna untuk memancarkan peringatan dan pesan kesalahan agar terlihat bahkan ketika stdout telah dialihkan:

    >>>sys.stderr.write('Warning, log file not found starting a new one\n')
    Warning, log file not found starting a new one

Cara paling langsung untuk menghentikan skrip adalah dengan menggunakan sys.exit().

***10.5. String Pattern Matching***

Modul re menyediakan alat ekspresi reguler untuk pemrosesan string tingkat lanjut. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan optimal:

    >>>import re
    >>>re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
    ['foot', 'fell', 'fastest']
    >>>re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
    'cat in the hat'
    
Ketika hanya kemampuan sederhana yang diperlukan, metode string lebih disukai karena lebih mudah dibaca dan di-debug:

    >>>'tea for too'.replace('too', 'two')
    'tea for two'

***10.6. Mathematics***

Modul matematika memberikan akses ke fungsi perpustakaan C yang mendasari untuk matematika floating point:

    >>>import math
    >>>math.cos(math.pi / 4)
    0.70710678118654757
    >>>math.log(1024, 2)
    10.0

Modul acak menyediakan alat untuk membuat pilihan acak:

    >>>import random
    >>>random.choice(['apple', 'pear', 'banana'])
    'apple'
    >>>random.sample(range(100), 10)   # sampling without replacement
    [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
    >>>random.random()    # random float
    0.17970987693706186
    >>>random.randrange(6)    # random integer chosen from range(6)
    4

Modul statistik menghitung properti statistik dasar (rata-rata, median, varians, dll.) dari data numerik:

    >>>import statistics
    >>>data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    >>>statistics.mean(data)
    1.6071428571428572
    >>>statistics.median(data)
    1.25
    >>>statistics.variance(data)
    1.3720238095238095

Proyek SciPy <https://scipy.org> memiliki banyak modul lain untuk perhitungan numerik.

***10.7. Akses internet***

Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua yang paling sederhana adalah urllib.request untuk mengambil data dari URL dan smtplib untuk mengirim email:

    >>>from urllib.request import urlopen
    >>>with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    ...    for line in response:
    ...        line = line.decode()             # Convert bytes to a str
    ...        if line.startswith('datetime'):
    ...            print(line.rstrip())         # Remove trailing newline
    ...
    datetime: 2022-01-01T01:36:47.689215+00:00
    
    >>>import smtplib
    >>>server = smtplib.SMTP('localhost')
    >>>server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
    ..."""To: jcaesar@example.org
    ...From: soothsayer@example.org
    ...
    ...Beware the Ides of March.
    ...""")
    >>>server.quit()

(Perhatikan bahwa contoh kedua memerlukan server email yang berjalan di localhost.)

***10.8. Tanggal dan Waktu***

Modul datetime menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara sederhana dan kompleks. Meskipun aritmatika tanggal dan waktu didukung, fokus penerapannya adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi keluaran. Modul ini juga mendukung objek yang sadar zona waktu.

    >>> # dates are easily constructed and formatted
    >>> from datetime import date
    >>> now = date.today()
    >>> now
    datetime.date(2003, 12, 2)
    >>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
    '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'
    
    >>> # dates support calendar arithmetic
    >>> birthday = date(1964, 7, 31)
    >>> age = now - birthday
    >>> age.days
    14368

***10.9. Kompresi Data***

Format pengarsipan dan kompresi data umum didukung langsung oleh modul termasuk: zlib, gzip, bz2, lzma, zipfile, dan tarfile.

    >>> import zlib
    >>> s = b'witch which has which witches wrist watch'
    >>> len(s)
    41
    >>> t = zlib.compress(s)
    >>> len(t)
    37
    >>> zlib.decompress(t)
    b'witch which has which witches wrist watch'
    >>> zlib.crc32(s)
    226805979

***10.10. Pengukuran Kinerja***

Beberapa pengguna Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari berbagai pendekatan untuk masalah yang sama. Python menyediakan alat pengukuran yang segera menjawab pertanyaan tersebut.

Misalnya, mungkin tergoda untuk menggunakan fitur packing dan unpacking tuple daripada pendekatan tradisional untuk bertukar argumen. Modul timeit dengan cepat menunjukkan keunggulan kinerja sederhana:

    >>> from timeit import Timer
    >>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
    0.57535828626024577
    >>> Timer('a,b = b,a', 'a=1; b=2').timeit()
    0.54962537085770791

Berbeda dengan tingkat granularitas timeit yang baik, modul profile dan pstats menyediakan alat untuk mengidentifikasi bagian waktu kritis dalam blok kode yang lebih besar.

***10.11. Kontrol kualitas***

Salah satu pendekatan untuk mengembangkan perangkat lunak berkualitas tinggi adalah dengan menulis pengujian untuk setiap fungsi saat fungsi tersebut dikembangkan dan menjalankan pengujian tersebut secara berkala selama proses pengembangan.

Modul doctest menyediakan alat untuk memindai modul dan memvalidasi tes yang tertanam dalam docstrings program. Konstruksi pengujian semudah memotong-dan-menempelkan panggilan biasa beserta hasilnya ke dalam docstring. Hal ini meningkatkan dokumentasi dengan memberikan contoh kepada pengguna dan memungkinkan modul doctest memastikan kode tetap sesuai dengan dokumentasi:

    def average(values):
        """Computes the arithmetic mean of a list of numbers.
    
        >>> print(average([20, 30, 70]))
        40.0
        """
        return sum(values) / len(values)
    
    import doctest
    doctest.testmod()   # automatically validate the embedded tests


Modul unittest tidak semudah modul doctest, tetapi memungkinkan serangkaian pengujian yang lebih komprehensif untuk dipertahankan dalam file terpisah:

    import unittest
    
    class TestStatisticalFunctions(unittest.TestCase):
    
        def test_average(self):
            self.assertEqual(average([20, 30, 70]), 40.0)
            self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
            with self.assertRaises(ZeroDivisionError):
                average([])
            with self.assertRaises(TypeError):
                average(20, 30, 70)
    
    unittest.main()  # Calling from the command line invokes all tests

***10.12. Sudah Termasuk Baterai***

Python memiliki filosofi "termasuk baterai". Ini paling baik dilihat melalui kemampuan canggih dan tangguh dari paket-paketnya yang lebih besar. Misalnya:

- Modul xmlrpc.client dan xmlrpc.server membuat penerapan panggilan prosedur jarak jauh menjadi tugas yang hampir sepele. Terlepas dari nama modul, tidak diperlukan pengetahuan langsung atau penanganan XML.

- Paket email adalah pustaka untuk mengelola pesan email, termasuk MIME dan dokumen pesan berbasis RFC 2822 lainnya. Tidak seperti smtplib dan poplib yang benar-benar mengirim dan menerima pesan, paket email memiliki perangkat lengkap untuk membangun atau mendekode struktur pesan yang kompleks (termasuk lampiran) dan untuk mengimplementasikan protokol penyandian dan header internet.

- Paket json memberikan dukungan kuat untuk mem-parsing format pertukaran data populer ini. Modul csv mendukung pembacaan dan penulisan file secara langsung dalam format Comma-Separated Value, umumnya didukung oleh database dan spreadsheet. Pemrosesan XML didukung oleh paket xml.etree.ElementTree, xml.dom dan xml.sax. Bersama-sama, modul dan paket ini sangat menyederhanakan pertukaran data antara aplikasi Python dan alat lainnya.

- Modul sqlite3 adalah pembungkus untuk perpustakaan database SQLite, menyediakan database persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL yang sedikit tidak standar.

- Internasionalisasi didukung oleh sejumlah modul termasuk gettext, locale, dan paket codec.

# 11. Tur Singkat Perpustakaan Standar — Bagian II

Tur kedua ini mencakup modul lebih lanjut yang mendukung kebutuhan pemrograman profesional. Modul-modul ini jarang muncul dalam skrip kecil.

***11.1. Pemformatan Keluaran***

Modul reprlib menyediakan versi repr() yang disesuaikan untuk tampilan singkat dari wadah bersarang besar atau bersarang dalam:

    >>> import reprlib
    >>> reprlib.repr(set('supercalifragilisticexpialidocious'))
    "{'a', 'c', 'd', 'e', 'f', 'g', ...}"

Modul pprint menawarkan kontrol yang lebih canggih atas pencetakan objek bawaan dan yang ditentukan pengguna dengan cara yang dapat dibaca oleh juru bahasa. Jika hasilnya lebih panjang dari satu baris, “printer cantik” menambahkan jeda baris dan lekukan untuk menampilkan struktur data dengan lebih jelas:

    >>> import pprint
    >>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    ...    'yellow'], 'blue']]]
    ...
    >>>pprint.pprint(t, width=30)
    [[[['black', 'cyan'],
       'white',
       ['green', 'red']],
      [['magenta', 'yellow'],
       'blue']]]


Modul textwrap memformat paragraf teks agar sesuai dengan lebar layar yang diberikan:

    >>> import textwrap
    >>> doc = """The wrap() method is just like fill() except that it returns
    ... a list of strings instead of one big string with newlines to separate
    ... the wrapped lines."""
    ...
    >>> print(textwrap.fill(doc, width=40))
    The wrap() method is just like fill()
    except that it returns a list of strings
    instead of one big string with newlines
    to separate the wrapped lines.

Modul lokal mengakses database format data khusus budaya. Atribut pengelompokan fungsi format lokal menyediakan cara langsung memformat angka dengan pemisah grup:

    >>> import locale
    >>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
    'English_United States.1252'
    >>> conv = locale.localeconv()          # get a mapping of conventions
    >>> x = 1234567.8
    >>> locale.format("%d", x, grouping=True)
    '1,234,567'
    >>> locale.format_string("%s%.*f", (conv['currency_symbol'],
                         conv['frac_digits'], x), grouping=True)
    '$1,234,567.80'


***11.2. Templat***

Modul string menyertakan kelas Templat serbaguna dengan sintaks sederhana yang cocok untuk diedit oleh pengguna akhir. Ini memungkinkan pengguna untuk menyesuaikan aplikasi mereka tanpa harus mengubah aplikasi.

Formatnya menggunakan nama placeholder yang dibentuk oleh $ dengan pengidentifikasi Python yang valid (karakter alfanumerik dan garis bawah). Mengelilingi placeholder dengan tanda kurung memungkinkannya diikuti oleh lebih banyak huruf alfanumerik tanpa spasi. Menulis $$ menghasilkan satu $ yang lolos:

    >>> from string import Template
    >>> t = Template('${village}folk send $$10 to $cause.')
    >>> t.substitute(village='Nottingham', cause='the ditch fund')
    'Nottinghamfolk send $10 to the ditch fund.'

Metode pengganti () memunculkan KeyError saat placeholder tidak disediakan dalam kamus atau argumen kata kunci. Untuk aplikasi gaya gabungan surat, data yang diberikan pengguna mungkin tidak lengkap dan metode safe_substitute() mungkin lebih tepat — metode ini akan membiarkan placeholder tidak berubah jika data hilang:

    >>> t = Template('Return the $item to $owner.')
    >>> d = dict(item='unladen swallow')
    >>> t.substitute(d)
    Traceback (most recent call last):
      ...
    KeyError: 'owner'
    >>> t.safe_substitute(d)
    'Return the unladen swallow to $owner.'

Subkelas templat dapat menentukan pembatas khusus. Misalnya, utilitas penggantian nama batch untuk browser foto dapat memilih untuk menggunakan tanda persen untuk placeholder seperti tanggal saat ini, nomor urut gambar, atau format file:

    >>> import time, os.path
    >>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
    >>> class BatchRename(Template):
    ...    delimiter = '%'
    ...
    >>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
    Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f
    
    >>> t = BatchRename(fmt)
    >>> date = time.strftime('%d%b%y')
    >>> for i, filename in enumerate(photofiles):
    ...    base, ext = os.path.splitext(filename)
    ...    newname = t.substitute(d=date, n=i, f=ext)
    ...    print('{0} --> {1}'.format(filename, newname))
    
    img_1074.jpg --> Ashley_0.jpg
    img_1076.jpg --> Ashley_1.jpg
    img_1077.jpg --> Ashley_2.jpg


Aplikasi lain untuk templating adalah memisahkan logika program dari detail berbagai format keluaran. Hal ini memungkinkan untuk mengganti template khusus untuk file XML, laporan teks biasa, dan laporan web HTML.

***11.3. Bekerja dengan Tata Letak Catatan Data Biner***

Modul struct menyediakan fungsi pack() dan unpack() untuk bekerja dengan format rekaman biner dengan panjang variabel. Contoh berikut menunjukkan cara mengulang informasi header dalam file ZIP tanpa menggunakan modul zipfile. Kode paket "H" dan "I" masing-masing mewakili dua dan empat byte angka yang tidak ditandatangani. "<" menunjukkan bahwa ukurannya standar dan dalam urutan byte little-endian:

    import struct
    
    with open('myfile.zip', 'rb') as f:
        data = f.read()
    
    start = 0
    for i in range(3):                      # show the first 3 file headers
        start += 14
        fields = struct.unpack('<IIIHH', data[start:start+16])
        crc32, comp_size, uncomp_size, filenamesize, extra_size = fields
    
        start += 16
        filename = data[start:start+filenamesize]
        start += filenamesize
        extra = data[start:start+extra_size]
        print(filename, hex(crc32), comp_size, uncomp_size)
    
        start += extra_size + comp_size     # skip to the next header

***11.4. Multi-threading***

Threading adalah teknik untuk memisahkan tugas yang tidak bergantung secara berurutan. Utas dapat digunakan untuk meningkatkan daya tanggap aplikasi yang menerima input pengguna saat tugas lain berjalan di latar belakang. Kasus penggunaan terkait sedang menjalankan I/O secara paralel dengan perhitungan di utas lainnya.

Kode berikut menunjukkan bagaimana modul threading tingkat tinggi dapat menjalankan tugas di latar belakang sementara program utama terus berjalan:

    import threading, zipfile
    
    class AsyncZip(threading.Thread):
        def __init__(self, infile, outfile):
            threading.Thread.__init__(self)
            self.infile = infile
            self.outfile = outfile
    
        def run(self):
            f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
            f.write(self.infile)
            f.close()
            print('Finished background zip of:', self.infile)
    
    background = AsyncZip('mydata.txt', 'myarchive.zip')
    background.start()
    print('The main program continues to run in foreground.')
    
    background.join()    # Wait for the background task to finish
    print('Main program waited until background was done.')

Tantangan utama aplikasi multi-thread adalah mengoordinasikan thread yang berbagi data atau sumber daya lainnya. Untuk itu, modul threading menyediakan sejumlah primitif sinkronisasi termasuk kunci, peristiwa, variabel kondisi, dan semafor.

Meskipun alat-alat tersebut ampuh, kesalahan desain kecil dapat mengakibatkan masalah yang sulit untuk direproduksi. Jadi, pendekatan yang lebih disukai untuk koordinasi tugas adalah dengan memusatkan semua akses ke sumber daya dalam satu thread dan kemudian menggunakan modul antrian untuk memasukkan thread tersebut dengan permintaan dari thread lain. Aplikasi yang menggunakan objek Queue untuk komunikasi dan koordinasi antar-thread lebih mudah dirancang, lebih mudah dibaca, dan lebih andal.

***11.5. Logging***

Modul logging menawarkan sistem logging berfitur lengkap dan fleksibel. Sederhananya, pesan log dikirim ke file atau ke sys.stderr:

    import logging
    logging.debug('Debugging information')
    logging.info('Informational message')
    logging.warning('Warning:config file %s not found', 'server.conf')
    logging.error('Error occurred')
    logging.critical('Critical error -- shutting down')

Ini menghasilkan output berikut:

    WARNING:root:Warning:config file server.conf not found
    ERROR:root:Error occurred
    CRITICAL:root:Critical error -- shutting down

Secara default, pesan informasi dan debug disembunyikan dan output dikirim ke kesalahan standar. Opsi keluaran lainnya termasuk merutekan pesan melalui email, datagram, soket, atau ke Server HTTP. Filter baru dapat memilih rute yang berbeda berdasarkan prioritas pesan: DEBUG, INFO, WARNING, ERROR, dan CRITICAL.

Sistem logging dapat dikonfigurasi langsung dari Python atau dapat dimuat dari file konfigurasi yang dapat diedit pengguna untuk logging yang disesuaikan tanpa mengubah aplikasi.

***11.6. Referensi Lemah***

Python melakukan manajemen memori otomatis (penghitungan referensi untuk sebagian besar objek dan pengumpulan sampah untuk menghilangkan siklus). Memori dibebaskan segera setelah referensi terakhir ke memori tersebut dihilangkan.

Pendekatan ini berfungsi dengan baik untuk sebagian besar aplikasi tetapi kadang-kadang ada kebutuhan untuk melacak objek hanya selama objek tersebut sedang digunakan oleh sesuatu yang lain. Sayangnya, hanya melacaknya akan menghasilkan referensi yang menjadikannya permanen. Modul lemahref menyediakan alat untuk melacak objek tanpa membuat referensi. Ketika objek tidak lagi diperlukan, objek tersebut secara otomatis dihapus dari tabel lemah dan panggilan balik dipicu untuk objek lemah. Aplikasi yang umum mencakup objek caching yang mahal untuk dibuat:

    >>> import weakref, gc
    >>> class A:
    ...    def __init__(self, value):
    ...        self.value = value
    ...    def __repr__(self):
    ...        return str(self.value)
    ...
    >>> a = A(10)                   # create a reference
    >>> d = weakref.WeakValueDictionary()
    >>> d['primary'] = a            # does not create a reference
    >>> d['primary']                # fetch the object if it is still alive
    10
    >>> del a                       # remove the one reference
    >>> gc.collect()                # run garbage collection right away
    0
    >>> d['primary']                # entry was automatically removed
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        d['primary']                # entry was automatically removed
      File "C:/python311/lib/weakref.py", line 46, in __getitem__
        o = self.data[key]()
    KeyError: 'primary'

***11.7. Alat untuk Bekerja dengan Daftar***

Banyak kebutuhan struktur data yang dapat dipenuhi dengan tipe daftar bawaan. Namun, terkadang diperlukan penerapan alternatif dengan trade-off kinerja yang berbeda.

Modul array menyediakan objek array() seperti daftar yang hanya menyimpan data homogen dan menyimpannya dengan lebih kompak. Contoh berikut menunjukkan larik angka yang disimpan sebagai angka biner tak bertanda dua byte (kode ketik "H") daripada 16 byte biasa per entri untuk daftar reguler objek int Python:

    >>> from array import array
    >>> a = array('H', [4000, 10, 700, 22222])
    >>> sum(a)
    26932
    >>> a[1:3]
    array('H', [10, 700])

Modul koleksi menyediakan objek deque() seperti daftar dengan penambahan dan pop yang lebih cepat dari sisi kiri tetapi pencarian lebih lambat di tengah. Objek-objek ini sangat cocok untuk mengimplementasikan antrian dan pencarian pohon luasnya yang pertama:

    >>> from collections import deque
    >>> d = deque(["task1", "task2", "task3"])
    >>> d.append("task4")
    >>> print("Handling", d.popleft())
    Handling task

    unsearched = deque([starting_node])
    def breadth_first_search(unsearched):
        node = unsearched.popleft()
        for m in gen_moves(node):
            if is_goal(m):
                return m
            unsearched.append(m)


Selain implementasi daftar alternatif, perpustakaan juga menawarkan alat lain seperti modul membagi dua dengan fungsi untuk memanipulasi daftar yang diurutkan:

    >>> import bisect
    >>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
    >>> bisect.insort(scores, (300, 'ruby'))
    >>> scores
    [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

Modul heapq menyediakan fungsi untuk mengimplementasikan tumpukan berdasarkan daftar reguler. Entri bernilai terendah selalu disimpan di posisi nol. Ini berguna untuk aplikasi yang berulang kali mengakses elemen terkecil tetapi tidak ingin menjalankan pengurutan daftar lengkap:

    >>> from heapq import heapify, heappop, heappush
    >>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    >>> heapify(data)                      # rearrange the list into heap order
    >>> heappush(data, -5)                 # add a new entry
    >>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
    [-5, 0, 1]

***11.8. Aritmatika Titik Mengambang Desimal***

Modul desimal menawarkan tipe data Desimal untuk aritmatika floating point desimal. Dibandingkan dengan implementasi float bawaan dari floating point biner, kelas ini sangat membantu

- aplikasi keuangan dan penggunaan lain yang memerlukan representasi desimal yang tepat,

- kontrol atas presisi,

- kontrol atas pembulatan untuk memenuhi persyaratan hukum atau peraturan,

- pelacakan tempat desimal yang signifikan, atau

- aplikasi di mana pengguna mengharapkan hasilnya sesuai dengan perhitungan yang dilakukan dengan tangan.

Misalnya, menghitung pajak 5% untuk tagihan telepon sebesar 70 sen memberikan hasil yang berbeda dalam floating point desimal dan floating point biner. Perbedaannya menjadi signifikan jika hasilnya dibulatkan ke sen terdekat:

    >>> from decimal import *
    >>> round(Decimal('0.70') * Decimal('1.05'), 2)
    Decimal('0.74')
    >>> round(.70 * 1.05, 2)
    0.73

Hasil Desimal mempertahankan angka nol di belakangnya, secara otomatis menyimpulkan signifikansi empat tempat dari perkalian dengan signifikansi dua tempat. Desimal mereproduksi matematika seperti yang dilakukan dengan tangan dan menghindari masalah yang dapat muncul ketika floating point biner tidak dapat mewakili kuantitas desimal secara tepat.

Representasi yang tepat memungkinkan kelas Desimal melakukan penghitungan modulo dan pengujian kesetaraan yang tidak cocok untuk floating point biner:

    >>> Decimal('1.00') % Decimal('.10')
    Decimal('0.00')
    >>> 1.00 % 0.10
    0.09999999999999995
    
    >>> sum([Decimal('0.1')]*10) == Decimal('1.0')
    True
    >>> sum([0.1]*10) == 1.0
    False


Modul desimal menyediakan aritmatika dengan presisi sebanyak yang diperlukan:

    >>> getcontext().prec = 36
    >>> Decimal(1) / Decimal(7)
    Decimal('0.142857142857142857142857142857142857')
