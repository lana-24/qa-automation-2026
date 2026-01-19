# hal-hal yang ku pelajari selama praktek di folder ini

15-jan-2026 
## response json 
1. response.json() tidak hanya mengembalikan tipe data dict(JSON OBJECT) ,bisa list(JSON ARRAY), string ,int ,bool ,atau bahkan json null 
**TIPS**
- selalu baca dokumentasi untuk mengetahui struktur response nya 
- gunakan type() untuk debugging
- siapkan handling jika api response tidak konsisten
- gunakan try except 

16-jan-2026
## perbedaan parameter dalam method requests post
2. data=dataku dengan json=dataku dalam parameter requests adalah hal yg berbeda ,aku mencoba mengirim data di github api dengan parameter data=dataku dan gagal ,json lebih universal 

18-jan-2026
## except exception vs except {spesifik}
3. jika ada dua def dengan try except ,satu def except spesifik dan satu general atau exception ,ketika def general mengirim data ke def except spesifik ,ketika terjadi error yg tidak di tangkap except di dalam def spesifik ,maka akan di tangkap oleh def general(pemanggil)
**TIPS**
- gunakan except spesifik setiap kondisi tertentu jika error bisa di prediksi ,pakai exception ketika dalam gerbang terakhir atau error yang tidak di inginkan 

4. ketika menjalankan script requests dan tiba-tiba internet lemot atau mati ,stuck deh 
**TIPS**
- gunakan parameter timeout(waktu connect  ,waktu baca ) di requests
- gunakan try except Timeout dan ConnectionError

