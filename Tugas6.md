Diandita Wira Puspita
1144028
D4 Teknik Informatika 3C
Politeknik Pos Indonesia

Theorema Bayes
Dalam Kasus Diagnosa Penyakit Paru-Paru

Sistem pakar adalah cabang kecerdasan buatan yang menggunakan pengetahuan/ knowledge khusus untuk memecahkan masalah pada level human expert/pakar. Salah satu penerapan sistem pakar dalam bidang kedokteran adalah untuk melakukan diagnosa penyakit. Pada penelitian ini dilakukan perancangan dan pembuatan sistem pakar yang digunakan untuk membantu menentukan diagnosa suatu penyakit yang diawali dari gejala utama penyakit paru-paru serta menentukan saran terapi yang harus diberikan. Masalah ketidakpastian pengetahuan dalam sistem pakar ini diatasi dengan menggunakan metode probabilitas Bayesian. Proses penentuan diagnosa dalam sistem Pakar ini diawali dengan sesi konsultasi, dimana sistem akan mengajukan pertanyaan-pertanyaan yang relevan kepada pasien sesuai gejala utama penyakit paru-paru yang dialami pasien. 
Hasil akhir dari penelitian ini adalah sebuah sistem pakar untuk melakukan diagnosa penyakit paru-paru beserta nilai probabilitas dari penyakit. 
Hasil diagnosa yang menunjukkan tingkat kepercayaan sistem terhadap penyakit tersebut dan saran terapi yang harus diberikan.

Teorema Bayes adalah sebuah teorema dengan dua penafsiran berbeda. Dalam penafsiran Bayes, teorema ini menyatakan seberapa jauh derajat kepercayaan subjektif harus berubah secara rasional ketika ada petunjuk baru.
Dalam penafsiran frekuentis teorema ini menjelaskan representasi invers probabilitas dua kejadian.
Probabilitas bayes adalah salah satu cara untuk mengatasi ketidakpastian data dengan menggunakan formula Bayes yang dinyatakan sebagai berikut:

Suatu sistem pakar disusun oleh tiga modul utama yaitu:
1) Modul Penerimaan Pengetahuan (Knowledge Acquisition Mode) Sistem berada pada modul ini, pada saat ia menerima pengetahuan dari pakar. Proses mengumpulkan pengetahuan akan digunakan untuk pengembangan sistem, dilakukan dengan bantuan knowledge engineer. 
2) Modul Konsultasi (Consultation Mode) Pada saat sistem berada pada posisi memberikan jawaban atas permasalahan yang diajukan oleh user, sistem pakar berada dalam modul konsultasi. 
3) Modul Penjelasan (Explanation Mode) Modul ini menjelaskan proses pengambilan keputusan oleh sistem. 


Perhitungan dengan Theorema Bayes
Dengan ini akan di jelaskan cara melakukan perhitungan berdasarkan data berikut : 
1) Jumlah pasien 250. 
2) Penderita Tuberkolosis(TB): 100 orang, sehingga probabilitas terkena Tuberkolosis(TB) tanpa memandang gejala apapun , P(P4) adalah 100/250 
3) Pasien dengan gejala rasa sakit di dada saat menarik nafas dalam-dalam adalah 60 orang, sehingga probabilitas pasien dengan gejala rasa sakit di dada saat menarik nafas dalam-dalam jika menderita Tuberkolosis(TB) P(G0004|P4) = 60/100 
4) Penderita Pneumonia : 45 orang sehingga probabilitas terkena Pneumonia tanpa memandang gejala apapun , P(P1) adalah 45/250. 
5) Jika diketahui gejala rasa sakit di dada saat menarik nafas dalam-dalam dapat juga menyebabkan Pneumonia maka probabilitas pasien dengan gejala rasa sakit di dada saat menarik nafas dalam-dalam jika menderita Pneumonia, P(G0004|P1) adalah 20/45

Dengan menggunakan formula di atas dapat di hitung : 
Probabilitas Tuberkolosis(TB) jika di ketahui gejala rasa sakit di dada saat menarik nafas dalam-dalam, 
P(P4|G0004) = P(G0004|P4) * P(P4) + P(G0004|P1) * P(P1) P(G0004|P4) * P(P4) 
P(P4|G0004)= 60/100 .100/250+20/45. 45/250 60/100 .100/250 = 0.76 
Probabilitas Pneumonia jika diketahui gejala rasa sakit di dada saat menarik nafas dalam-dalam, P(P1|G0004)= P(G0004|P1) * P(P1) + P(G0004|P4) * P(P4) 
P(G0004|P1) * P(P1) P(P1|G0004)= 20/45. 45/250 + 60/100 .100/250 20/45. 45/250 = 0.23 
Dalam kasus Tuberkolosis(TB) dan Pneumonia nilai probabilitas 0.76 dan 0.23 mengandung makna bahwa probabilitas penyakit tersebut mencakup dari 250 orang pasien.

Kesimpulan
Adapun kesimpulan yang di peroleh oleh penulis adalah sebagai berikut : 
1. Sistem ini dapat membantu pasien untuk mendiaknosa penyakit yang dialami sehingga pasien dapat menangani penyakit yang diderita dengan cepat dan tepat. 
2. Dengan menggunakan metode bayes, sistem yang di bangun dapat mengatasi ketidakpastian dalam penyelesaian masalah.

Saran
Sebaiknya pembaca lebih memahami theorema bayes ini secara mendalam agar bisa lebih jelas dalam menerapkan theorema bayes dalam kecerdasan buatan.

Referensi
Subanar,2006, Inferensi Bayesian, Universitas Terbuka, Jakarta
Oemiati, 2013, Epidemiologis penyakit paru obstruktif kronik (PPOK), Vol. 23 No. 2, Jakarta 

Link Youtube
https://www.youtube.com/watch?v=RZcKwGtxmA0&t=13s 

Plagiatrisme
https://drive.google.com/open?id=0B17w878LGlWFbzJ6aWlhNzhobXM 


https://drive.google.com/open?id=0B17w878LGlWFbzZrZU9nOWMtTHc


Blog

http://dianditapuspita.blogspot.co.id/2017/06/kecerdasan-buatan-tugas-ke-6-tentang.html


