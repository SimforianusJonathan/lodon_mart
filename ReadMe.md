# LODON MART 
---
Tautan menuju PWS yang sudah di deploy :
[lodon mart link](http://simforianus-jonathan-lodonmart.pbp.cs.ui.ac.id/)
---

## TUGAS 1
### Step By Step
Step by step membuat proyek django :
1. membuat direktori lokal bernama "lodon_mart" (sesuai nama e-commerce saya)
2. Membuat dan mengaktifkan virtual environment dengan tujuan mengisolasi package serta dependencies dari aplikasi agar tidak bertabrakan dengan versi lain yang ada pada komputer
3. Membuat dokumen txt yang berisi list of dependencies (komponen / modul seperti library, framework, atau package yang berguna untuk mempercepat pengembangan dan developer / pengembang memanfaatkan kode yang sudah ada) yang dibutuhkan untuk membuat proyek django.
4. Melakukan instalasi terhadap depedencies yang ada di dalam dokumen txt (diberi nama requirements.txt) di dalam terminal dengan command 'pip install -r requirements.txt'
5. Membuat proyek django untuk e-commerce saya dengan instruksi 'django-admin startproject lodon_mart .'
6. Membuka file settings.py pada bagian direktori proyek 'lodon_mart' dan menambahkan 2 string' "localhost", "127.0.0.1" ' pada list bernama Allowed_Hosts untuk memungkinkan local host untuk mengakses proyek ini (dalam kondisi ini hanya bisa diakses dari jaringan pribadi saya).
7. Menjalankan server django dengan menjalankan program pada manage.py dengan instruksi 'python manage.py runserver'. Untuk menghentikan server pencet CTRL + C dan ketik 'deactivate' untuk keluar dari virtual environment.

Step by step membuat aplikasi main pada proyek 'lodon_mart' :
1. Membuat aplikasi baru dengan nama 'main' dengan instruksi 'python manage.py startapp main'. Akan tercipta direktori baru yang berisi struktur awal untuk aplikasi django lodon_mart.
2. Mendaftarkan aplikasi main ke dalam proyek 'lodon_mart' dengan menambahkan string 'main' pada list Installed_Apps pada file settings.py di dalam direktori proyek lodon_mart.

Step by step membuat fungsi pada views.py untuk dikembaklikan ke template html :
1. Membuat terlebih dahulu direktori baru bernama 'template' di dalam direktori 'main' lalu membuat file html yang berisikan format untuk menampilkan nama, kelas, dan npm.
2. Pada bagian views.py (mengimport render dari modul django.shortcuts), membuat fungsi baru(contoh nama : show_main) dengan parameter request. Lalu buatlah dictionary (contoh nama : context) di dalamnya dengan key masing-masing adalah nama,kelas,dan npm dengan value yang bersesuaian.
3. Buatlah agar fungsi show_main tersebut mereturn fungsi render dengan parameter(request, nama file html, dictionary berisi informasi nama, kelas, dan npm yang akan diteruskan ke tampilan untuk penampilan dinamis).
4. Setelah ini kita bisa dapat mengganti konten bagian nama, kelas, dan npm pada bagian file html dengan nama variabel di dalam '{{}}'
(Hal ini adalah tujuan dari render di file views.py agar dapat me render informasi value dalam dictionary konteks yang akan ditampilkan pada file html sesuai dengan nama key dari dictionary tersebut).

Step by step membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py :
1. pada file urls.py di direktori main, import path dari modul django.urls
2. Import fungsi show_main dari main.views.
3. Inisialisasi variabel untuk menyimpan nama aplikasi yaitu 'main'.
4. Membuat list dengan isi path('', show_main, name ='show_main').

keterangan :

path(...) -> Mendefiniskan pola url
'' -> Pola URL yang diberikan adalah string kosong, yang berarti ini adalah root atau home URL dari aplikasi
show_main -> fungsi pada views.py yang dipanggil saat url ini diakses
name = 'show-main' -> nama yang diberikan kepada pola url yang didefinisikan ini

Step by step melakukan routing untuk menjalankan aplikasi 'main' :
1. Membuka urls.py yang ada di direktori proyek 'lodon_mart' (bukan direktori main).
2. import path,include dari modul django.urls.
3. Menambahkan dalam list url_patterns ( yang awalnya hanya berisi path('admin/', admin.site.urls) ) dengan path('', include('main.urls')).

keterangan :

path(...) -> mendefinisikan pola url
'' -> diarahkan ke rute yang didefinisikan dalam berkas urls.py aplikasi main (dibuat string kosong agar halaman aplikasi main dapat langsung diakses).
include('main.urls') -> memasukkan pola url dari modul lain (di sini adalah urls.py dari direktori aplikasi 'main').

Step by step membuat model pada aplikasi main dengan nama Product dan memiliki atribut 'name', 'price', dan 'description' :
1. Membuka models.py dalam direktori aplikasi 'main'.
2. Membuat class baru bernama Product dengan parameter models.Model.
3. Menambahkan atribut name dengan tipe charField, price dengan tipe IntegerField, dan description dengan tipe TextField
4. Menambahkan properti berisi fungsi "_str_(self)" untuk menampilkan nama dan harga dari product (opsional).

Step by step deployment ke PWS terhadap aplikasi yang sudah dibuat :
1. Login akun PWS (dengan syarat sudah registrasi terlebih dahulu).
2. Menekan tombol 'Creat New Project '.
3. Mengisi nama poject dengan 'lodonmart'.
4. Menyimpan informasi credential untuk username dan password.
5. Membuka settings.py di direktori proyek 'lodon_mart' dan menambahkan url deployment pada list Allowed_Hosts menjadi 
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "http://simforianus-jonathan-lodonmart.pbp.cs.ui.ac.id/"]
6. Menyimpan perubahan pada repository github dengan melakukan add,commit,dan push.
7. Menjalankan instruksi yang ada di bagian project command di PWS.
8. Buka proyek lodonmart lewat akses sidebar dan menunggu status yang awalnya Building menjadi Running.
9. URL deployment dapat diakses.

### Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya
![alt text](image.png)

Penjelasan : 
1. User mengirimkan request melalui browser ke server
2. Internet menghubungkan pengguna dengan server aplikasi. request diteruskan via internet ke server yang menjalankan django.
3. Python Django sebagai framework yan digunakan sebagai pengelola utama aplikasi. django menerima request user dan diteruskan ke urls.py
4. Urls.py berisi kode untuk mendefinisikan url. urls.py mencari url yang cocok untuk diteruskan ke logic di views.py
4. views.py merupakan file berisi fungsi untuk menangani logika bisnis dan berinteraksi dengan data base lewat models.py
5. models.py berisi model yang didefinisikan developer yang digunakan untuk mengambil data yang diperlukan dari database lalu dilakukan perhitungan dan manipulasi data yang diperlukan untuk respons kembali dan akan dilakukan rendering kembali yang dipanggil di file views.py.
6. Template html seabagai interface / tampilan yang dilihat user (html,css, js). django akan me render template html dengan menggabung data yang dihasilkan sebagai respond dan dikembalikan oleh aplikasi melalui internet kembali kepada user. respond berupa perubahan pada halaman halaman html tergantung request yang diberikan oleh user pada awal kesempatan.

### GIT RELATED
Git merupakan suatu perangkat lunak pengendali versi atau proyek manajemen kode perangkat lunak.

Fungsi Git dalam pengembangan perangkat lunak :

1. Control Version
Kontrol versi merupakan salah satu fungsi utama dari git, yaitu sebuah sistem untuk mengatur pengelolaan perubahan pada source code atau dari dokumen-dokumen lainnya (sinkronisasi perubahan pada source code).

Tujuannya :
1a. Tracking terhadap perubahan source code dari waktu ke waktu untuk tujuan pemantauan. Hal tersebut juga didukung oleh fitur pada git yang dapat melakukan tagging / labeling pada tahap tertentu dalam riwayat revisi kode.

1b. Recover / Rollback kode ke versi sebelum diupdate atau direvisi (jika update yang baru kurang sesuai dan preferensi lebih menuju ke arah source code sebelum dilakukan perubahan).


2. Branching dan Merging
2a. Branching yang memungkinkan para developer untuk dapat membuat cabang baru yang dapat digunakan untuk perbaikan bug pada kode atau melakukan improvement lainnya pada kode yang nantinya bisa kembali di merging ke branch utama.

2b. Merging kode dari beberapa developer dan dapat disimpan di branch yang berebeda

2c. Git yang dapat membantu untuk meresolusi konflik saat terjadinya merging antara beberapa developer

2d. Forking / mendapatkan salinan terhadap kode proyek yang dapat dimodifikasi untuk kepentingan developer dan bisa mengajukan perubahan tersebut (melalui pull request).

3. Kolaborasi 
Hal paling lainnya adalah kolaborasi. Lewat git sebagai proyek manajemen kode ini, para developer bisa mengerjakan suatu proyek secara simultan / bersamaan dengan melakukan branching, merging, forking, maupun resolusi konflik seperti yang sudah dijelaskan untuk mempermudah pekerjaan. Hal tersebut dapat meningkatkan efisiensi dalam berkerja .

4. Security
Git dapat memebrikan kita untuk memilih  orang orang tertentu (developer) yang ingin diberikan izin untuk diberikan kontrol akses terhadap source code pada repositori yang ada serta akses untuk melakukan perubahan terhadap kode tersebut.

### DJANGO FOR STARTING POINT
Alasan mengapa framework django menjadi opsi sebagai awal untuk mempelajari pengembangan perangkat lunak :

1. Dokumentasi 
Dokumentasi django dibuat dengan lengkap dan rinci mulai dari tutorial terhadap penggunaan django dan tahapan untuk membuat project pertama dengan django, guides untuk topik,konsep,dan latar belakang informasi mengenai django, guide terhadap referensi teknikal untuk API dan aspek lain mesin django, dan lainnya.

2. Fitur 
Fitur bawaan django yang ditawarkan oleh django lumayan lengkap seperti admin interface seperti sistem templating untuk aplikasi dan proyek yang cukup lengkap, autentikasi pengguna, dan juga ORM (Object-Relational Mapping) yang akan dijelaskan nanti.

3. Python Language
Sebagai salah satu mahasiswa Fasilkom UI yang sempat belajar DDP1 di semester 1 lalu. Saya merasa dimudahkan dalam penggunaan framework django yang menggunakan dasar bahasa pemrograman python. Di samping pengalaman saya dalam mempelajari python, menurut saya untuk para pemula yang baru belajar, bahasa pemrograman python merupakan salah satu bahasa pemrograman yang mudah dipahami, sehingga cukup mudah untuk mempelajari penggunaaan dan menggunakan framework django untuk memulai pembelajaran terhadap pengembangan perangkat lunak.

4. Security
Fitur keamanan django yang dibuat untuk mengantisipasi serangan seperti Cross-Site Scripting (memasukkan kode html ke suatu website seakan akan merupakan suatu kode bawaan dari website tersebut yang dapat menyebabkan kerusakan situs / pencurian info pribadi), Cross-Site Request Forgery (pemalsuan permintaan izin akses dari suatu website yang biasanya untuk pencurian info pribadi), dan SQL Injection (memanfaatkan celah keamanan untuk mengakses data dari database yang tidak diberikan akses).

#### Django and ORM 
 ORM sendiri adalah teknik pemrograman untuk menggunakan database relasional untuk menyimpan data dalam bentuk objek. Bahas pemrograman yang digunakan harus support OOP untuk dapat menggunakan database relasional sebagai penyimpanan.

model django disebut ORM (Object-Relational Mapping).
Hal tersebut dapat dikatakan dengan alasan dengan definisi suatu class dan instansiasi objek lewat bahas pemrograman python dapat digunakan untuk berinteraksi dengan database tanpa harus melakukan query secara terpisah untuk berinteraksi database.

---
## TUGAS 2

### Step by Step 
Disclaimer :
Sebelumnya telah dibuat file untuk template html, yaitu "base.html" yang berfungsi sebagai template dasar yang dapat digunakan sebagai kerangka umum untuk halaman web lainnya di dalam proyek dan juga "main.html" untuk menampilkan halaman utama saat memasuki website proyek lodon mart.

Step by Step Membuat input form untuk menambahkan objek model pada app sebelumnya :
1. Membuat berkas baru bernama forms.py pada direktori aplikasi main.
2. Pada bagian awal kode, import ModelForm dari modul django.forms dan import class Product dari main.models
3. Membuat class baru bernama "ProductForm" dan buatlah class lagi di dalamnya bernama "Meta".
4. Di dalam class meta, definisikan 
"model = Product"
Kode tersebut menunjukkan model untuk form di mana data dari pengisian form aku disimpan dalam bentuk objek class 'Product' yang diimport dari models.py di direktori aplikasi main saat ini.
5. tambahkan baris "fields = ["name", "price", "description"]" sebagai field dari model "Product" yang digunakan untuk form.
6. Di bagian berkas views.py, tambahkan import baru untuk redirect dari modul django.shortcuts
7. membuat fungsi baru bernama create_product dengan isi
"""
form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
"""
baris pertama digunakan untuk membuat entry ProductForm baru dengan memasukkan QueryDict berdasarkan input dari user pada request.POST.

baris "IF" berguna untuk menyimpan data hasil dari input form jika telah divalidasi dan jika dilakukan post request oleh user. Setelah itu dilakukan redirecting ke fungsi show_main pada views aplikasi main setelah data form berhasil disimpan.

Buatlah agar fungsi create_product tersebut mereturn fungsi render dengan parameter(request, nama file html (di sini sudah disediakan file html template bernama create_product.html), dictionary berisi tulisan form sebagai key dan value nya yang akan diteruskan ke tampilan untuk penampilan dinamis).

8. Membuka berkas urls.py di direktori aplikasi main lalu menambahkan fungsi create_product yang diimport dari main.views.
9. Menambahkan pola url untuk diproses daat request di minta pada list urlpatterns yaitu 
" path('create-product', create_product, name='create_product') ".

keterangan :
path(...) -> Mendefiniskan pola url
'create-product' -> Pola URL yang akan ditangani adalah /create-product.
create_product -> fungsi pada views.py yang dipanggil saat url ini diakses
name = 'create_product' -> nama yang diberikan kepada pola url yang didefinisikan ini. Pemberian nama ini berguna untuk membuat referensi URL secara dinamis di template atau di bagian lain dari aplikasi Django

11. Membuat berkas html baru di direktori template dengan nama "create_product.html" sesuai dengan nama berkas html yang diletakan dalam parameter fungsi sebagai lokasi untuk di render dalam fungsi buatan create_product di berkas views.py direktori aplikasi main.
12. create_product.html ini dibuat dengan melakukan extend dari base.html sebagai template dasar website dengan isi block content tag form dengan atribut method = POST, lalu template tags untuk crsf token yang berfungsi sebagai security, lalu tag table berisi template tag  {{ form.as_table }} yang digunakan untuk menampilkan fields form yang sudah dibuat pada forms.py sebagai table dan di dalamnya tambahkan tag <input type="submit" value="Add Product"/> digunakan sebagai tombol submit untuk mengirimkan request ke view create_product(request).
13. Pada berkas main.html sebaga halaman utama, menambahkan tag tautan link dengan atribut href untuk mendefinisikan alamat link berupa template tag django dengan isi url app_name:path_name yang telah didefinisikan di urls.py (pada direktori aplikasi main dan untuk menjalankan fungsi create_product) dan menambahkan tag button sebegai event yang harus dilakukan untuk redirecting ke halaman baru untuk mengisi form data produk baru.

Potongan kode :
<a href="{% url 'main:create_product' %}">
  <button>Add New Product</button>
</a>

14. Pada fungsi show_main yang sebelumnya sudah kita buat untuk menampilkan tampilan utama berupa nama, kelas, dan npm, kita tambahkan baris baru pada awal fungsi "products = Product.objects.all()" yang digunakan untuk mengambil seluruh objek Product yang tersimpan pada database. Lalu menambahkan data baru dalam dictionary dengan key dan value yaitu "products". (Opsional dilakukan untuk menampilkan data-data hasil entry yang sudah ada di database setelah form diisi dan valid).

Step by Step membuat  4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
1.  Membuka berkas views.py pada direktori aplikasi main
2.  Mengimport HttpResponse dari modul django.http dan import  serializers dari modul django.core
3. Tambahkan beberapa kode di bawah :
"""
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
"""
keterangan :

- baris "data = Product.objects.all()" digunakan untuk mengambil seluruh objek Product yang tersimpan pada database

- baris "data = Product.objects.filter(pk=id)" digunakan mendapatkan semua objek Product dari database di mana primary key (pk) objek tersebut sama dengan nilai atribut id pada class Product yang telah di modelkan di direktori aplikasi main di berkas models.py

- baris "return HttpResponse(serializers.serialize("...", data), content_type="application/...")" digunakan untuk mengirimkan respons HTTP kepada client dengan parameter yang menyimpan data hasil query yang telah di translasi  objek model menjadi format lain seperti (dalam fungsi yang ada berupa XML / JSON) oleh fungsi serialize dari objek serializers dan juga parameter content_type yaitu header HTTP menentukan tipeMIME dari respons agar client dapat mengetahui format data yang dikrimkan (dalam fungsi yang ada yaitu JSON atau XML).

fungsi :
- show_xml = mengembalikan data dalam bentuk xml
- show_json = mengembalikan data dalam bentuk json
- show_xml_by_id = mengembalikan data dalam bentuk xml sesuai atribut id pada class Product yang telah digenerate menggunakan modul uuid
- show_json_by_id = mengembalikan data dalam bentuk json esuai atribut id pada class Product yang telah digenerate menggunakan modul uuid

Step by step membuat routing URL untuk masing-masing views yang telah ditambahkan :
1. Membuka berkas urls.py pada direktori aplikasi main.
2. Mengimport fungsi yang sudah dibuat, yaitu show_xml,show_json,show_json_by_id,show_xml_by_id dari main.views.
3. Menambahkan path baru dalam list urlpatterns untuk masing masing fungsi yang telah dibuat.

Potongan kode :
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:id>/', show_json_by_id, name='show_json_by_id')

keterangan :
path(...) -> Mendefiniskan pola url
'...' -> Pola URL yang akan ditangani adalah "xml/" atau "json/" atau "xml/id" atau "json/id".
"show_...." -> fungsi pada views.py yang dipanggil saat url ini diakses
name = 'show_...' -> nama yang diberikan kepada pola url yang didefinisikan ini. Pemberian nama ini berguna untuk membuat referensi URL secara dinamis di template atau di bagian lain dari aplikasi Django

### Pentingnya Data Delivery dalam Implementasi Platform

1. Integritas Sistem dan Sinkronisasi data
Data delivery dalam suatu platform yang melibatkan banyak pengguna dan sistem dapat menjaga sinkronisasi antara data pusat dengan data yang ditampilkan dapat diakses melalui platform tersebut. Jadi dapat menghindari terjadinya misinformasi dan dapat memberikan update informasi secara real time kepada pengguna.
Data delivery juga membantu dalam integrasi sistem. Hal tersebut dapat dilihat dari berbagai jenis sumber data yang digunakan oleh platform modern yang digabungkan mulai dari database internal maupun API eksternal. Data delivery memungkinan pengaksesan data-data tersebut dan dapat diproses di satu tempat / wadah.

2. Pengalaman Pengguna
Pengiriman data yang cepat dan konsisten dapat meningkatkan kepuasan dalam pengalaman pengguna di platform tersebut. Selain itu karena pengiriman data biasa dilakukan juga untuk fitur interaktif untuk para pengguna seperti notifikasi chat atau notifikasi untuk pembaharuan. Pengalaman pengguna yang mulus dan cepat sangat bergantung pada pengiriman data yang cepat dan andal.

3. Analisis Data dan Laporan
Dengan sistem data delivery yang dapat membantu sinkronisasi data pada data pusat dan platforn serta integrasi data dari berbagai sumber yang berbeda di dalam satu tempat (data warehouse / data lake) dapat memungkinkan ketersediaan data yang uptodate agara dapat dilakukan analisis yang komprehensif ynag tentunya digunakan untuk pengembangan sistem yang lebih baik atau melakukan penambahan fitur. Selain itu, data delivery juga  memastikan data yang digunakan untuk membuat laporan selalu up-to-date dan akurat.

4. Migrasi Data
Data delivery dapat digunakan untuk melakukan pemindahan data dari sistem lama ke sistem yang baru. Hal tersebut biasanya dilakukan oleh suatu perusahaan yang ingin melakukan perpindahan menuju platform yang baru dengan tujuan untuk meningkatkan efektivitas dan efisiensi dalam bekerja atau melakukan perubahan dalam sistem dan dalam menjalankan platform yang telah dibuat.

### XML dan JSON

Berikut beberapa alasan mengapa JSON lebih populer penggunaannya dibanding XML :

1. Syntax JSON dan XML
Syantax milik JSON lebih ringkas dan simple dibandingkan XML. Hal itu dapat menentukan kenyamanan bagi para developer untuk cenderung memilih JSON dibadndaingkan dengan XML. JSON menggunakan tanda kurung kurawal {} untuk objek dan tanda kurung siku [] untuk array, yang membuatnya lebih mudah dibaca dan ditulis daripada XML, yang menggunakan tag pembuka dan penutup.

2. JavaScript
JSON adalah format yang asli untuk JavaScript, sehingga pengelolaan dan proses manipulasi lebih mudah apabila digunakan dalam aplikasi web yang berbasis JavaScript. Selain itu JS memiliki beberapa built in function yang dikhususkan untuk mengakses JSON, sehingga lebih sederhana dan efisien dalam pengerjaannya (contoh : JSON.parse() dan JSON.stringify()).

3. Readability
Karena Syntax dari JSON yang lebih ringkas dan tidak diperlukan tag tag untuk menulis informasinya / datanya membuat JSON terlihat lebih mudah untuk dibaca bagi manusia dan dimengerti dibandingkan dengan XML yang walaupun terlihat lebih terstruktur, masih memberikan kesan yang kurang rapih dan lebih kompleks dibandingkan JSON.

4. Ukuran File
Ukuran File JSON lebih kecil dibandingkan dengan XML karena syntax yang sederhana. Sedangkan XML mengambil memori yang lebih besar karena ukuran file nya yang lebih besar pula dilihat dari syntaxnya yang memerlukan beberapa tag untuk informasi yang ada dan belum termasuk atribut (info mendetail) yang merupakan bawaan dari tag nya. Hal tersebut memungkinkan JSON untuk dapat mengurangi penggunaan bandwidth dan waktu pemrosesan saat mentransfer data melalui jaringan.

5. Fleksibilitas
JSON memberikan para developer kemudahan dan fleksibiltas dalam mengelola dan pengembangan data karena datanya lebih dinamis dan tentunya mudah untuk diubah. Dibandingkan dengan JSON, XML terlihat lebih kaku karena harus mengikuti skema yang ketat seperti XSD (XML Scheme Definition).

Sebagai seorang programmer, kita tidak bisa menyimpulkan mengenai bahasa pemrograman terbaik, framework terbaik, platform terbaik, dan lainnya. Semua bahasa pemrograman, framework, maupun sistem data delivery dibangun dengan spesifikasi yang berbeda-beda, serta memiliki kekurangan dan kelebihan masing-masing. Pemakaian sistem data delivery pada suatu platform disesuaikan dengan kebutuhan perusahaan atau kebutuhan pengembang terhadap aplikasi tersebut. Apabila kita ingin memiliki format data yang lebih ringkas(lebih mudah dibaca dan diterjemahkan) dan lebih mudah untuk diproses (efektifitas transmisi data), dan khsususnya jika mengembangkan suatuplatform berbasis javascript.. JSON merupakan pilihan yang lebih baik dan memudahkan dibandingkan XML. Namun, jika anda membutuhkan struktur data yang sangat terperinci dengan dukungan untuk validasi dan metadata tambahan, memerlukan dukungan untuk namespace yang kompleks, dan jika tuntutan dari terdapat pekerjaan di mana skema validasi atau markup dokumen penting... anda dapat memilih untuk menggunakan XML. Jadi tidak ada yang lebih baik antara satu sama lain, namun mana yang lebih cocok pengunaannya bagi para developer yang dapat memudahkan pekerjaan mereka. (pendapat pribadi saya).

### Fungsi Method is_valid() pada Form Django

Ketika pengguna mengirimkan data melalui formulir, metode is_valid() akan memeriksa apakah data yang dimasukkan memenuhi semua persyaratan validasi yang telah ditetapkan. Validasi tersebut ditentukan berdasarkan dari kelas "form". Selain itu, method ini juga mencakup validasi built-in Django (seperti validasi email atau angka) dan juga validasi lain yang telah developer tambahkan. Method ini akan me return suatu tipe data boolean. Jika valid akan return "true" dan jika tidak akan return "false". Jika kita memanggil method is_valid() maka Django secara otomatis memanggil metode clean() pada form dan pada setiap field form = clean_<fieldname>().

Method ini dibutuhkan untuk :
1. Keamanan Data yang terjamin karena sebelum data dimasukkan de dalam database, data tersebut diproses lewat method is_valid() ini sehingga dapat membantu untuk menjaga integritas data dan mencegah inkonsistensi data atau data yang tidak valid. Hal tersebut dapat mencegah serangan siber seperti SQL Injection atau XSS(Cross Site Scripting).
2. Responsif terhadap pengguna / client karena jika data yang diberikan tidak valid, akan muncul suatu error berbentuk notifikasi / pemberitahuan dan dapat membantu pengguna untuk mengirim data selanjutnya dengan benar.

### CSRF Token Pada Django

CSRF (Cross-Site Request Forgery) adalah serangan siber dimana attacker mengirimkan request ke sebuah aplikasi web dengan mengatasnamakan akun user yang telah terautentikasi dan tentunya tidak diketahui oleh user asli dan tanpa persetujuan terlebih dahulu. CSRF yang disediakan oleh Django dibuat dengan tujuan untuk mencegah terjadinya serangan CSRF pada aplikasi web kita. CSRF token memastikan bahwa permintaan yang dikirim ke server berasal dari sumber yang sah dan bukan dari penyerang. Token ini berupa string unik yang dikirim oleh server ke browser pengguna dan dikirim kembali dengan setiap permintaan untuk mengolah data. Dengan begini para attacker akan kesusahan karena akan kesulitan untuk mencoba mengakses karena tidak memiliki token user yang valid.

Jika tidak mengaplikasian csrf token ini. Maka attacker dapat lebih mudah untuk melakukan pengaksesan tanpa seizin user yang valid dan dapat melakukan berbagai hal seperti membuat form palsu yang bisa jadi berisi permintaan yang berbahaya untuk situs kita. Serta dapat mengubah pengaturan akun maupun sistem yang ada seperti mengubah password pengguna atau menghapus akun pengguna serta dapat membuat form palsu untuk melakukan transaksi keuangan maupun pembelian terhadap suatu barang / jasa, dan juga dengan membuat banyak permintaan yang tidak sah, yang bisa menyebabkan kerusakan sistem atau beban berlebih pada server.

Cara mereka memanfatkan kesempatan tersebut bisa dengan pembuatan halaman web yang berisi script yang mengirimkan request ke aplikasi target tanpa sepengetahuan pengguna(biasanya menggunakan iframe tersembunyi). Dengan cara seperti itu, Jika pengguna yang terautentikasi mengunjungi halaman berbahaya yang telah dibuat oleh penyerang, permintaan yang dikirim dari halaman tersebut dapat menggunakan kredensial pengguna untuk melakukan suatu tindakan tanpa diektahui oleh pengguna tersebut.

### Screenshoot Postman
JSON
![Postman JSON](image-2.png)
XML
![Postman XML](image-1.png)
JSON by ID
![Postman JSON by ID](image-3.png)
XML by ID
![Postman JSON by ID](image-4.png)





