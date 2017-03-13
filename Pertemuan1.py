import time
start_time = time.time()
print("menghitung nilai rumus matematika menggunakan bahasa jawa ngoko")
d = raw_input("Masukan Nilai 1: ")
i = raw_input("Masukan Nilai 2: ")
a = raw_input("Masukan Nilai 3: ")
n = raw_input("Masukan Nilai 4: ")
s = raw_input("Masukan Nilai 5: ")

if d == 'siji':
	d=1

if d == 'loro':
	d=2

if d == 'telu':
	d=3

if d == 'papat':
	d=4

if d == 'limo':
	d=5

if d == 'enem':
	d=6

if d == 'pitu':
	d=7

if d == 'wolu':
	d=8

if d == 'songo':
	d=9

if d == 'nol':
	d=0


if i == 'siji':
	i=1

if i == 'loro':
	i=2

if i == 'telu':
	i=3

if i == 'papat':
	i=4

if i == 'limo':
	i=5

if i == 'enem':
	i=6

if i == 'pitu':
	i=7

if i == 'wolu':
	i=8

if i == 'songo':
	i=9

if i == 'nol':
	i=0
	

if a == 'siji':
	a=1

if a == 'loro':
	a=2

if a == 'telu':
	a=3

if a == 'papat':
	a=4

if a == 'limo':
	a=5

if a == 'enem':
	a=6

if a == 'pitu':
	a=7

if a == 'wolu':
	a=8

if a == 'songo':
	a=9

if a == 'nol':
	a=0


if n == 'siji':
	n=1

if n == 'loro':
	n=2

if n == 'telu':
	n=3

if n == 'papat':
	n=4

if n == 'limo':
	n=5

if n == 'enem':
	n=6

if n == 'pitu':
	n=7

if n == 'wolu':
	n=8

if n == 'songo':
	n=9

if n == 'nol':
	n=0

if s == 'siji':
	s=1

if s == 'loro':
	s=2

if s == 'telu':
	s=3

if s == 'papat':
	s=4

if s == 'limo':
	s=5

if s == 'enem':
	s=6

if s == 'pitu':
	s=7

if s == 'wolu':
	s=8

if s == 'songo':
	s=9

if s == 'nol':
	s=0	
	

jumlah =(d*i)+(a/n-s)
print ("hasil" , jumlah)
print("time : %s detik " % (time.time() - start_time))
