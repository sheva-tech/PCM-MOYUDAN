# Website PCM Moyudan

Tugas *Pemrograman Web berbasis Framework (TIF1336)*. Website Pimpinan Cabang Muhammadiyah (PCM) Moyudan, Sleman, DIY, dibangun dengan Django 6.

> Website ini dibuat untuk tugas kuliah, bukan website resmi PCM Moyudan. Situs resmi: https://muhammadiyahmoyudan.or.id

## Kelompok
Nama kelompok: O

| Nama | NIM |
|---|---|
| Afifa Najwa Azzahra | L200240174 |
| Ahmad Zacky Syafa | L200240187 |
| Sheva Rosa Mardiyah | L200240196 |
| Mohammad Dawid Hafizal | L200240235 |
| Nayla Putri Anjani Mahardani | L200240236 |


## PCM yang dipilih
PCM Moyudan, Kapanewon Moyudan, Kabupaten Sleman, DI Yogyakarta.
Pengurus yang memberi izin (foto/data):  ("belum ada")

### Sumber data
| Data | Sumber | Tanggal diambil |
|---|---|---|
| Susunan pimpinan 2022–2027 | https://muhammadiyahmoyudan.or.id/pcm/ | 14 Nov 2026 |
| Foto pengurus (hero) | https://muhammadiyahmoyudan.or.id/pcm/ (dokumentasi PCM) | 14 Nov 2026 |
| Nama amal usaha | Halaman program kerja PCM + prosiding UMY (SMP Muhammadiyah 1 Moyudan) | 14 Nov 2026 |
| Ranting, sejarah, visi-misi, alamat, berita, agenda | (isi setelah dikumpulkan) | (isi) |

Data yang belum tersedia ditampilkan "belum tersedia", tidak dikarang. Tidak ada data pribadi (HP/alamat rumah/NIK) yang ditampilkan.

## Kontribusi anggota
| Anggota | Pekerjaan |
|---|---|
| Afifa Najwa Azzahra (L200240174) | Seed, test, Docker, dokumentasi |
| Ahmad Zacky Syafa (L200240187) | Model dan admin |
| Sheva Rosa Mardiyah (L200240196) | Setup dan konfigurasi |
| Mohammad Dawid Hafizal (L200240235) | Template dan tampilan |
| Nayla Putri Anjani Mahardani (L200240236) | View, URL, form |

## Menjalankan di laptop (uv)
bash
cp .env.example .env
uv sync
uv run python manage.py migrate
uv run python manage.py seed_pcm
uv run python manage.py createsuperuser
uv run python manage.py test
uv run python manage.py runserver     # http://127.0.0.1:8000

Letakkan logo Muhammadiyah (Wikimedia Commons, CC BY-SA 4.0) di static/img/logo-muhammadiyah.svg.

## Menjalankan dengan Docker
bash
docker compose up --build             # http://localhost:8000
docker compose exec web uv run python manage.py seed_pcm
docker compose exec web uv run python manage.py createsuperuser

- docker compose down menghentikan container; data (volume pgdata) dan gambar unggahan (volume media) tetap ada.
- docker compose down -v ikut *menghapus volume*, sehingga database dan gambar hilang. Gunakan hanya untuk mulai dari nol.

## Produksi
- URL: (isi)
- Platform: Render (Docker, render.yaml) · Database: Neon/Supabase PostgreSQL · Media: Supabase Storage (S3). Alasan: (isi)
- Media di platform tidak permanen, jadi gambar unggahan disimpan di object storage lewat django-storages (aktif jika AWS_STORAGE_BUCKET_NAME diisi).
- Pooler mode transaction (Supabase :6543 / Neon -pooler) terdeteksi otomatis: DISABLE_SERVER_SIDE_CURSORS=True, CONN_MAX_AGE=0. Jalankan migrasi lewat koneksi direct bila memakai Neon.
- Setelah deploy: python manage.py seed_pcm dengan DATABASE_URL produksi (dari laptop).

## Environment variable
Lihat .env.example. Wajib di produksi: SECRET_KEY, DEBUG=False, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS, DATABASE_URL, serta variabel AWS_* untuk storage.

## Akun admin demo
Dikirim terpisah (tidak di-commit).