# EmailSpoof

______________
Membuat dan mengirimkan EMAIL palsu.

_____________________________________

## <a id="getting-started">Menginstall</a>

   - `$ git clone https://github.com/GLoriusHeLL666/EmailSpoof.git` 
   - Activate `$ virtualenv` 
   - `$ pip install -r requirements.txt` 
   - `$ python3 spoof.py` 

 Petunjuk untuk membuat dan mengaktifkan virtualenv dapat ditemukan di sini: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

--------------------

## <a id="commands">Perintah</a>

   EmailSpoof mempunyai dua perintah: [`wizard`](#wizard) dan [`cli`](#cli):
    
    
    $ python3 spoof.py -h
    usage: spoof.py [-h] {wizard,cli} ...

    optional arguments:
    -h, --help    tampilkan pesan bantuan ini dan keluar

    perintah:
      {wizard,cli}  Perintah yang di izinkan
        wizard      Tetap mengikuti panduan
        cli         Lewati argument secara teliti
   
   Cth: `$ python3 spoof.py cli` ..........
     
-----------------

### <a id="cli">CLI</a>

   perintah `cli -h` untuk melihat bantuan:
  
      $ python3 spoof.py cli -h
      usage: spoof.py cli [-h] (--noauth | --username USERNAME)
                          [--password PASSWORD] --host HOST --port PORT --sender
                          PENGIRIM --name NAMA --recipients Email Tujuan
                          [Email Tujuan ...] --subject SUBJECT --filename NamaFile

      optional arguments:
        -h, --help            Tampilkan pesan bantuan ini dan keluar
        --noauth              Nonaktifkan pemeriksaan authentication
        --username USERNAME   SMTP username
        --password PASSWORD   SMTP password (bersama --username)

      required arguments:
        --host HOST           SMTP hostname
        --port PORT           SMTP nomor port
        --sender SENDER       Email pengirim (Cth. bintangbokep@domain.com)
        --name NAME           Nama pengirim (Cth. GLorius HeLL)
        --recipients RECIPIENTS [RECIPIENTS ...]
                              Email Tujuan (Cth. masihperawan@domain.com ...)
        --subject SUBJECT     Subject line
        --filename FILENAME   Isi pesan (Cth. contoh.html)
        
        
  Keluarkan perintah cli bersama dengan argumen yang sesuai:
    Jika `--noauth` tidak ditentukan, `--username` dan `--password` diperlukan.
   
      Cth:python3 spoof.py cli --username SMTP username --password SMTP password --host SMTP hostname --port SMTP port --sender bintangbokep@domain.com --name GLoriusHeLL --recipients masihperawan@domain.com --subject test --filename contoh.html
--------------------
### <a id="wizard">Wizard</a>
  Wizard untuk sementara tidak bisa...!!!
