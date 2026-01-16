# hal-hal yang ku pelajari selama praktek di folder ini

15-jan-2026
1. response.json() tidak hanya mengembalikan tipe data dict(JSON OBJECT) ,bisa list(JSON ARRAY), string ,int ,bool ,atau bahkan json null 
**TIPS**
- selalu baca dokumentasi untuk mengetahui struktur response nya 
- gunakan type() untuk debugging
- siapkan handling jika api response tidak konsisten
- gunakan try except 

16-jan-2026
2. data=dataku dengan json=dataku dalam parameter requests adalah hal yg berbeda ,aku mencoba mengirim data di github api dengan parameter data=dataku dan gagal ,json lebih universal 
