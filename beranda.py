from os import link
from turtle import width
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


#st sidebar
with st.sidebar:
    selected=option_menu(
        menu_title="Menu",
        options=["Home","Library","Video Reference","Exam"],   
    )

if selected == "Home":
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    st.markdown("""
   <!-- As a heading -->
   <nav class="navbar" style="background-color :#310AC5" >
  <div class="container-fluid">
    <h1 class="text-white"style="alight:text-center">HOME</h2>
   </div>
   </nav>
    """, unsafe_allow_html=True)

    st.title('WELCOME TO LEARN CS')
    st.subheader("Learn CS adalah  web aplikasi untuk edukasi untuk mengetahui apa itu Cyber Security .")
    image =Image.open('photo.jfif')
    st.image(image)
    st.markdown(
    """
    Mengapa kita harus memahami Cyber Security??
    
    
    Secara umum cyber security lebih dikenal sebagai upaya untuk melindungi informasi dari adanya cyber attack.
    Cyber attack sendiri merupakan tindakan yang sengaja dilakukan oleh satu atau sekelompok orang untuk mengganggu confidentiality, integrity, dan, availability data

"""

)



    st.markdown ("""
    "Bagaimana Persepsi Keamanan Data Pribadi Pengguna Internet di Indonesia?"

Kebocoran data pribadi kian marak terjadi belakangan ini. Mulai dari data pengguna platform market place seperti Tokopedia
Lantas, bagaimana persepsi pengguna internet di Indonesia atas keamanan data pribadinya? Hasil survei yang dilakukan oleh Asosiasi Penyelenggara Jasa Internet Indonesia (APJII) menemukan lebih dari setengah penggguna internet di Indonesia merasa data pribadinya di internet aman tanpa meraka ketahui bahwa data mereka juga telah terbobol.
Sehingga Kita harus tahu apa itu cyber security dan bagaimana cara kita terhindar dari Cyber attack """)  

if selected == "Library":
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    st.markdown("""
   <!-- As a heading -->
   <nav class="navbar" style="background-color :#310AC5" >
  <div class="container-fluid">
    <h1 class="text-white"style="alight:text-center">Library</h2>
   </div>
   </nav>
    """, unsafe_allow_html=True)
 
    st.subheader("APA ITU CYBER SECURITY?")
    image =Image.open('Cyber security.png')
    st.image(image)
    st.write("""Cyber Security adalah keamanan informasi yang diaplikasikan kepada komputer dan jaringannya. Keamanan komputer bertujuan membantu pengguna agar dapat mencegah penipuan atau mendeteksi adanya usaha penipuan di sebuah sistem yang berbasis informasi. Tanpa Cyber Security keamanan kita pasti akan dengan mudah di akses oleh orang lain , oleh karena itu, untuk mengamankan informasi yang kita miliki kita harus menerapkan Cyber Security Tersebut.
Manfaat dari cyber security yaitu untuk menjaga dan mencegah penyalahgunaan akses maupun pemanfaatan data dalam sistem Teknologi Informasi dari seseorang yang tidak memiliki hak untuk mengakses maupun memanfaatkan data dalam sistem tersebut. """)

    st.caption("https://www.udemy.com/course/cyber-security-bisaai/")
    st.write("_____________________________________________________________________________________________________________________________________________________________")

    st.title("Siapa Pelaku Cyber?")
    gamabar=Image.open('Hackers.jpg')
    st.image(gamabar, caption='https://rakitaplikasi.com/blog/pengertian-dan-jenis-jenis-hacker')
    
    st.markdown("""
    Hacker adalah Seseorang yang memiliki Keahlian berkaitan dengan sistem komputer dan pemrograman. Programmer istilah sendiri mengalami perkembangan pengertian dan definisi. Kata “hacker” mulai muncul di akhir tahun 1950-a, merujuk pada pengembang para mahir. Kemudian di Tahun 1970-an, istilah hacker digunakan untuk menggambarkan para revolusioner komputer yang menjadi cikal-bakal para pendiri perusahaan komputer. Akhir Tahun 1980-a, hacker kata identik dengan pembajakan fitur pengalihan dengan menghilangkan proteksi dan menjualnya. dan sebelumnya saat ini banyak yang mengartikan negatif bahwa hacker ialah seseorang yang menerobos sistem komputer guna mengumpulkan informasi, akses menolak, berkas cara menghapus atau cara mengacaukan sistem komputer.

Pengertian negatif dari hacker tidaklah sepenuhnya benar, meskipun memang ada jenis hacker yang aksinya melakukan hal-hal demikian. Hacker jenis ini sering disebut sebagai chacker. Hacker Banyak Yang aktivitasnya ialah mengamankan sistem komputer agar tidak mudah disusupi dari program-program Jahat. Agar anda tidak terlalu menganggap negatif istilah hacker, ada baiknya anda mengenal beberapa jenis hacker yang ada sebelumnya saat ini
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
       st.header("WHITE HAT HACKER")
       st.write("""White Hat Hacker ialah hacker yang memegang teguh standar etika, akses ke sistem komputer dilakukan bukan untuk tujuan yang merugikan, tetapi untuk menguji ketahanan sistem tersebut. Jadi, hacker jenis ini senang mempelajari sebuah jaringan sistem,
     bahkan banyak dari mereka yang disewa sebagai konsultan keamanan. White Hat Hacker inilah ialah hacker yang sebenarnya
     Sering disebut dengan ethical hacker
Contoh :Security Auditor,Penetration Tester
     """)

    with col2:
      st.header("GREY HAT HACKER")
      st.write("""Grey Hat Hacker ialah seseorang yang menganut standar etika ganda dalam melaksanakan hackingnya. Sekali Waktu hacker mungkin ini menjunjung etika hacker,
     namun di waktu yang lain aktivitasnya melanggar batas-batas hukum. Jadi, Kelompok hacker ini berada di hacker topi antara white dan black hat hacker.
     Contoh :Hacktivist ,Vulnerability Broker ,Bug Bounty Hunter""")


    with col3:
      st.header("BLACK HAT HACKER")
      st.write("""Black Hat Hacker ialah jenis hacker yang aktivitasnya menerobos sistem keamanan komputer untuk melakukan kerusakan, seperti: cara menghapus berkas, identitas pencurian, penipuan kartu kredit dan berbagi aktvitas lainnya yang merugikan. 
    Hacker jenis ini disebut juga sebagai chacker.Contoh :
    Cyber Criminal,Ransomware Gang""")


    st.write("_____________________________________________________________________________________________________________________________________________________________")

    st.header("Prinsip Dasar Keamanan Cyber")
    st.markdown("""JAKARTA (IndoTelko)c– Schneider Electric mengungkapkan pentingnya memahami risiko keamanan teknologi operasional (Operational Technology / OT) dan prinsip dasar dalam memperkuat ekosistem digital agar lebih aman, lebih produktif dan lebih efisien untuk mengantisipasi risiko serangan siber (cybercrime) yang semakin tinggi di era revolusi industri 4.0.
   
Konsep Dasar Cyber Security
Keamanan dunia maya secara keseluruhan adalah istilah yang sangat luas, tetapi didasarkan pada tiga konsep dasar yang dikenal sebagai “Trias CIA” yang terdiri dari Confidentiality, Integrity, dan Availability. Konsep ini bertujuan untuk memimpin organisasi dengan pedoman keamanan informasi di bidang keamanan informasi. Berikut penjelasanya:

1. Confidentiality
Cyber Security adalah aturan yang membatasi akses ke informasi dengan mengambil tindakan untuk membatasi akses peretas cyber ke informasi sensitif. Dalam suatu organisasi, orang diberi wewenang atau ditolak akses ke informasi berdasarkan kategorinya dengan memberikan izin kepada orang yang tepat di suatu departemen. Pelatihan yang tepat tentang berbagi informasi dan melindungi akun Anda dengan kata sandi aman juga ditawarkan

Anda dapat mengubah cara data dikelola dalam suatu organisasi untuk memastikan privasi. Opsi untuk memastikan kerahasiaan adalah otentikasi merupakan faktor enkripsi data, klasifikasi data, verifikasi biometrik, dan token keamanan.

2. Integrity
Integrity memastikan bahwa data konsisten, akurat, dan dapat diandalkan untuk jangka waktu tertentu. Ini berarti bahwa data tidak dapat diubah, dihapus, atau diakses secara ilegal selama transmisi. Suatu organisasi harus mengambil tindakan yang tepat untuk memastikan keamanannya. Izin file dan kontrol akses pengguna adalah langkah-langkah yang mencegah data diretas.

Selain itu, alat dan teknologi harus digunakan untuk mendeteksi perubahan atau pelanggaran data. Banyak organisasi menggunakan checksum dan checksum kriptografi untuk memverifikasi integritas data. Untuk mencegah kehilangan data atau penghapusan tidak disengaja atau bahkan serangan dunia maya, cadangan reguler harus ada. Cloud backup adalah solusi paling andal saat ini

3. Availability
Dalam hal ini, Availability mencakup persyaratan seperti perangkat keras, perangkat lunak, jaringan, dan perangkat keamanan yang kinerjanya harus dipertahankan dan ditingkatkan. Hal ini dilakukan untuk memastikan operasi yang lancar dan akses yang tidak terputus ke data dan untuk memastikan komunikasi yang konstan antara komponen dengan menyediakan bandwidth yang cukup.

Poin ini juga mencakup pemilihan perangkat keamanan tambahan jika terjadi bencana atau kemacetan lalu lintas. Utilitas seperti firewall, rencana pemulihan bencana, server proxy dan solusi cadangan yang sesuai harus diasuransikan untuk mengelola serangan penolakan layanan.

____________________________________________________________________________________________________________________________________________________________

Elemen Pokok Cyber Security
Berikut adalah beberapa elemen pokok dari Cyber Security:

a.Document security policy, adalah dokumen standar yang digunakan sebagai referensi untuk melaksanakan semua proses keamanan informasi.
Information

b.infrastructure, adalah media yang berperan dalam kelangsungan proses informasi, termasuk perangkat keras dan perangkat lunak.

c.Perimeter Defense, adalah media yang bertindak sebagai komponen pertahanan dalam infrastruktur TI seperti IDS, IPS dan firewall.

d. Network Monitoring System, adalah media yang tugasnya memantau kelayakan, penggunaan, dan kinerja infrastruktur informasi.

e. System Information and Event Management, adalah media yang berperan dalam memantau berbagai peristiwa di jaringan, termasuk peristiwa yang terkait dengan insiden keamanan.

f. Network Security Assessment, adalah elemen keamanan dunia maya yang berfungsi sebagai mekanisme kontrol dan memungkinkan keamanan informasi.

g. Human resource dan security awareness, dalam kaitannya dengan sumber daya manusia dan kesadaran keamanan informasi.
   """)
    st.write("_____________________________________________________________________________________________________________________________________________________________")

    st.subheader("Kriptografi")
    st.write("""

Kriptografi (atau kriptologi; dari bahasa Yunani κρυπτός kryptós, "tersembunyi, rahasia"; dan γράφειν graphein, "menulis", atau -λογία logi, "ilmu")

[1] merupakan keahlian dan ilmu dari cara-cara untuk komunikasi aman pada kehadirannya di pihak ketiga.

[2] Secara umum, kriptografi ialah mengenai mengkonstruksi dan menganalisis protokol komunikasi yang dapat memblokir lawan;


[3] berbagai aspek dalam keamanan informasi seperti data rahasia, integritas data, autentikasi, dan non-repudansi

[4] merupakan pusat dari kriptografi modern.

 Kriptografi modern terjadi karena terdapat titik temu antara disiplin ilmu matematika, ilmu komputer, dan teknik elektro. Aplikasi dari kriptografi termasuk ATM, password komputer, dan E-commerce.
Kriptografi sebelum merupakan sinonim dari "enkripsi", konversi dari kalimat-kalimat yang dapat dibaca menjadi kelihatan tidak masuk akal. Pembuat dari pesan enkripsi membagi teknik pemecahan sandi yang dibutuhkan untuk mengembalikan informasi asli jika hanya dengan penerima yang diinginkan, sehingga dapat mencegah orang yang tidak diinginkan melakukan hal yang sama
""")
    st.caption("wikipedia")

    st.write("_____________________________________________________________________________________________________________________________________________________________")

    st.subheader("TEKNIK SEDERHANA KRIPTOGRAFI")
    st.write("A.CAESAR CIPHER")

    st.markdown( '''
     Caesar Cipher merupakan salah 
satu algoritma cipher tertua dan paling 
diketahui dalam perkembangan ilmu 
kriptografi. Caesar cipher merupakan salah 
satu jenis cipher substitusi yang
membentuk cipher dengan cara melakukan 
penukaran karakter pada plainteks menjadi 
tepat satu karakter pada chiperteks. Teknik 
seperti ini disebut juga sebagai chiper abjad 
tunggal.Algoritma kriptografi Caesar Cipher 
sangat mudah untuk digunakan. Inti dari 
algoritma kriptografi ini adalah melakukan
pergeseran terhadap semua karakter pada 
plainteks dengan nilai pergeseran yangsama. Adapun langkah-langkah yang 
dilakukan untuk membentuk chiperteks
dengan Caesar Cipher adalah:

a. Menentukan besarnya pergeseran
karakter yang digunakan dalam
membentuk cipherteks ke plainteks

b. Menukarkan karakter pada plainteks
menjadi cipherteks dengan berdasarkan
pada pergeseran yang telah ditentukan
sebelumnya
     ''')


    st.write("---------------------------------------------------------------------------------------------------")

    st.subheader("B.Substitution Cipher")
    poto=Image.open("caesar.png")
    st.image(poto)

    st.write("Cipher Substitusi adalah cipher dengan cara mensubstitusi huruf dengan huruf yang lain sesuai dengan yang ditetapkan. Prinsip utama cipher substitusi adalah menukarkan setiap huruf pada plainteks dengan sesuatu. Cipher substitusi termasuk algoritma kriptografi klasik. Idenya adalah menggantikan sebuah atau lebih huruf pada plainteks dengan sebuah atau lebih huruf pada plainteks dengan aturan tertentu. Aturan tersebut bergantung cara proses enkripsi dan dekripsi")
    st.caption("Coba Caesar chipher pada link di bawah ini")
    st.write("https://www.dcode.fr/caesar-cipher")

    st.write("_____________________________________________________________________________________________________________________________________________________________")
    st.header("Enkripsi Modern")
    st.subheader("1.Symmetric Encryption")
    st.markdown("""
Enkripsi adalah konsep kunci dalam kriptografi. Ini adalah proses di mana seseorang dapat menyandikan pesan ke format yang tidak dapat dibaca oleh penyadap. Ini adalah teknik kuno, dan satu kasus penggunaan kuno yang populer ditemukan dalam pesan Caesar, yang dienkripsi menggunakan cipher Caesar. Ini dapat dianggap sebagai suatu transformasi. Pengguna memiliki teks biasa, dan ketika disandikan ke teks sandi, tidak ada penyadap yang dapat mengganggu teks biasa Anda. Setelah diterima oleh penerima yang dituju, ia dapat mendekripsi untuk mendapatkan teks polos asli. Enkripsi digunakan di hampir semua komunikasi jaringan ke berbagai tingkat tanpa sepengetahuan kami. Dulu terbatas pada aplikasi militer dan komunikasi pemerintah, tetapi dengan meluasnya internet baru-baru ini, kebutuhan akan saluran informasi yang aman menjadi yang terpenting, dan enkripsi menjadi solusi utama untuk itu. Ada dua jenis utama enkripsi yang dikenal sebagai Enkripsi Simetri dan Enkripsi Asimetris. Kami akan membandingkan mereka berdampingan satu sama lain hari ini.

Menggunakan satu kunci untuk enkripsi dan dekripsi yang disebut dengan pre-shared key (PSK)

Contoh algoritma:

> AES (Advanced Encryption Standard) - recommended
  Advanced Encryption Standard (AES) adalah algoritma kriptografi yang menjadi standar algoritma enkripsi kunci simetris pada saat ini. Dalam algoritma kriptografi AES 128, 1blok plainteks berukuran 128 bit terlebih dahulu dikonversi menjadi matriks heksadesimal berukuran 4x4 yang disebut state. Setiap elemen state berukuran 1 byte

  coba AES di sini : https://aesencryption.net/
> DES (Data Encryption Standard) - obsolete

> 3DES (Triple Data Encryption Standard) - obsolete

> RC4 (Rivest Cipher 4) - obsolete
""")

    st.write("---------------------------------------------------------------------------------------------------")
    st.subheader("Asymmetric Encryption")
    sa=Image.open("asy.png")
    st.image(sa)
    st.markdown("""
Enkripsi asimetris juga dikenal sebagai kriptografi kunci publik yang merupakan area yang relatif baru dibandingkan dengan enkripsi simetris. Enkripsi asimetris menggunakan dua kunci untuk mengenkripsi teks biasa Anda. Ini datang ke arena untuk mengatasi masalah yang melekat dengan sandi simetris. Jika eavesdropper entah bagaimana mendapatkan kunci rahasia simetris, maka seluruh titik enkripsi dibatalkan. Ini sangat mungkin karena kunci rahasia mungkin harus dikomunikasikan melalui saluran komunikasi yang tidak aman. Sebagai solusi, enkripsi asimetris menggunakan dua kunci di mana satu kunci tersedia untuk umum, dan kunci lainnya adalah pribadi dan hanya diketahui oleh Anda. Bayangkan seseorang ingin mengirimi Anda pesan; dalam skenario itu, Anda akan memiliki kunci rahasia pribadi dan kunci publik yang sesuai untuk itu akan tersedia bagi siapa saja yang mungkin ingin mengirimi Anda pesan terenkripsi. Jadi pengirim mengenkripsi pesan menggunakan kunci publik dan mengubah teks biasa menjadi teks sandi, dan ini hanya dapat didekripsi menggunakan kunci pribadi terkait yang memungkinkan siapapun
mengirimi Anda pesan tanpa harus berbagi kunci rahasia dengan Anda. Jika suatu pesan dienkripsi dengan kunci rahasia, maka itu juga dapat didekripsi dengan kunci publik. Bahkan, enkripsi Asymmetric sebagian besar digunakan dalam saluran komunikasi sehari-hari terutama melalui internet. Algoritma enkripsi kunci asimetris populer termasuk ElGamal, RSA, teknik kurva elips, PGP, SSH dll. 

coba RSA pada link ini :https://www.devglan.com/online-tools/rsa-encryption-decryption 
""")
    st.write("---------------------------------------------------------------------------------------------------")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Hash")
        st.write(""">Teknik kriptografi untuk memastikan integritas dari data,Sifatnya satu arah,Mudah untuk dihitung,Sangat sulit untuk dikembalikan
    """)

    with col2:
        st.header("Contoh :")
        st.write("""
    > SHA256 (Secure Hash Algorithm - 256) - Minimum Recommended
    
    > MD5 (Message Digest 5) - Obsolete
    
    > SHA128
    
    > SHA384
    """)

    with col3:
        st.header("Sifat Dari Hash")
        st.write("""
    > Input bisa sepanjang apapun, namun output panjangnya tetap sama.

    > Hampir mustahil untuk dikembalikan ke bentuk asalnya.

    > Dua jenis input akan selalu menghasilkan nilai hash yang berbeda
    """)
    st.write("_____________________________________________________________________________________________________________________________________________________________")
    col1, col2, col3 = st.columns(3)

    with col1:
       st.header("Salt")
       st.write("""
   > Hash sering digunakan untuk enkripsi password di dalam database.

   > Untuk membuatnya lebih aman, password sering sekali ditambahkan random string sebelum di-hash.
    """)

    with col2:
       st.header("Contoh")
       st.image("https://th.bing.com/th/id/OIP.rjIN5fd5VpMtVnPFSEuy9gHaDV?w=292&h=157&c=7&r=0&o=5&pid=1.7")

    with col3:
        st.header("quest")
        st.caption("""
    > Buka https://emn178.github.io/online-tools/sha256.html

    > Masukkan “password” pada form

    > Copy nilai hash tersebut

    > Masukkan nilai hash tersebut pada https://crackstation.net/

    > Buka kembali https://emn178.github.io/online-tools/sha256.html

    > Tambahkan random karakter setelah “password”

    > Copy nilai hash tersebut

    > Masukkan nilai hash baru pada https://crackstation.net/
    """)
    st.write("_____________________________________________________________________________________________________________________________________________________________")

    st.header("Pertahanan Cyber dan Privasi Data")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Mengamankan Perangkat Pribadi")
        st.write("""
    > Menghapus program yang tidak diperlukan

    > Melakukan update secara rutin

    > Memasang anti-malware

    > Menggunakan VPN saat melakukan koneksi melalui wifi publik
    """)

    with col2:
      st.subheader("Berkaitan dengan VPN")
      st.write("""
    > Pilihlah provider VPN yang terpercaya.

    > VPN provider gratis juga merupakan ancaman.
    """)

    with col3:
       st.subheader("Anti-Malware")
       st.write("""
    > Jangan pernah menggunakan versi bajakan

    > Apabila menggunakan Windows, sudah terdapat Windows Defender

    > Memiliki 2 software anti-malware pada 1 sistem tidak menambah kuat pertahanan dari sistem tersebut.
    """)
    st.write("_____________________________________________________________________________________________________________________________________________________________")

    col1, col2, col3 = st.columns(3)

    with col1:
       st.subheader("Host Firewall")
       st.write("""
    > Firewall yang terpasang pada host tersebut.

    > Mencegah koneksi illegal yang mengarah masuk ke dalam sistem.
    """)

    with col2:
       st.subheader("Update")
       st.write("""
    > Memang terasa merepotkan, namun banyak serangan siber dapat dicegah dengan sekedar mengupdate aplikasi atau sistem operasi.
    """)

    with col3:
        st.subheader("Bahaya Menginstall Aplikasi Bajakan")
        st.write("""
    > Banyak aplikasi bajakan yang disusupi malware.

      >>Adware

      >>Trojan

      >>Crypto-miner

      >>Ransomware

    > Tidak bisa bergantung pada anti-malware saja, kita harus membiasakan diri untuk tidak membajak aplikasi.
    """)
    st.write("_____________________________________________________________________________________________________________________________________________________________")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Keamanan Pada Wireless")
        st.write("""
    > Beberapa standar Wifi:

       >> WEP (Wired Equivalent Privacy) – menggunakan algoritma enkripsi yang tidak aman

       >> WPA / WPA2 / WPA3 (Wi-Fi Protected Access) – sudah menggunakan AES, algoritma enkripsi yang aman.

    > Gunakan koneksi wireless dengan standar keamanan WPA2 atau WPA3.
    """)

    with col2:
       st.subheader("Perlindungan Secara Administratif")
       st.write("""
    > Tidak menggunakan administrator account untuk pekerjaan sehari-hari

    > Menghapus aplikasi yang sudah tidak terpakai

    > Menggunakan firewall untuk

      >> Menutup port yang tidak terpakai

      >>Menutup layanan yang tidak membutuhkan komunikasi melalui jaringan.
    """)

    with col3:
        st.subheader("Perlindungan Fisik Perangkat")
        st.write("""
   >  Cable locks untuk mengamankan perangkat supaya tidak tercuri.

   >  Memastikan ruangan tetap terkunci

   >  Logout timer

   > Anti-glare pada layer

   >  CCTV
    """)
  
    st.write("_____________________________________________________________________________________________________________________________________________________________")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Keamanan pada Data Center – Man Trap")
        st.write("""
   > Menerapkan autentikasi 2 faktor pada akses lokasi.

   > Terdiri dari dua pintu:

      >> Pintu pertama dibuka dengan kartu RFID

      >> Pintu kedua dibuka dengan sidik jari
    """)

    with col2:
        st.subheader("Perlindungan Fisik Perangkat - Availability")
        st.write("""
    > Menyediakan sumber daya listrik cadangan

       >> UPS

       >> Genset

    > Heating, Ventilation, and Air Conditioning (HVAC)
    """)

    with col3:
       st.subheader("Two-Factor Authentication")
       st.write("""
> Two Factor Authentication (2FA) / Multi Factor Authentication (MFA) adalah teknik autentikasi dengan menggunakan beberapa faktor, yaitu:

    >> Something you know

    >> Something you have

    >> Something you are

> Note: 2FA ini harus menggunakan faktor yang berbeda. Contoh: dua autentikasi something you know tidak bisa menjadi 2FA.
    """)




if selected == "Video Reference":
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    st.markdown("""
   <!-- As a heading -->
   <nav class="navbar" style="background-color :#310AC5" >
  <div class="container-fluid">
    <h1 class="text-white"style="alight:text-center">Video Reference</h2>
   </div>
   </nav>
    """, unsafe_allow_html=True)

    st.header("what's cyber security")
    video_file = open("what's cyber security.mp4", 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

    st.header("Prinsip Dasar")
    video_file = open("prinsip dasar.mp4", 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

    st.header("Jenis Hacker")
    video_file = open("jenis hacker.mp4", 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

    st.header("Introduction To Cyber")
    video_file = open("Introduction To Cyber Security _ Cyber Security Training For Beginners _ CyberSecurity _ Simplilearn.mp4", 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

    st.header("Cryptography")
    video_file = open("Cryptography Full Course _ Cryptography And Network Security _ Cryptography _ Simplilearn.mp4", 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

    
    st.header("Password Management")
    video_file = open("Animasi Cyber Security Awareness _ Password Management.mp4", 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
        

   
   
    
  
  


if selected == "Exam":
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    st.markdown("""
   <!-- As a heading -->
   <nav class="navbar" style="background-color :#310AC5" >
  <div class="container-fluid">
    <h1 class="text-white"style="alight:text-center">EXAM</h2>
   </div>
   </nav>
    """, unsafe_allow_html=True)
    st.subheader(f'WELCOME TO LEARN CS ')
    option = st.selectbox(
     'Untuk melatih Pemahaman kamu tentang Cyber Security Mari kerjakan Latihan soal ini',
     ['Pilih','Exam1', 'Exam2', 'Exam3','Exam4','Exam5'])
    if option== "Pilih":
        st.write("_")
    elif option == "Exam1":
        genre = st.radio(
        "1.Keamanan informasi yang di aplikasikan kepada komputer dan jaringan adalah...",
     ('Cyber Security', 'Malware', 'Cyber Crime'))
       
        dada = st.radio(
        "2. Sebutkan Jenis -jenis hacker yang benar yaitu",
     ('Black hat-grey hat-white hat','black hat-white hat-brown hat','white hat-grey hat - red hat'))

        caca=st.radio(
            "3.Hacker Jenis Mana Yang di sebut Cyber Criminal",
            ('grey hat','red hat','black hat')
        )

        dudu=st.radio(
            "4. Yang serng disebut enthical hacker adalah ....",
            ('white hat','brown hat','grey hat')
        )

        dede=st.radio(
            "5. Apa itu Trias CIA?",
            ('tiga konsep dasar cyber crime','tiga konsep dasar cyber security','tiga larangan bagi hacker')
        )
        
        if  st.button('Submit'):


                if genre == "Cyber Security":
                    nilai=20
                    st.write("1.Keamanan informasi yang di aplikasikan kepada komputer dan jaringan adalah...","(",genre,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("1.Keamanan informasi yang di aplikasikan kepada komputer dan jaringan adalah...","(",genre,")",":",nilai,":cry:")

                
                if dada == "'Black hat-grey hat-white hat'":
                    nilai=20
                    st.write("2. Sebutkan Jenis -jenis hacker yang benar yaitu","(",dada,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("2. Sebutkan Jenis -jenis hacker yang benar yaitu","(",dada,")",":",nilai,":cry:")


                
                if caca == "black hat":
                    nilai=20
                    st.write("3.Hacker Jenis Mana Yang di sebut Cyber Criminal","(",caca,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("3.Hacker Jenis Mana Yang di sebut Cyber Criminal","(",caca,")",":",nilai,":cry:")

                
                
                if dudu == "white hat":
                    nilai=20
                    st.write( "4. Yang serng disebut enthical hacker adalah ....","(",dudu,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write( "4. Yang serng disebut enthical hacker adalah ....","(",dudu,")",":",nilai,":cry:")



                
                if dede == "tiga konsep dasar cyber security":
                    nilai=20
                    st.write("5. Apa itu Trias CIA?","(",dede,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("5. Apa itu Trias CIA?","(",dede,")",":",nilai,":cry:")


                    st.balloons()

    elif option == "Exam2":
        genre = st.radio(
        "1.Berikut ini yang benar tentang isi dari Trias CIA ",
     ('integrity,confidentially,fundamental', 'confidentially,integrity,avalability', 'confidentially,avalability,fundamental'))
       
        dada = st.radio(
        "2.ada berapa elemen pokok cyber security?",
     (7,10,6))

        caca=st.radio(
            "3.kriptologi berasal dari bahasa",
            ('Yunani','inggris','latin')
        )

        dudu=st.radio(
            "4.berikut ini yang benar tentang aplikasi dari kriptograpi",
            ('Kalkulator,ATM,E-commerce','ATM,E-commerce,password komputer','ATM,password komputer,Kalkulator')
        )

        dede=st.radio(
            "5.Salah satu algoritma tertua dan paling diketahui  dalam perkembangan kriptograpi adalah",
            ('symmetric encryption','Caesar Chipher','AES')
        )
        
        if  st.button('Submit'):


                if genre == "confidentially,integrity,avalability":
                    nilai=20
                    st.write("1.Berikut ini yang benar tentang isi dari Trias CIA ","(",genre,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("1.Berikut ini yang benar tentang isi dari Trias CIA ","(",genre,")",":",nilai,":cry:")

                
                if dada == 6:
                    nilai=20
                    st.write("2.ada berapa elemen pokok cyber security?","(",dada,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("2.ada berapa elemen pokok cyber security?","(",dada,")",":",nilai,":cry:")


                
                if caca == "Yunani":
                    nilai=20
                    st.write("3.kriptologi berasal dari bahasa","(",caca,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("3.kriptologi berasal dari bahasa","(",caca,")",":",nilai,":cry:")

                
                
                if dudu == "ATM,E-commerce,password komputer":
                    nilai=20
                    st.write("4.berikut ini yang benar tentang aplikasi dari kriptograpi","(",dudu,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("4.berikut ini yang benar tentang aplikasi dari kriptograpi","(",dudu,")",":",nilai,":cry:")



                
                if dede == "Caesar Chipher":
                    nilai=20
                    st.write("5.Salah satu algoritma tertua dan paling diketahui  dalam perkembangan kriptograpi adalah","(",dede,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("5.Salah satu algoritma tertua dan paling diketahui  dalam perkembangan kriptograpi adalah","(",dede,")",":",nilai,":cry:")


                st.balloons()

    elif option == "Exam3":
        genre = st.radio(
        "1.ete oefev erhe,descript teks di samping menggunakan subtitution Chipher?",
     ('apa anda baik hari ini', 'apa kabar anda', 'siapa nama anda'))
       
        dada = st.radio(
       "2.Apa prinsip Utama subtitution Chipher ?",
        ('menukarkan setiap huruf dengan plainteks dengan sesuatu','menambahkan setiap huruf dengan plainteks dengan sesuatu','menambahkan setiap huruf dengan plainteks dengan sesuatu'))
        caca=st.radio(
            "3.Yang termasuk enkripsi modern adalah",
           ('symmetric encryption & caesar chipher','asymmtric encryption & substitution chipher','asymmtric encryption & symmetric encryption'))

        

        dudu=st.radio(
           "4.apa kepanjangan dari AES?",
            ('Asian East Security','advanced encryption standard','american encryption standard')
        )

        dede=st.radio(
            "5. Decrypt kode ini A01sgutIhUoLKE0jlvvZbf+GPxDXm3wJXz3SHBwhtPs=  mengunakan AES",
            ('ayo belajar cyber hakcer','aku senang belajar cyber security','ayo belajar cyber security')
        )
        
        if  st.button('Submit'):


                if genre == "apa kabar anda":
                    nilai=20
                    st.write("1.ete oefev erhe,descript teks di samping menggunakan subtitution Chipher?","(",genre,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("1.ete oefev erhe,descript teks di samping menggunakan subtitution Chipher?","(",genre,")",":",nilai,":cry:")

                
                if dada == "menukarkan setiap huruf dengan plainteks dengan sesuatu ":
                    nilai=20
                    st.write("2.Apa prinsip Utama subtitution Chipher ?","(",dada,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("2.Apa prinsip Utama subtitution Chipher ?","(",dada,")",":",nilai,":cry:")


                
                if caca == "asymmtric encryption & symmetric encryption":
                    nilai=20
                    st.write("3.Yang termasuk enkripsi modern adalah","(",caca,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("3.Yang termasuk enkripsi modern adalah","(",caca,")",":",nilai,":cry:")

                
                
                if dudu == "advanced encryption standard":
                    nilai=20
                    st.write("4.apa kepanjangan dari AES?","(",dudu,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("4.apa kepanjangan dari AES?","(",dudu,")",":",nilai,":cry:")



                
                if dede == "ayo belajar cyber security":
                    nilai=20
                    st.write("5. Decrypt kode ini A01sgutIhUoLKE0jlvvZbf+GPxDXm3wJXz3SHBwhtPs= mengunakan AES","(",dede,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("5. Decrypt kode ini A01sgutIhUoLKE0jlvvZbf+GPxDXm3wJXz3SHBwhtPs= mengunakan AES","(",dede,")",":",nilai,":cry:")


                    st.balloons()


    elif option == "Exam4":
        genre = st.radio(
        "1.RSA meiliki 2 key type yaitu",
     ('encript key & Public key ', 'private key & encript key', 'Public key & private key'))
       
        dada = st.radio(
        "2. yang termasuk contoh dari hash adalah?",
     ('Encrpt','MD5','SHA27'))

        caca=st.radio(
            "3.yang termasuk sifat dari hash adalah",
            ('dua jenis input akamenghaslkan nilai hash yang berbeda','dua jenis input akamenghaslkan nilai hash yang sama','bisa di kembalikanke bentuk semula')
        )

        dudu=st.radio(
            "4.contoh pertahana cyber yang berkaitan dengan VPN",
            ('pih provider VPN gratis','pilih provider VPN terpercaya','Gunakan VPN yang sedang viral')
        )

        dede=st.radio(
            "5.yang tidak termasuk mengamankan perangkat pribadi yaitu",
            ('menghapus program yang tidak di pakai','memasang anti malware','memasag VPN')
        )
        
        if  st.button('Submit'):


                if genre == "Public key & private key":
                    nilai=20
                    st.write("1.RSA meiliki 2 key type yaitu","(",genre,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("1.RSA meiliki 2 key type yaitu","(",genre,")",":",nilai,":cry:")

                
                if dada == "MD5":
                    nilai=20
                    st.write("2. yang termasuk contoh dari hash adalah?","(",dada,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("2. yang termasuk contoh dari hash adalah?","(",dada,")",":",nilai,":cry:")


                
                if caca == "dua jenis input akamenghaslkan nilai hash yang berbeda":
                    nilai=20
                    st.write("3.yang termasuk sifat dari hash adalah","(",caca,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("3.yang termasuk sifat dari hash adalah","(",caca,")",":",nilai,":cry:")

                
                
                if dudu == "pilih provider VPN terpercaya":
                    nilai=20
                    st.write("4.contoh pertahana cyber yang berkaitan dengan VPN","(",dudu,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("4.contoh pertahana cyber yang berkaitan dengan VPN","(",dudu,")",":",nilai,":cry:")



                
                if dede == "memasag VPN":
                    nilai=20
                    st.write("5.yang tidak termasuk mengamankan perangkat pribadi yaitu","(",dede,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("5.yang tidak termasuk mengamankan perangkat pribadi yaitu","(",dede,")",":",nilai,":cry:")


                    st.balloons()


    elif option == "Exam5":
        genre = st.radio(
        "1.berikut salah satu faktor MFA adalah",
     ('someting you know', 'something you says', 'something you buy'))
       
        dada = st.radio(
        "2.mengapa kita harus mengupdate aplikasi?",
     ('agar bisa menuggunaka fitur terbaru','mencegah serangan cyber','agar tidak tertinggal trend'))

        caca=st.radio(
            "3.agar wireless aman kita harus menggunakan standard keamanan yang..,",
            ('WAP','WEP','WPA3')
        )

        dudu=st.radio(
            "4.mengapa kita harus menggunakan cable locks untuk laptop?",
            ('agar data kita tidak di curi','mengikuti trend','terindar dari debu')
        )

        dede=st.radio(
            "5.yang tidak termasuk hash adalah",
            ('SHA256','SHA384','SHA385')
        )
        
        if  st.button('Submit'):


                if genre == "something you know":
                    nilai=20
                    st.write("1.What's your favorite movie genre?","(",genre,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("1.What's your favorite movie genre?","(",genre,")",":",nilai,":cry:")

                
                if dada == "mencegah seraga cyber":
                    nilai=20
                    st.write("2.Who are you?","(",dada,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("2.Who are you?","(",dada,")",":",nilai,":cry:")


                
                if caca == "WPA3":
                    nilai=20
                    st.write("3.who am i?","(",caca,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("3.who am i?","(",caca,")",":",nilai,":cry:")

                
                
                if dudu == "agar data kita tidak d curi":
                    nilai=20
                    st.write("4.Where do you live?","(",dudu,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("4.where do you live?","(",dudu,")",":",nilai,":cry:")



                
                if dede == "SHA385":
                    nilai=20
                    st.write("5.are you boring?","(",dede,")",":",nilai,":smile:")
                else:
                    nilai=0
                    st.write("5.are you boring?","(",dede,")",":",nilai,":cry:")


                    st.balloons()
                
               
               
        
                    


        

                
               
               
        
                    


        

                
               
               
        
                    


        

                
               
               
        
                    


        

                

         
               
        
                    


        

           

           
            
   