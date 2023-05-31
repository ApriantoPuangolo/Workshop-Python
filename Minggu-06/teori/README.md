# Bab 8 Error And Exceptions (Kesalahan dan Pengecualian)
Sampai saat ini pesan kesalahan belum banyak disebutkan, tetapi jika Anda telah mencoba contoh-contohnya, Anda mungkin telah melihat beberapa. Ada (setidaknya) dua jenis kesalahan yang dapat dibedakan: kesalahan sintaksis dan pengecualian.


***8.1. Syntax Errors (Kesalahan Sintaks)***

Kesalahan sintaksis, juga dikenal sebagai kesalahan parsing, mungkin merupakan jenis keluhan paling umum yang Anda dapatkan saat masih mempelajari Python:

    >>>while True print('Hello world')
      File "<stdin>", line 1
        while True print('Hello world')
                       ^
    SyntaxError: invalid syntax
Parser mengulangi baris yang menyinggung dan menampilkan 'panah' kecil yang menunjuk ke titik paling awal di baris tempat kesalahan terdeteksi. Kesalahan disebabkan oleh (atau setidaknya terdeteksi pada) token yang mendahului tanda panah: dalam contoh, kesalahan terdeteksi pada fungsi print(), karena tanda titik dua (':') tidak ada sebelumnya. Nama file dan nomor baris dicetak sehingga Anda tahu ke mana harus mencari jika input berasal dari skrip.

***8.2. Exceptions (pengecualian)***

Bahkan jika sebuah pernyataan atau ekspresi benar secara sintaksis, itu dapat menyebabkan kesalahan ketika upaya dilakukan untuk mengeksekusinya. Kesalahan yang terdeteksi selama eksekusi disebut pengecualian dan tidak fatal tanpa syarat: Anda akan segera belajar cara menanganinya dalam program Python. Namun, sebagian besar pengecualian tidak ditangani oleh program, dan menghasilkan pesan kesalahan seperti yang ditampilkan di sini:

    >>>10 * (1/0)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero
    >>>4 + spam*3
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'spam' is not defined
    >>>'2' + 2
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can only concatenate str (not "int") to str
Baris terakhir dari pesan kesalahan menunjukkan apa yang terjadi. Pengecualian datang dalam berbagai jenis, dan jenisnya dicetak sebagai bagian dari pesan: jenis dalam contoh adalah ZeroDivisionError, NameError, dan TypeError. String yang dicetak sebagai tipe pengecualian adalah nama dari pengecualian bawaan yang terjadi. Ini benar untuk semua pengecualian bawaan, tetapi tidak harus benar untuk pengecualian yang ditentukan pengguna (walaupun ini adalah konvensi yang berguna). Nama pengecualian standar adalah pengidentifikasi bawaan (bukan kata kunci yang dicadangkan). Baris selanjutnya memberikan detail berdasarkan jenis pengecualian dan apa yang menyebabkannya. Bagian sebelumnya dari pesan kesalahan menunjukkan konteks di mana pengecualian terjadi, dalam bentuk stack traceback. Secara umum ini berisi baris sumber daftar traceback stack; namun, ini tidak akan menampilkan baris yang dibaca dari input standar. Pengecualian Bawaan mencantumkan pengecualian bawaan dan artinya.

***8.3. Handling Exceptions (Menangani Pengecualian)***

Dimungkinkan untuk menulis program yang menangani pengecualian yang dipilih. Lihat contoh berikut, yang meminta input dari pengguna hingga integer yang valid telah dimasukkan, tetapi memungkinkan pengguna untuk menginterupsi program (menggunakan Control-C atau apa pun yang didukung oleh sistem operasi); perhatikan bahwa interupsi yang dibuat pengguna ditandai dengan menaikkan pengecualian KeyboardInterrupt.

    >>>while True:
    ...    try:
    ...        x = int(input("Please enter a number: "))
    ...        break
    ...    except ValueError:
    ...        print("Oops!  That was no valid number.  Try again...")
    ...
Pernyataan try berfungsi sebagai berikut.

-Pertama, klausa coba (pernyataan antara kata kunci coba dan kecuali) dijalankan.

-Jika tidak ada pengecualian yang terjadi, klausa pengecualian dilewati dan eksekusi pernyataan try selesai.

-Jika pengecualian terjadi selama eksekusi klausa try, klausa lainnya akan dilewati. Kemudian, jika tipenya cocok dengan pengecualian yang dinamai setelah kata kunci kecuali, klausa kecuali dieksekusi, dan kemudian eksekusi dilanjutkan setelah blok coba/kecuali.

-Jika pengecualian terjadi yang tidak cocok dengan pengecualian yang disebutkan dalam klausa kecuali, itu diteruskan ke pernyataan try luar; jika tidak ada penangan yang ditemukan, itu adalah pengecualian yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.

***8.4. Raising Exceptions (Meningkatkan Pengecualian)***

Pernyataan kenaikan memungkinkan programmer untuk memaksa pengecualian tertentu terjadi. Misalnya:

    >>>raise NameError('HiThere')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: HiThere
Satu-satunya argumen yang akan dinaikkan menunjukkan pengecualian yang akan dimunculkan. Ini harus berupa instance pengecualian atau kelas pengecualian (kelas yang berasal dari BaseException, seperti Pengecualian atau salah satu subkelasnya). Jika sebuah kelas eksepsi dilewatkan, maka secara implisit akan dibuatkan instance-nya dengan memanggil konstruktornya tanpa argumen:

    raise ValueError  # shorthand for 'raise ValueError()'
Jika Anda perlu menentukan apakah pengecualian muncul tetapi tidak berniat untuk menanganinya, bentuk yang lebih sederhana dari pernyataan kenaikan memungkinkan Anda untuk menaikkan kembali pengecualian:

    >>>try:
    ...    raise NameError('HiThere')
    ...except NameError:
    ...    print('An exception flew by!')
    ...    raise
    ...
    An exception flew by!
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
    NameError: HiThere
***8.5. Exception Chaining (Rantai Pengecualian)***


Jika pengecualian yang tidak tertangani terjadi di dalam bagian kecuali, pengecualian yang ditangani akan dilampirkan padanya dan disertakan dalam pesan kesalahan:

    >>>try:
    ...    open("database.sqlite")
    ...except OSError:
    ...    raise RuntimeError("unable to handle error")
    ...
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
    FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
    RuntimeError: unable to handle error
Untuk menunjukkan bahwa pengecualian adalah konsekuensi langsung dari yang lain, pernyataan kenaikan memungkinkan opsional dari klausa:

    # exc must be exception instance or None.
    raise RuntimeError from exc

ini bisa berguna saat Anda mengubah pengecualian. Misalnya:

    >>>def func():
    ...    raise ConnectionError
    ...
    >>>try:
    ...    func()
    ...except ConnectionError as exc:
    ...    raise RuntimeError('Failed to open database') from exc
    ...
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
      File "<stdin>", line 2, in func
    ConnectionError

    The above exception was the direct cause of the following exception:

    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
    RuntimeError: Failed to open database
Itu juga memungkinkan penonaktifan rangkaian pengecualian otomatis menggunakan idiom dari Tidak ada:

    >>>try:
    ...    open('database.sqlite')
    ...except OSError:
    ...   raise RuntimeError from None
    ...
    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
    RuntimeError
***8.6. User-defined Exceptions (Pengecualian yang Ditentukan Pengguna)***

Program dapat menamai pengecualiannya sendiri dengan membuat kelas pengecualian baru (lihat Kelas untuk informasi lebih lanjut tentang kelas Python). Pengecualian biasanya harus diturunkan dari kelas Pengecualian, baik secara langsung maupun tidak langsung.

Kelas pengecualian dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya tetap sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk pengecualian.

Sebagian besar pengecualian ditentukan dengan nama yang diakhiri dengan "Kesalahan", mirip dengan penamaan pengecualian standar.

Banyak modul standar menentukan pengecualian mereka sendiri untuk melaporkan kesalahan yang mungkin terjadi pada fungsi yang mereka tentukan.

***8.7. Defining Clean-up Actions (Mendefinisikan Tindakan Pembersihan)***

Pernyataan try memiliki klausa opsional lain yang dimaksudkan untuk menentukan tindakan pembersihan yang harus dijalankan dalam semua keadaan. Misalnya:

    >>>try:
    ...    raise KeyboardInterrupt
    ...finally:
    ...    print('Goodbye, world!')
    ...
    Goodbye, world!
    KeyboardInterrupt
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
Jika klausa akhirnya ada, klausa akhirnya akan dieksekusi sebagai tugas terakhir sebelum pernyataan try selesai. Klausa akhirnya berjalan apakah pernyataan try menghasilkan pengecualian atau tidak. Poin-poin berikut membahas kasus yang lebih kompleks ketika pengecualian terjadi:

-Jika pengecualian terjadi selama eksekusi klausa try, pengecualian dapat ditangani oleh klausa kecuali. Jika pengecualian tidak ditangani oleh pengecualian klausa, pengecualian akan dimunculkan kembali setelah klausa akhirnya dieksekusi.

-Pengecualian dapat terjadi selama eksekusi klausa kecuali atau yang lain. Sekali lagi, pengecualian dimunculkan kembali setelah klausa akhirnya dieksekusi.

-Jika akhirnya klausa mengeksekusi pernyataan istirahat, lanjutkan atau kembalikan, pengecualian tidak dimunculkan kembali.

-Jika pernyataan try mencapai pernyataan istirahat, lanjutkan atau kembalikan, klausa akhirnya akan dieksekusi tepat sebelum eksekusi pernyataan istirahat, lanjutkan atau kembalikan.

-Jika klausa akhirnya menyertakan pernyataan pengembalian, nilai yang dikembalikan akan menjadi salah satu dari pernyataan pengembalian klausa akhirnya, bukan nilai dari pernyataan pengembalian klausa try.

Misalnya:

    >>>def bool_return():
    ...    try:
    ...        return True
    ...    finally:
    ...        return False
    ...
    >>>bool_return()
    False
Contoh yang lebih rumit:

    >>>def divide(x, y):
    ...    try:
    ...        result = x / y
    ...    except ZeroDivisionError:
    ...        print("division by zero!")
    ...    else:
    ...        print("result is", result)
    ...    finally:
    ...        print("executing finally clause")
    ...
    >>>divide(2, 1)
    result is 2.0
    executing finally clause
    >>>divide(2, 0)
    division by zero!
    executing finally clause
    >>>divide("2", "1")
    executing finally clause
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 3, in divide
    TypeError: unsupported operand type(s) for /: 'str' and 'str'
Seperti yang Anda lihat, klausa akhirnya dijalankan dalam acara apa pun. TypeError yang dimunculkan dengan membagi dua string tidak ditangani oleh kecuali klausa dan oleh karena itu dimunculkan kembali setelah klausa akhirnya dieksekusi.

Dalam aplikasi dunia nyata, akhirnya klausa berguna untuk melepaskan sumber daya eksternal (seperti file atau koneksi jaringan), terlepas dari apakah penggunaan sumber berhasil.

***8.8. Predefined Clean-up Actions (Tindakan Pembersihan yang Telah Ditentukan)***

Beberapa objek menentukan tindakan pembersihan standar yang harus dilakukan saat objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Lihat contoh berikut, yang mencoba membuka file dan mencetak isinya ke layar.

    for line in open("myfile.txt"):
        print(line, end="")
Masalah dengan kode ini adalah membiarkan file terbuka untuk waktu yang tidak ditentukan setelah bagian kode ini selesai dijalankan. Ini bukan masalah dalam skrip sederhana, tetapi bisa menjadi masalah untuk aplikasi yang lebih besar. Dengan pernyataan memungkinkan objek seperti file untuk digunakan dengan cara yang memastikan mereka selalu dibersihkan dengan cepat dan benar.

    with open("myfile.txt") as f:
        for line in f:
            print(line, end="")
Setelah pernyataan dieksekusi, file f selalu ditutup, bahkan jika terjadi masalah saat memproses baris. Objek yang, seperti file, memberikan tindakan pembersihan yang telah ditentukan sebelumnya akan menunjukkan hal ini dalam dokumentasinya.

***8.9. Raising and Handling Multiple Unrelated Exceptions (Menaikkan dan Menangani Beberapa Pengecualian yang Tidak Terkait)***

Ada situasi di mana perlu melaporkan beberapa pengecualian yang telah terjadi. Ini sering terjadi dalam kerangka kerja konkurensi, ketika beberapa tugas mungkin gagal secara paralel, tetapi ada juga kasus penggunaan lain yang diinginkan untuk melanjutkan eksekusi dan mengumpulkan banyak kesalahan daripada memunculkan pengecualian pertama.

ExceptionGroup bawaan membungkus daftar instance pengecualian sehingga dapat dimunculkan bersama. Ini adalah pengecualian itu sendiri, sehingga dapat ditangkap seperti pengecualian lainnya.

    >>>def f():
    ...    excs = [OSError('error 1'), SystemError('error 2')]
    ...    raise ExceptionGroup('there were problems', excs)
    ...
    >>>f()
      + Exception Group Traceback (most recent call last):
      |   File "<stdin>", line 1, in <module>
      |   File "<stdin>", line 3, in f
      | ExceptionGroup: there were problems
      +-+---------------- 1 ----------------
        | OSError: error 1
        +---------------- 2 ----------------
        | SystemError: error 2
        +------------------------------------
    >>>try:
    ...    f()
    ...except Exception as e:
    ...    print(f'caught {type(e)}: e')
    ...
    caught <class 'ExceptionGroup'>: e
    >>>
Dengan menggunakan exception* sebagai ganti dari exception, kita hanya dapat menangani pengecualian dalam grup yang cocok dengan tipe tertentu secara selektif. Dalam contoh berikut, yang memperlihatkan grup pengecualian bersarang, setiap klausa exception* mengekstrak dari pengecualian grup dari jenis tertentu sambil membiarkan semua pengecualian lainnya menyebar ke klausa lain dan akhirnya dinaikkan kembali.

    >>>def f():
    ...    raise ExceptionGroup("group1",
    ...                         [OSError(1),
    ...                          SystemError(2),
    ...                          ExceptionGroup("group2",
    ...                                         [OSError(3), RecursionError(4)])])
    ...
    >>>try:
    ...    f()
    ...except* OSError as e:
    ...    print("There were OSErrors")
    ...except* SystemError as e:
    ...   print("There were SystemErrors")
    ...
    There were OSErrors
    There were SystemErrors
      + Exception Group Traceback (most recent call last):
      |   File "<stdin>", line 2, in <module>
      |   File "<stdin>", line 2, in f
      | ExceptionGroup: group1
      +-+---------------- 1 ----------------
        | ExceptionGroup: group2
        +-+---------------- 1 ----------------
          | RecursionError: 4
          +------------------------------------
    >>>
Perhatikan bahwa pengecualian yang bersarang di grup pengecualian harus berupa instance, bukan tipe. Ini karena dalam praktiknya, pengecualian biasanya adalah pengecualian yang telah dimunculkan dan ditangkap oleh program, dengan pola berikut:

    >>>excs = []
    ...for test in tests:
    ...    try:
    ...        test.run()
    ...    except Exception as e:
    ...        excs.append(e)
    ...
    >>>if excs:
    ...   raise ExceptionGroup("Test Failures", excs)
    ...
***8.10. Enriching Exceptions with Notes (Memperkaya Pengecualian dengan Catatan)***

Saat pengecualian dibuat untuk dimunculkan, biasanya diinisialisasi dengan informasi yang menjelaskan kesalahan yang terjadi. Ada kasus di mana berguna untuk menambahkan informasi setelah pengecualian tertangkap. Untuk tujuan ini, pengecualian memiliki metode add_note(note) yang menerima string dan menambahkannya ke daftar catatan pengecualian. Render traceback standar menyertakan semua catatan, sesuai urutan penambahannya, setelah pengecualian.

    >>>try:
    ...    raise TypeError('bad type')
    ...except Exception as e:
    ...    e.add_note('Add some information')
    ...    e.add_note('Add some more information')
    ...    raise
    ...
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
    TypeError: bad type
    Add some information
    Add some more information
    >>>
Misalnya, saat mengumpulkan pengecualian ke dalam grup pengecualian, kami mungkin ingin menambahkan informasi konteks untuk setiap kesalahan. Berikut ini setiap pengecualian dalam grup memiliki catatan yang menunjukkan kapan kesalahan ini terjadi.

    >>>def f():
    ...    raise OSError('operation failed')
    ...
    >>>excs = []
    >>>for i in range(3):
    ...    try:
    ...        f()
    ...    except Exception as e:
    ...        e.add_note(f'Happened in Iteration {i+1}')
    ...        excs.append(e)
    ...
    >>>raise ExceptionGroup('We have some problems', excs)
      + Exception Group Traceback (most recent call last):
      |   File "<stdin>", line 1, in <module>
      | ExceptionGroup: We have some problems (3 sub-exceptions)
      +-+---------------- 1 ----------------
        | Traceback (most recent call last):
        |   File "<stdin>", line 3, in <module>
        |   File "<stdin>", line 2, in f
        | OSError: operation failed
        | Happened in Iteration 1
        +---------------- 2 ----------------
        | Traceback (most recent call last):
        |   File "<stdin>", line 3, in <module>
        |   File "<stdin>", line 2, in f
        | OSError: operation failed
        | Happened in Iteration 2
        +---------------- 3 ----------------
        | Traceback (most recent call last):
        |   File "<stdin>", line 3, in <module>
        |   File "<stdin>", line 2, in f
        | OSError: operation failed
        | Happened in Iteration 3
        +------------------------------------
    >>>
