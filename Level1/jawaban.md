# Penjelasan Jawaban

Algoritma yang saya gunakan untuk menghitung huruf yang sama di dalam sebuah string yang diberikan adalah dengan mengecek satu huruf dengan huruf di depannya. Pada fungsi yang saya telah buat, hal pertama yang saya lakukan adalah meng-assign variabel output agar memiliki nilai 0. Variabel output dimasukkan nilai 0 agar kita dapat menambahkan variabel tersebut dengan nilai satu setiap kita menemui character yang sama dan bersebelahan di dalam string.

Kemudian, perulangan diperlukan untuk melakukan pengecekan di string tersebut. Pada perulangan, kondisi yang saya gunakan adalah range(len(inputString) - 1) yang akan membuat set angka sebanyak panjang dari string tersebut dikurangi dengan nilai satu. Pengurangan tersebut perlu dilakukan karena kita akan melakukan pengecekan suatu character dengan character di depannya. Artinya, kita melakukan pengecekan dengan satu indeks di depan indeks yang akan dicek. Jadi, kondisi perulangan di atas berguna untuk mengantisipasi agar tidak terjadi error string index out of range.

Pada setiap perulangan, kita melakukan pengecekan huruf yang memiliki index i dengan index di depannya. Apabila huruf yang memiliki index i dengan huruf di depannya sama, nilai output akan bertambah satu. Setelah perulangan selesai, nilai output akan dikembalikan.

Sekian penjelasan dari fungsi untuk mengetahui jumlah minimum huruf yang dihapus agar tidak terdapat huruf yang sama saling bersebelahan. Terima kasih. Mohon maaf apabila terdapat kesalahan.