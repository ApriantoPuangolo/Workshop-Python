# BAB 4 
# More Control Flow Tools
Selain pernyataan while yang baru saja diperkenalkan, Python menggunakan pernyataan kontrol aliran biasa yang dikenal dari bahasa lain, dengan beberapa perubahan :

***4.1. if statement***

Mungkin jenis pernyataan yang paling terkenal adalah pernyataan if. Misalnya:

    >>> x = int(input("Please enter an integer: "))
    Please enter an integer: 42
    >>> if x < 0:
    ...     x = 0
    ...     print('Negative changed to zero')
    ... elif x == 0:
    ...     print('Zero')
    ... elif x == 1:
    ...     print('Single')
    ... else:
    ...     print('More')
    ...
    More
    
Kata kunci 'elif' merupakan kependekan dari 'else if', dan berguna untuk menghindari indentasi yang berlebihan. Urutan if … elif … elif … adalah pengganti untuk pernyataan sakelar atau kasus yang ditemukan dalam bahasa lain.

***4.2. for statement***

Pernyataan for di Python sedikit berbeda dari yang biasa Anda gunakan di C atau Pascal. Daripada selalu mengulangi perkembangan aritmatika angka (seperti di Pascal), atau memberi pengguna kemampuan untuk menentukan langkah iterasi dan menghentikan kondisi (sebagai C), pernyataan for Python mengulangi item dari urutan apa pun (daftar atau sebuah string), dalam urutan kemunculannya dalam urutan. Misalnya (tidak ada permainan kata-kata):

    >>> # Measure some strings:
    >>> words = ['cat', 'window', 'defenestrate']
    >>> for w in words:
    ...     print(w, len(w))
    ...
    cat 3
    window 6
    defenestrate 12
    
***4.3. The range() Function***

Jika Anda memang perlu mengulangi urutan angka, fungsi built-in range() sangat berguna. Ini menghasilkan progresi aritmatika:

    >>> for i in range(5):
    ...     print(i)
    ...
    0
    1
    2
    3
    4
    
Titik akhir yang diberikan tidak pernah menjadi bagian dari urutan yang dihasilkan; range(10) menghasilkan 10 nilai, indeks legal untuk item dengan urutan panjang 10. Dimungkinkan untuk membiarkan rentang dimulai dari angka lain, atau untuk menentukan kenaikan yang berbeda (bahkan negatif; terkadang ini disebut 'langkah') ):

    >>> list(range(5, 10))
    [5, 6, 7, 8, 9]
    >>> list(range(0, 10, 3))
    [0, 3, 6, 9]
    >>> list(range(-10, -100, -30))
    [-10, -40, -70]
    

Untuk mengulangi indeks urutan, Anda dapat menggabungkan range() dan len() sebagai berikut:

    >>> a = ['Mary', 'had', 'a', 'little', 'lamb']
    >>> for i in range(len(a)):
    ...     print(i, a[i])
    ...
    0 Mary
    1 had
    2 a
    3 little
    4 lamb
    
***4.4. break and continue Statements, and else Clauses on Loops***

Pernyataan break, seperti di C, keluar dari loop for atau while terlampir terdalam.

Pernyataan pengulangan mungkin memiliki klausa lain; itu dieksekusi ketika loop berakhir melalui kelelahan iterable (dengan for) atau ketika kondisi menjadi salah (dengan while), tetapi tidak ketika loop diakhiri dengan pernyataan break. Ini dicontohkan oleh loop berikut, yang mencari bilangan prima:

    >>> for n in range(2, 10):
    ...     for x in range(2, n):
    ...         if n % x == 0:
    ...             print(n, 'equals', x, '*', n//x)
    ...             break
    ...     else:
    ...         # loop fell through without finding a factor
    ...         print(n, 'is a prime number')
    ...
    2 is a prime number
    3 is a prime number
    4 equals 2 * 2
    5 is a prime number
    6 equals 2 * 3
    7 is a prime number
    8 equals 2 * 4
    9 equals 3 * 3
    
Ketika digunakan dengan perulangan, klausa else memiliki lebih banyak kesamaan dengan klausa else dari pernyataan try daripada dengan pernyataan if: klausa else dari pernyataan try berjalan ketika tidak ada pengecualian yang terjadi, dan klausa else dari sebuah loop berjalan ketika tidak ada break terjadi.

    >>> for num in range(2, 10):
    ...     if num % 2 == 0:
    ...         print("Found an even number", num)
    ...         continue
    ...     print("Found an odd number", num)
    ...
    Found an even number 2
    Found an odd number 3
    Found an even number 4
    Found an odd number 5
    Found an even number 6
    Found an odd number 7
    Found an even number 8
    Found an odd number 9
    
***4.5 Pass statement atau pernyataan mulus***

Pernyataan pass tidak melakukan apa-apa. Itu dapat digunakan ketika pernyataan diperlukan secara sintaksis tetapi program tidak memerlukan tindakan. Misalnya:

    >>> while True:
    ...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
    ...
    
untuk membuat kelas minimal :

    >>> class MyEmptyClass:
    ...     pass
    ...
    
***4.6. match statement***

Pernyataan kecocokan mengambil ekspresi dan membandingkan nilainya dengan pola berurutan yang diberikan sebagai satu atau beberapa blok kasus. Ini mirip dengan pernyataan switch di C, Java atau JavaScript (dan banyak bahasa lainnya), tetapi lebih mirip dengan pencocokan pola dalam bahasa seperti Rust atau Haskell. Hanya pola pertama yang cocok yang akan dieksekusi dan juga dapat mengekstrak komponen (elemen urutan atau atribut objek) dari nilai menjadi variabel.

Bentuk paling sederhana membandingkan nilai subjek terhadap satu atau lebih literal:

    def http_error(status):
        match status:
            case 400:
                return "Bad request"
            case 404:
                return "Not found"
            case 418:
                return "I'm a teapot"
            case _:
                return "Something's wrong with the internet"
                
Catat blok terakhir: "nama variabel" _ bertindak sebagai wildcard dan tidak pernah gagal untuk mencocokkan. Jika tidak ada case yang cocok, tidak ada cabang yang dieksekusi.Anda dapat menggabungkan beberapa literal dalam satu pola menggunakan | ("atau"):
                
    case 401 | 403 | 404:
        return "Not allowed"

Pola dapat terlihat seperti tugas membongkar, dan dapat digunakan untuk mengikat variabel:

    # point is an (x, y) tuple
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
            
***4.7. Defining Functions atau Mendefinisikan Fungsi***

Kita dapat membuat fungsi yang menulis deret Fibonacci ke batas arbitrer:

    >>> def fib(n):    # write Fibonacci series up to n
    ...     """Print a Fibonacci series up to n."""
    ...     a, b = 0, 1
    ...     while a < n:
    ...         print(a, end=' ')
    ...         a, b = b, a+b
    ...     print()
    ...
    >>> # Now call the function we just defined:
    >>> fib(2000)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
    
A function definition associates the function name with the function object in the current symbol table. The interpreter recognizes the object pointed to by that name as a user-defined function. Other names can also point to that same function object and can also be used to access the function:

    >>> fib
    <function fib at 0x000001E66F3CEB90>
    >>> f = fib
    >>> f(100)
    0 1 1 2 3 5 8 13 21 34 55 89
    
-Pernyataan kembali kembali dengan nilai dari suatu fungsi. kembali tanpa argumen ekspresi mengembalikan Tidak ada. Jatuh dari akhir fungsi juga mengembalikan Tidak ada.

-Pernyataan result.append(a) memanggil metode dari hasil objek daftar. Metode adalah fungsi yang 'milik' objek dan diberi nama obj.nama metode, di mana obj adalah beberapa objek (ini mungkin ekspresi), dan nama metode adalah nama metode yang ditentukan oleh tipe objek. Jenis yang berbeda menentukan metode yang berbeda. Metode dari jenis yang berbeda dapat memiliki nama yang sama tanpa menimbulkan ambiguitas. (Dimungkinkan untuk menentukan tipe dan metode objek Anda sendiri, menggunakan kelas, lihat Kelas) Metode append() yang ditampilkan dalam contoh didefinisikan untuk objek daftar; itu menambahkan elemen baru di akhir daftar. Dalam contoh ini sama dengan result = result + [a], tetapi lebih efisien.

***4.8. More on Defining Functions***
Dimungkinkan juga untuk mendefinisikan fungsi dengan sejumlah variabel argumen. Ada tiga bentuk yang bisa digabungkan.

***4.8.1. Default Argument Values***
Bentuk yang paling berguna adalah menentukan nilai default untuk satu atau beberapa argumen. Ini menciptakan fungsi yang dapat dipanggil dengan lebih sedikit argumen daripada yang diizinkan. Misalnya:

    def ask_ok(prompt, retries=4, reminder='Please try again!'):
        while True:
            ok = input(prompt)
            if ok in ('y', 'ye', 'yes'):
                return True
            if ok in ('n', 'no', 'nop', 'nope'):
                return False
            retries = retries - 1
            if retries < 0:
                raise ValueError('invalid user response')
            print(reminder)
            
Fungsi ini dapat dipanggil dengan beberapa cara:

-hanya memberikan argumen wajib: ask_ok('Apakah Anda benar-benar ingin berhenti?')

-memberikan salah satu argumen opsional: ask_ok('OK untuk menimpa file?', 2)

-atau bahkan memberikan semua argumen: ask_ok('OK untuk menimpa file?', 2, 'Ayolah, hanya ya atau tidak!')
