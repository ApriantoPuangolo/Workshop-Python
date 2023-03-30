# Bab 5
# Data Structures (Struktur Data)
# Lists
Tipe data daftar memiliki beberapa metode lagi. Berikut ini semua metode objek daftar:

***list.append(x)***

Tambahkan item ke akhir daftar. Setara dengan a[len(a):] = [x].

***list.extend(iterable)***

Perpanjang daftar dengan menambahkan semua item dari iterable. Setara dengan a[len(a):] = iterable.

***list.insert(i, x)***

Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen sebelum disisipkan, jadi a.insert(0, x) menyisipkan di depan daftar, dan a.insert(len(a), x) setara dengan a.append( X).

***list.remove(x)***

Hapus item pertama dari daftar yang nilainya sama dengan x. Itu memunculkan ValueError jika tidak ada item seperti itu.

***list.pop([i])***

Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop() menghapus dan mengembalikan item terakhir dalam daftar. (Kurung siku di sekitar i pada tanda tangan metode menunjukkan bahwa parameternya opsional, bukan berarti Anda harus mengetikkan tanda kurung siku pada posisi itu. Anda akan sering melihat notasi ini di Referensi Pustaka Python.) dan lain-lain.

Contoh yang menggunakan sebagian besar metode daftar:

    >>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    >>> fruits.count('apple')
    2
    >>>fruits.count('tangerine')
    0
    >>>fruits.index('banana')
    3
    >>>fruits.index('banana', 4)  # Find next banana starting at position 4
    6
    >>>fruits.reverse()
    >>>fruits
    ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
    >>>fruits.append('grape')
    >>>fruits
    ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
    >>>fruits.sort()
    >>>fruits
    ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
    >>>fruits.pop()
    'pear'

Anda mungkin telah memperhatikan bahwa metode seperti menyisipkan, menghapus, atau mengurutkan yang hanya mengubah daftar tidak memiliki nilai kembalian yang dicetak – mereka mengembalikan default Tidak ada. 1 Ini adalah prinsip desain untuk semua struktur data yang bisa berubah di Python.

# Using Lists as Stacks (Menggunakan Daftar sebagai Tumpukan)
Metode daftar membuatnya sangat mudah untuk menggunakan daftar sebagai tumpukan, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil (“last-in, first-out”). Untuk menambahkan item ke bagian atas tumpukan, gunakan append(). Untuk mengambil item dari atas tumpukan, gunakan pop() tanpa indeks eksplisit. Misalnya:

    >>>stack = [3, 4, 5]
    >>>stack.append(6)
    >>>stack.append(7)
    >>>stack
    [3, 4, 5, 6, 7]
    >>>stack.pop()
    7
    >>>stack
    [3, 4, 5, 6]
    >>>stack.pop()
    6
    >>>stack.pop()
    5
    stack
    [3, 4]
# Using Lists as Queues (Menggunakan Daftar sebagai Antrian)
Dimungkinkan juga untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil (“first-in, first-out”); namun, daftar tidak efisien untuk tujuan ini. Sementara menambahkan dan muncul dari akhir daftar cepat, melakukan sisipan atau muncul dari awal daftar lambat (karena semua elemen lain harus digeser satu).

Untuk mengimplementasikan antrean, gunakan collections.deque yang dirancang untuk menambahkan dan muncul dengan cepat dari kedua ujungnya. Misalnya:

    >>>from collections import deque
    >>>queue = deque(["Eric", "John", "Michael"])
    >>>queue.append("Terry")           # Terry arrives
    >>>queue.append("Graham")          # Graham arrives
    >>>queue.popleft()                 # The first to arrive now leaves
    'Eric'
    >>>queue.popleft()                 # The second to arrive now leaves
    'John'
    >>>queue                           # Remaining queue in order of arrival
    deque(['Michael', 'Terry', 'Graham'])
# List Comprehensions (Daftar Pemahaman)
Pemahaman daftar menyediakan cara ringkas untuk membuat daftar. Aplikasi umum adalah membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota urutan lain atau iterable, atau untuk membuat urutan elemen yang memenuhi kondisi tertentu.

Sebagai contoh, misalkan kita ingin membuat daftar kotak, seperti:

    >>> squares = []
    >>>for x in range(10):
    ...    squares.append(x**2)
    ...
    >>>squares
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Nested List Comprehensions (Pemahaman Daftar Bersarang)
Ekspresi awal dalam pemahaman daftar dapat berupa sembarang ekspresi, termasuk pemahaman daftar lainnya.

Pertimbangkan contoh matriks 3x4 berikut yang diimplementasikan sebagai daftar 3 daftar dengan panjang 4:

    >>>matrix = [
    ...    [1, 2, 3, 4],
    ...    [5, 6, 7, 8],
    ...    [9, 10, 11, 12],
    ...]
# The del statement (Pernyataan del)
Ada cara untuk menghapus item dari daftar yang diberikan indeksnya alih-alih nilainya: pernyataan del. Ini berbeda dari metode pop() yang mengembalikan nilai. Pernyataan del juga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar (yang kita lakukan sebelumnya dengan menugaskan daftar kosong ke irisan). Misalnya:

    >>>a = [-1, 1, 66.25, 333, 333, 1234.5]
    >>>del a[0]
    >>>a
    [1, 66.25, 333, 333, 1234.5]
    >>>del a[2:4]
    >>>a
    [1, 66.25, 1234.5]
    >>>del a[:]
    >>>a
    []
# Tuples and Sequences (Tuple dan Urutan)
Kami melihat bahwa daftar dan string memiliki banyak properti umum, seperti operasi pengindeksan dan pemotongan. Mereka adalah dua contoh tipe data urutan (lihat Jenis Urutan - daftar, tupel, rentang). Karena Python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lainnya: tuple.

Sebuah tuple terdiri dari sejumlah nilai yang dipisahkan dengan koma, misalnya:

    >>>t = 12345, 54321, 'hello!'
    >>>t[0]
    12345
    >>>t
    (12345, 54321, 'hello!')
    >>># Tuples may be nested:
    ...u = t, (1, 2, 3, 4, 5)
    >>>u
    ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
    >>># Tuples are immutable:
    ...t[0] = 88888
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment
    >>># but they can contain mutable objects:
    ...v = ([1, 2, 3], [3, 2, 1])
    >>>v
    ([1, 2, 3], [3, 2, 1])
# Sets (Set)
Python juga menyertakan tipe data untuk set. Himpunan adalah koleksi tak terurut tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Set objek juga mendukung operasi matematika seperti penyatuan, persimpangan, perbedaan, dan perbedaan simetris.

Kurung kurawal atau fungsi set() dapat digunakan untuk membuat set. Catatan: untuk membuat set kosong Anda harus menggunakan set(), bukan {}; yang terakhir membuat kamus kosong, struktur data yang akan kita bahas di bagian selanjutnya.

Berikut demonstrasi singkatnya:

    >>>basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    >>>print(basket)                      # show that duplicates have been removed
    {'orange', 'banana', 'pear', 'apple'}
    >>>'orange' in basket                 # fast membership testing
    True
    >>>'crabgrass' in basket
    False

    >>># Demonstrate set operations on unique letters from two words
    ...
    >>>a = set('abracadabra')
    >>>b = set('alacazam')
    >>>a                                  # unique letters in a
    {'a', 'r', 'b', 'c', 'd'}
    >>>a - b                              # letters in a but not in b
    {'r', 'd', 'b'}
    >>>a | b                              # letters in a or b or both
    {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
    >>>a & b                              # letters in both a and b
    {'a', 'c'}
    >>>a ^ b                              # letters in a or b but not both
    {'r', 'd', 'b', 'm', 'z', 'l'}
# Dictionaries (Kamus)
Tipe data berguna lainnya yang dibangun ke dalam Python adalah kamus (lihat Jenis Pemetaan — dict). Kamus terkadang ditemukan dalam bahasa lain sebagai "memori asosiatif" atau "array asosiatif". Tidak seperti urutan, yang diindeks oleh rentang angka, kamus diindeks oleh kunci, yang dapat berupa tipe apa pun yang tidak dapat diubah; string dan angka selalu bisa menjadi kunci. Tupel dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tupel; jika tuple berisi objek yang dapat diubah baik secara langsung maupun tidak langsung, itu tidak dapat digunakan sebagai kunci. Anda tidak dapat menggunakan daftar sebagai kunci, karena daftar dapat dimodifikasi menggunakan penetapan indeks, penetapan irisan, atau metode seperti append() dan extend().

Berikut adalah contoh kecil menggunakan kamus:

    >>>tel = {'jack': 4098, 'sape': 4139}
    >>>tel['guido'] = 4127
    >>>tel
    {'jack': 4098, 'sape': 4139, 'guido': 4127}
    >>>tel['jack']
    4098
    >>>del tel['sape']
    >>>tel['irv'] = 4127
    >>>tel
    {'jack': 4098, 'guido': 4127, 'irv': 4127}
    >>>list(tel)
    ['jack', 'guido', 'irv']
    >>>sorted(tel)
    ['guido', 'irv', 'jack']
    >>>'guido' in tel
    True
    >>>'jack' not in tel
    False
# Looping Techniques (Teknik Looping)
Saat mengulang melalui kamus, kunci dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan metode items() .

    >>>knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    >>>for k, v in knights.items():
    ...    print(k, v)
    ...
    gallahad the pure
    robin the brave
# More on Conditions
Kondisi yang digunakan dalam pernyataan while dan if dapat berisi operator apa saja, bukan hanya perbandingan.

Operator pembanding in dan not in adalah uji keanggotaan yang menentukan apakah suatu nilai ada di dalam (atau tidak di dalam) wadah. Operator adalah dan tidak membandingkan apakah dua objek benar-benar objek yang sama. Semua operator pembanding memiliki prioritas yang sama, yang lebih rendah dari semua operator numerik.

Perbandingan dapat dirantai. Misalnya, a < b == c menguji apakah a kurang dari b dan terlebih lagi b sama dengan c.

Perbandingan dapat digabungkan menggunakan operator Boolean dan dan atau, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat ditiadakan dengan not. Ini memiliki prioritas lebih rendah daripada operator pembanding; di antara mereka, tidak memiliki prioritas tertinggi dan atau terendah, sehingga A dan bukan B atau C setara dengan (A dan (bukan B)) atau C. Seperti biasa, tanda kurung dapat digunakan untuk menyatakan komposisi yang diinginkan.

Operator Boolean dan dan atau disebut operator hubung singkat: argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika A dan C benar tetapi B salah, A dan B dan C tidak mengevaluasi ekspresi C. Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai kembalian dari operator hubung singkat adalah yang terakhir argumen yang dievaluasi.

Dimungkinkan untuk menetapkan hasil perbandingan atau ekspresi Boolean lainnya ke variabel. Misalnya :

    >>>string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
    >>>non_null = string1 or string2 or string3
    >>>non_null
    'Trondheim'
# Comparing Sequences and Other Types (Membandingkan Urutan dan Jenis Lainnya)
Objek urutan biasanya dapat dibandingkan dengan objek lain dengan tipe urutan yang sama. Perbandingannya menggunakan urutan leksikografis: pertama dua item pertama dibandingkan, dan jika berbeda, ini menentukan hasil perbandingan; jika sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu urutannya habis. Jika dua item yang akan dibandingkan itu sendiri adalah urutan dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif. Jika semua item dari dua urutan sebanding, urutannya dianggap sama. Jika satu urutan adalah sub-urutan awal dari yang lain, urutan yang lebih pendek adalah yang lebih kecil (lebih kecil). Pengurutan leksikografis untuk string menggunakan nomor poin kode Unicode untuk mengurutkan karakter individual. Beberapa contoh perbandingan antar barisan yang sejenis:

    (1, 2, 3)              < (1, 2, 4)
    [1, 2, 3]              < [1, 2, 4]
    'ABC' < 'C' < 'Pascal' < 'Python'
    (1, 2, 3, 4)           < (1, 2, 4)
    (1, 2)                 < (1, 2, -1)
    (1, 2, 3)             == (1.0, 2.0, 3.0)
    (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
