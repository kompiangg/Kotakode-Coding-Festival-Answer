# Penjelasan Jawaban

Pertama, saya deklarasikan variabel dengan nama `subset_list` yang berguna untuk menyimpan semua subset yang mungkin (**termasuk subset yang bersebelahan**). Kemudian, karena pada catatan diberitahukan apabila semua elemen di dalam list adalah negatif maka fungsi akan mengembalikan nilai 0. Berdasarkan pada catatan tersebut, saya membuat sebuah kondisi apabila jumlah dari semua elemen tersebut dijumlahkan dengan jumlah dari mutlak semua elemen sama dengan nol, fungsi akan mengembalikan nilai 0. Saya membuat kondisinya seperti itu karena, apabila semua bilangan negatif maka hasil penjumlahan dari jumlah semua bilangan tersebut dengan mutlak dari jumlah semua bilangan tersebut adalah 0.

Contoh : `(-1 + -2 + -3 + -4) + |(-1 + -2 + -3 + -4)| = -10 + |-10| = -10 + 10 = 0`

Setelah itu, terdapat perulangan untuk menyimpan semua subset yang mungkin (**termasuk subset yang bersebelahan**). Seteleh perulangan ini, variabel `subset_list` sudah menyimpan semua subset yang mungkin. Namun, karena instruksinya menyebutkan bahwa tidak boleh menyertakan subset yang pada urutan elemennya bersebelahan, kita akan menghapus subset tersebut pada perulangan berikutnya.

Saya mendeklarasikan variabel `length_subset` yang mempunyai nilai yang sama dengan `len(subset_list)`, hal tersebut saya lakukan karena ketika kita menghapus elemen di dalam list, panjang dari `subset_list` akan berubah. Namun, apabila saya menggunakan perulangan `for`, saya tidak dapat mengubah nilai dari panjang elemen tersebut. Oleh karena itu, saya menggunakan perulangan `while` dan membuat variabel baru yang menyimpan panjang dari variabel `subset_list`.

Selanjutnya, perulangan yang berguna untuk menghapus subset yang urutan awalnya bersebelahan. Dalam perulangan tersebut saya melakukan penyeleksian kepada elemen yang akan dihapus dengan kondisi

```python
if abs(inputList.index(subset_list[i][j]) - inputList.index(subset_list[i][j - 1])) == 1 :
```
Jadi, ketika kita mencari index dari nilai elemen tersebut di dalam variabel list awal (`inputList`) dan kita mengurangkannya dengan index dari nilai elemen sebelumnya, apabila hasil pengurangan tersebut sama dengan 1 itu artinya pada awalnya, elemen-elemen tersebut memiliki urutan yang bersebelahan. Lalu, kita dapat menghapus elemen tersebut menggunakan method `.pop()` dengan argumen yaitu nilai dari variabel `i` saat itu

Setelah kita menghilangkan subset yang tidak diinginkan. Selanjutnya, kita akan melakukan komparasi dari penjumlahan pada setiap subset dengan menggunakan perulangan. Hasil dari perulangan tersebut adalah nilai dari variabel `output`, yang awalnya adalah 0, akan menyimpan nilai dari penjumlahan terbesar dari salah satu subset yang ada di list tersebut