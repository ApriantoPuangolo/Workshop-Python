# 9. Classes (Kelas)
Kelas menyediakan sarana bundling data dan fungsionalitas bersama. Membuat kelas baru akan membuat tipe objek baru, yang memungkinkan instance baru dari tipe tersebut dibuat. Setiap instance kelas dapat memiliki atribut yang melekat padanya untuk mempertahankan statusnya. Instance kelas juga dapat memiliki metode (ditentukan oleh kelasnya) untuk memodifikasi statusnya.

Dibandingkan dengan bahasa pemrograman lain, mekanisme kelas Python menambahkan kelas dengan sintaks dan semantik baru yang minimal. Ini adalah campuran dari mekanisme kelas yang ditemukan di C++ dan Modula-3. Kelas Python menyediakan semua fitur standar Pemrograman Berorientasi Objek: mekanisme pewarisan kelas memungkinkan banyak kelas dasar, kelas turunan dapat mengganti metode apa pun dari kelas atau kelas dasarnya, dan metode dapat memanggil metode kelas dasar dengan nama yang sama . Objek dapat berisi jumlah dan jenis data yang sewenang-wenang. Seperti halnya modul, kelas mengambil bagian dari sifat dinamis Python: mereka dibuat saat runtime, dan dapat dimodifikasi lebih lanjut setelah dibuat.

Dalam terminologi C++, biasanya anggota kelas (termasuk anggota data) bersifat publik (kecuali lihat di bawah Variabel Pribadi), dan semua fungsi anggota bersifat virtual. Seperti di Modula-3, tidak ada singkatan untuk mereferensikan anggota objek dari metodenya: fungsi metode dideklarasikan dengan argumen pertama eksplisit yang mewakili objek, yang disediakan secara implisit oleh panggilan. Seperti di Smalltalk, kelas itu sendiri adalah objek. Ini menyediakan semantik untuk mengimpor dan mengganti nama. Tidak seperti C++ dan Modula-3, tipe bawaan dapat digunakan sebagai kelas dasar untuk ekstensi oleh pengguna. Juga, seperti di C++, sebagian besar operator bawaan dengan sintaks khusus (operator aritmatika, subskrip, dll.) dapat didefinisikan ulang untuk instance kelas.

(Kurangnya terminologi yang diterima secara universal untuk berbicara tentang kelas, saya akan sesekali menggunakan istilah Smalltalk dan C++. Saya akan menggunakan istilah Modula-3, karena semantik berorientasi objeknya lebih dekat dengan Python daripada C++, tetapi saya berharap bahwa beberapa pembaca pernah mendengarnya.)

***9.1. A Word About Names and Objects (Sebuah Kata Tentang Nama dan Objek)***

Objek memiliki individualitas, dan banyak nama (dalam berbagai cakupan) dapat terikat ke objek yang sama. Ini dikenal sebagai aliasing dalam bahasa lain. Ini biasanya tidak dihargai pada pandangan pertama di Python, dan dapat diabaikan dengan aman ketika berhadapan dengan tipe dasar yang tidak dapat diubah (angka, string, tupel). Namun, aliasing mungkin memiliki efek yang mengejutkan pada semantik kode Python yang melibatkan objek yang dapat diubah seperti daftar, kamus, dan sebagian besar jenis lainnya. Ini biasanya digunakan untuk kepentingan program, karena alias berperilaku seperti penunjuk dalam beberapa hal. Misalnya, melewatkan objek itu murah karena hanya sebuah pointer yang dilewatkan oleh implementasi; dan jika sebuah fungsi memodifikasi objek yang diteruskan sebagai argumen, pemanggil akan melihat perubahannya — ini menghilangkan kebutuhan akan dua mekanisme penerusan argumen yang berbeda seperti di Pascal.

***9.2. Python Scopes and Namespaces (Lingkup dan Ruang Nama Python)***

Sebelum memperkenalkan kelas, pertama-tama saya harus memberi tahu Anda sesuatu tentang aturan ruang lingkup Python. Definisi kelas memainkan beberapa trik rapi dengan ruang nama, dan Anda perlu mengetahui cara kerja ruang lingkup dan ruang nama untuk memahami sepenuhnya apa yang terjadi. Kebetulan, pengetahuan tentang subjek ini berguna untuk semua programmer Python tingkat lanjut.

Mari kita mulai dengan beberapa definisi.

Namespace adalah pemetaan dari nama ke objek. Sebagian besar ruang nama saat ini diimplementasikan sebagai kamus Python, tetapi biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan mungkin berubah di masa mendatang. Contoh ruang nama adalah: kumpulan nama bawaan (berisi fungsi seperti abs(), dan nama pengecualian bawaan); nama global dalam modul; dan nama lokal dalam pemanggilan fungsi. Dalam arti himpunan atribut suatu objek juga membentuk namespace. Hal penting yang harus diketahui tentang ruang nama adalah sama sekali tidak ada hubungan antara nama di ruang nama yang berbeda; misalnya, dua modul berbeda dapat menentukan fungsi maksimalkan tanpa kebingungan — pengguna modul harus mengawalinya dengan nama modul.

Omong-omong, saya menggunakan atribut kata untuk nama apa pun yang mengikuti titik — misalnya, dalam ekspresi z.real, real adalah atribut dari objek z. Sebenarnya, referensi ke nama dalam modul adalah referensi atribut: dalam ekspresi modname.funcname, modname adalah objek modul dan funcname adalah atributnya. Dalam hal ini terjadi pemetaan langsung antara atribut modul dan nama global yang ditentukan dalam modul: mereka berbagi namespace yang sama! 1

Atribut dapat berupa read-only atau writable. Dalam kasus terakhir, penugasan ke atribut dimungkinkan. Atribut modul dapat ditulis: Anda dapat menulis modname.the_answer = 42. Atribut yang dapat ditulis juga dapat dihapus dengan pernyataan del. Misalnya, del modname.the_answer akan menghapus atribut the_answer dari objek yang diberi nama modname.

Ruang nama dibuat pada momen yang berbeda dan memiliki masa hidup yang berbeda. Ruang nama yang berisi nama bawaan dibuat saat juru bahasa Python dijalankan, dan tidak pernah dihapus. Ruang nama global untuk modul dibuat saat definisi modul dibaca; biasanya, ruang nama modul juga bertahan hingga juru bahasa berhenti. Pernyataan yang dieksekusi oleh pemanggilan tingkat atas dari juru bahasa, baik dibaca dari file skrip atau secara interaktif, dianggap sebagai bagian dari modul bernama __main__, sehingga mereka memiliki namespace globalnya sendiri. (Nama bawaan sebenarnya juga hidup dalam modul; ini disebut builtin.)

***9.2.1. Scopes and Namespaces Example(Contoh Ruang Lingkup dan Namespace)***

Ini adalah contoh yang mendemonstrasikan cara mereferensikan cakupan dan ruang nama yang berbeda, dan bagaimana pengaruh global dan nonlokal terhadap pengikatan variabel:

    def scope_test():
        def do_local():
            spam = "local spam"

        def do_nonlocal():
            nonlocal spam
            spam = "nonlocal spam"

        def do_global():
            global spam
            spam = "global spam"

        spam = "test spam"
        do_local()
        print("After local assignment:", spam)
        do_nonlocal()
        print("After nonlocal assignment:", spam)
        do_global()
        print("After global assignment:", spam)

    scope_test()
    print("In global scope:", spam)
Output dari kode contoh adalah:

***9.3.1. Class Definition Syntax(Sintaks Definisi Kelas)***

Bentuk paling sederhana dari definisi kelas terlihat seperti ini:

    class ClassName:
        <statement-1>
        .
        .
        .
        <statement-N>
Definisi kelas, seperti definisi fungsi (pernyataan def) harus dijalankan sebelum memiliki efek apa pun. (Anda dapat menempatkan definisi kelas di cabang pernyataan if, atau di dalam fungsi.)

Dalam praktiknya, pernyataan di dalam definisi kelas biasanya berupa definisi fungsi, tetapi pernyataan lain diperbolehkan, dan terkadang berguna — kita akan membahasnya lagi nanti. Definisi fungsi di dalam kelas biasanya memiliki bentuk daftar argumen yang khas, ditentukan oleh konvensi pemanggilan metode — sekali lagi, ini akan dijelaskan nanti.

Saat definisi kelas dimasukkan, namespace baru dibuat, dan digunakan sebagai cakupan lokal — jadi, semua penugasan ke variabel lokal masuk ke namespace baru ini. Secara khusus, definisi fungsi mengikat nama fungsi baru di sini.

Ketika definisi kelas dibiarkan normal (melalui akhir), objek kelas dibuat. Ini pada dasarnya adalah pembungkus isi namespace yang dibuat oleh definisi kelas; kita akan mempelajari lebih lanjut tentang objek kelas di bagian selanjutnya. Lingkup lokal asli (yang berlaku tepat sebelum definisi kelas dimasukkan) dipulihkan, dan objek kelas terikat di sini dengan nama kelas yang diberikan dalam header definisi kelas (ClassName dalam contoh).

***9.3.2. Class Objects(Objek Kelas)***

Objek kelas mendukung dua jenis operasi: referensi atribut dan instantiasi.

Referensi atribut menggunakan sintaks standar yang digunakan untuk semua referensi atribut di Python: obj.name. Nama atribut yang valid adalah semua nama yang ada di ruang nama kelas saat objek kelas dibuat. Jadi, jika definisi kelas terlihat seperti ini:

    class MyClass:
        """A simple example class"""
        i = 12345

        def f(self):
            return 'hello world'
maka MyClass.i dan MyClass.f adalah referensi atribut yang valid, masing-masing mengembalikan bilangan bulat dan objek fungsi. Atribut kelas juga dapat ditetapkan, sehingga Anda dapat mengubah nilai MyClass.i berdasarkan penetapan. __doc__ juga merupakan atribut yang valid, mengembalikan docstring milik kelas: "A simple example class".

Instansiasi kelas menggunakan notasi fungsi. Anggap saja objek kelas adalah fungsi tanpa parameter yang mengembalikan instance baru dari kelas. Misalnya (dengan asumsi kelas di atas):

    x = MyClass()
membuat instance baru dari kelas dan menugaskan objek ini ke variabel lokal x.

Operasi instantiasi ("memanggil" objek kelas) membuat objek kosong. Banyak kelas suka membuat objek dengan instance yang disesuaikan dengan keadaan awal tertentu. Oleh karena itu kelas dapat mendefinisikan metode khusus bernama __init__(), seperti ini:

***9.3.5. Class and Instance Variables(Variabel Kelas dan Instance)***

Secara umum, variabel instan untuk data unik untuk setiap instans dan variabel kelas untuk atribut dan metode yang digunakan bersama oleh semua instans kelas:

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'

Seperti yang dibahas dalam A Word About Names and Objects, data yang dibagikan mungkin memiliki efek mengejutkan dengan melibatkan objek yang dapat berubah seperti daftar dan kamus. Misalnya, daftar trik dalam kode berikut tidak boleh digunakan sebagai variabel kelas karena hanya satu daftar yang akan digunakan bersama oleh semua instance Anjing:

class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']

Desain kelas yang benar harus menggunakan variabel instan sebagai gantinya:

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']

***9.4. Random Remarks (Keterangan Acak)***


Jika nama atribut yang sama muncul di kedua instance dan di kelas, maka pencarian atribut akan memprioritaskan instance tersebut:

>>>class Warehouse:
...   purpose = 'storage'
...   region = 'west'
...
>>>w1 = Warehouse()
>>>print(w1.purpose, w1.region)
storage west
>>>w2 = Warehouse()
>>>w2.region = 'east'
>>>print(w2.purpose, w2.region)
storage east

Atribut data dapat direferensikan oleh metode maupun oleh pengguna biasa ("klien") dari suatu objek. Dengan kata lain, kelas tidak dapat digunakan untuk mengimplementasikan tipe data abstrak murni. Nyatanya, tidak ada apa pun dalam Python yang memungkinkan untuk memaksakan penyembunyian data — semuanya didasarkan pada konvensi. (Di sisi lain, implementasi Python, yang ditulis dalam C, dapat sepenuhnya menyembunyikan detail implementasi dan mengontrol akses ke objek jika perlu; ini dapat digunakan oleh ekstensi ke Python yang ditulis dalam C.)


Klien harus menggunakan atribut data dengan hati-hati — klien dapat mengacaukan invarian yang dikelola oleh metode dengan menandai atribut data mereka. Perhatikan bahwa klien dapat menambahkan atribut datanya sendiri ke objek instan tanpa memengaruhi validitas metode, selama konflik nama dihindari — sekali lagi, konvensi penamaan dapat menghemat banyak kerumitan di sini.


Tidak ada singkatan untuk mereferensikan atribut data (atau metode lain!) dari dalam metode. Saya menemukan bahwa ini benar-benar meningkatkan keterbacaan metode: tidak ada kemungkinan membingungkan variabel lokal dan variabel instan ketika melihat sekilas melalui metode.


Seringkali, argumen pertama dari sebuah metode disebut self. Ini tidak lebih dari sebuah konvensi: nama self sama sekali tidak memiliki arti khusus untuk Python. Perhatikan, bagaimanapun, bahwa dengan tidak mengikuti konvensi, kode Anda mungkin kurang dapat dibaca oleh programmer Python lainnya, dan juga dapat dibayangkan bahwa program browser kelas dapat ditulis yang bergantung pada konvensi semacam itu.
