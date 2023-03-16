BAB 1
Python
Python adalah bahasa yang ditafsirkan, yang dapat menghemat banyak waktu Anda selama pengembangan program karena tidak diperlukan kompilasi dan penautan. Penerjemah dapat digunakan secara interaktif, yang membuatnya mudah untuk bereksperimen dengan fitur bahasa, menulis program sekali pakai, atau menguji fungsi selama pengembangan program dari bawah ke atas. Ini juga merupakan kalkulator meja yang berguna.
Python memungkinkan program ditulis dengan kompak dan mudah dibaca. Program yang ditulis dengan Python biasanya jauh lebih pendek daripada program C, C++, atau Java yang setara, karena beberapa alasan:

-tipe data tingkat tinggi memungkinkan Anda mengekspresikan operasi kompleks dalam satu pernyataan;

-pengelompokan pernyataan dilakukan dengan lekukan alih-alih tanda kurung awal dan akhir;

-tidak diperlukan deklarasi variabel atau argumen.
Python dapat diperluas: jika Anda tahu cara memprogram dalam C, mudah untuk menambahkan fungsi atau modul bawaan baru ke juru bahasa, baik untuk melakukan operasi kritis dengan kecepatan maksimum, atau untuk menautkan program Python ke pustaka yang mungkin hanya tersedia dalam bentuk biner (seperti perpustakaan grafis khusus vendor). Setelah Anda benar-benar ketagihan, Anda dapat menautkan juru bahasa Python ke aplikasi yang ditulis dalam C dan menggunakannya sebagai ekstensi atau bahasa perintah untuk aplikasi itu.

BAB 2
Interactive Mode
Ketika perintah dibaca dari tty, interpreter dikatakan dalam mode interaktif. Dalam mode ini ia meminta perintah berikutnya dengan prompt utama, biasanya tiga tanda lebih besar dari (>>>); untuk baris lanjutan diminta dengan prompt sekunder, secara default tiga titik (...). Penerjemah mencetak pesan selamat datang yang menyatakan nomor versinya dan pemberitahuan hak cipta sebelum mencetak permintaan pertama:

(base) C:\Windows\System32>python
Python 3.10.9 | packaged by conda-forge | (main, Jan 11 2023, 15:15:40) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!

BAB 3
Using Python as a Calculator 

Numbers :
Penerjemah bertindak sebagai kalkulator sederhana: Anda dapat mengetikkan ekspresi dan itu akan menulis nilainya. Sintaks ekspresi langsung: operator +, -, * dan / berfungsi seperti kebanyakan bahasa lain (misalnya, Pascal atau C); tanda kurung (()) dapat digunakan untuk pengelompokan. Misalnya:
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # floored quotient * divisor + remainder
17
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
>>> width = 20
>>> height = 5 * 9
>>> width * height
900

String :
Selain angka, Python juga bisa memanipulasi string, yang bisa diekspresikan dalam beberapa cara. Mereka dapat diapit dengan tanda kutip tunggal ('...') atau tanda kutip ganda ("...") dengan hasil yang sama 2. \ dapat digunakan untuk menghindari tanda kutip:
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>>
KeyboardInterrupt
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), \n is included in the output
'First line.\nSecond line.'
>>> print(s)  # with print(), \n produces a new line
First line.
Second line.

Lists :
Python mengetahui sejumlah tipe data majemuk, yang digunakan untuk mengelompokkan nilai lain. Yang paling serbaguna adalah daftar, yang dapat ditulis sebagai daftar nilai (item) yang dipisahkan koma di antara tanda kurung siku. Daftar mungkin berisi item dari tipe yang berbeda, tetapi biasanya semua item memiliki tipe yang sama.
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
>>> # Fibonacci series:
>>> # the sum of two elements defines the next
    a, b = 0, 1
    while a < 10:
    print(a)
  File "<stdin>", line 2
    print(a)
    ^
IndentationError: expected an indented block after 'while' statement on line 1
    while a < 10:
         print(a)
         a, b = b, a+b

0
1
1
2
3
5
8
   i = 256*256
     print('The value of i is', i)
The value of i is 65536
     a, b = 0, 1
while a < 1000:
     print(a, end=',')
     a, b = b, a+b

0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

