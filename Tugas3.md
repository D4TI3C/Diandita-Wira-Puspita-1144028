Diandita Wira Puspita
1144028
D4 Teknik Informatika 3C
Politeknik Pos Indonesia




Reasoning ( teknik penalaran ) yaitu teknik penyelesaian masalah yang mempresentasikan masalah masalah ke dalam logic ( mathematics tools yang digunakan untuk mempresentasikan dan memanipulasi fakta dan aturan).

Semantic network adalah representasi yang mengekspresikan solusi permasalahan dengan menggunakan network (graph berarah). Di dalamnya menggunakan node(simpul) untuk merepretasikan suatu kondisi, dan arc(link) untuk merepretasikan relasi antar simpul. 

Semantic network ini adalah representasi yang bersifat:

Lexically, di dalamnya terdapat node(simpul), link dan batasan-batasan khusus dari permasalahan
Structurally, masing-masing link akan terkoneksi dari simpul yang paling depan(head node) sampai simpul yang paling belakang (tail node).
Semantically, semua simpul dan link merepretasikan permasalahan tetao berada dalam batasannya.

Contoh:

Permasalahan pertani, serigala, angsa dan padi. Seorang petani ingin memindahkan dirinya sendiri, seekor serigala, seekor angsa gemuk, dan seikat padi yang berisi menyeberangi sungai. Sayangnya, perahunya sangat terbatas; dia hanya dapat membawa 1object dalam 1 penyeberangan. Dan lagi, dia tidak bisa meninggalkan angsa dan serigala dalam satu tempat, karena serigala akan memangsa angsa. Demikian pula dia tidak bisa meninggalkan angsa dan padi dalam satu tempat.
Mendeskripsikan permasalahan di atas dengan menggunakan bahasa natural bukanlah cara yang tepat. Dalam hal ini, kita dapa menggunakan Semantic Network untuk merepretasikannya.
Untuk membuat graph-nya, maka kita harus membangun node(simpul) untuk setiap kondisi yang memungkinkan bagi petani tersebut. Dengan memperhatikan petani dan tiga barangnya yang kemungkinan berada pada 2 seberang sungai, maka kita dapat menghitung jumlah simpul secara keseluruhan adalah 2^1+3= 2^4=16, dimana 10 simpul adalah kondisi yang aman (tidak ada satu barangpun yang termakan).
Langkah kedua dan merupakan langkah terakhir adalah membentuk link dari masing-masing perjalanan perahu. Pasangan dari dua buah node(simpul) dapat digabungkan dengan menggunakan link jika dan hanya jika bertemu pada 2 kondisi, yaitu: petama, petani berubah tempat, salah satu barang dari petani berubah tempat. Karena terdapat 10 buah simpul yang masuk dalam batasan (aman), dimungkinkan adanya 10 x 9 = 90 pasangan, akan tetapi hanya 20 link yang dapat terbentuk karena batasan sepertu yang disebut di atas.


Frame ditemukan oleh marvin Minsky pada tahun 1974 merupakan kumpulan pengetahuan tentang suatu object tertentu, peristiwa, lokasi, situasi, dll.
Frame memiliki slot yang menggambarkan rincian (atribut) dan karakteristik obyek. Frame biasanya digunakan untuk merepretasikan pengetahuan yang didasarkan pada karakteristik yang sudah dikenal, yang merupakan pengalaman-pengalaman. Dengan menggunakan frame, sangat mudah membuat inferensi tentang obyek, peristiwa atau situasi baru, karena frame menyediakan basis pengetahuan yang ditarik dari pengalaman. Ide hirariki dari frame sama dengan ide hirarki class yang terdapat pada pemrograman berorientasi obyek.

Bagaimana mengorganisir sebuah frame
Sebuah sistem frame merupakan hirarki dari frame-frame yang lain. Masing-masing frame memiliki:
Sebuah nama
Slot(tempat): yaitu komponen dari entiti yang mempunyai nama, dan mempunyai nilai. Nilai yang dimungkinkan adalah:
Identifikasi frame
Relasi dengan frame lain (slotnya: isa, instance)
Batasan nilai
Nilai: Default nilai (dapat berubah)
Prosedur untuk mendapatkan nilai
Prosedur yang dibangkitkan data (data driven): prosedur yang harus dilakukan jika nilai diubah, misal: periksa konsistensi kosong: untuk ditelusuri pada subclassnya.
Kesimpulan:
Semantic network adalah representasi yang mengekspresikan solusi permasalahan dengan menggunakan network (graph berarah). Di dalamnya menggunakan node(simpul) untuk merepretasikan suatu kondisi, dan arc(link) untuk merepretasikan relasi antar simpul. 

Saran:
Sebaiknya pembaca harus banyak mencari referensi agar lebih jelas.


Referensi:
1. Irawan. Jusak. 2007. Buku Pegangan Kuliah Sistem Pakar Sekolah Tinggi Manajemen Informatika & Teknik Komputer Surabaya. Surabaya: STIKOM


Plagiatrisme:
1. https://drive.google.com/open?id=0B17w878LGlWFLW5ESXRSQTlrSU0 
2. https://drive.google.com/open?id=0B17w878LGlWFLXFWSlI2Z3VRWEk 





