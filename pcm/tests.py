from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Agenda, Berita, PesanMasuk


class HalamanPublikTests(TestCase):
    def test_semua_halaman_publik_dapat_diakses(self):
        names = [
            "pcm:beranda",
            "pcm:profil",
            "pcm:pimpinan",
            "pcm:ranting",
            "pcm:amal_usaha",
            "pcm:berita_list",
            "pcm:agenda",
            "pcm:unduhan",
            "pcm:kontak",
        ]
        for name in names:
            with self.subTest(url=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)


class BeritaTests(TestCase):
    def create_news(self, **overrides):
        data = {
            "judul": "Berita Uji Coba",
            "ringkasan": "Ringkasan berita untuk pengujian.",
            "isi": "Isi berita untuk pengujian sistem.",
            "tanggal_terbit": timezone.now() - timedelta(days=1),
            "status": Berita.Status.TERBIT,
        }
        data.update(overrides)
        return Berita.objects.create(**data)

    def test_slug_dibuat_otomatis_dan_unik(self):
        first = self.create_news()
        second = self.create_news()
        self.assertEqual(first.slug, "berita-uji-coba")
        self.assertEqual(second.slug, "berita-uji-coba-2")

    def test_daftar_berita_hanya_menampilkan_berita_terbit(self):
        published = self.create_news(judul="Berita yang Terbit")
        draft = self.create_news(
            judul="Berita yang Masih Draf",
            status=Berita.Status.DRAF,
        )
        response = self.client.get(reverse("pcm:berita_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, published.judul)
        self.assertNotContains(response, draft.judul)

    def test_pencarian_berita(self):
        match = self.create_news(judul="Kegiatan Bakti Sosial")
        no_match = self.create_news(judul="Informasi Pendidikan")
        response = self.client.get(
            reverse("pcm:berita_list"), {"q": "Bakti Sosial"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, match.judul)
        self.assertNotContains(response, no_match.judul)

    def test_detail_berita_terbit_dapat_dibuka(self):
        news = self.create_news(judul="Berita Detail")
        response = self.client.get(
            reverse("pcm:berita_detail", kwargs={"slug": news.slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, news.judul)

    def test_detail_berita_draf_menghasilkan_404(self):
        news = self.create_news(
            judul="Berita Rahasia",
            status=Berita.Status.DRAF,
        )
        response = self.client.get(
            reverse("pcm:berita_detail", kwargs={"slug": news.slug})
        )
        self.assertEqual(response.status_code, 404)


class AgendaTests(TestCase):
    def test_agenda_mendatang_dan_terlaksana_ditampilkan(self):
        upcoming = Agenda.objects.create(
            nama_kegiatan="Agenda Mendatang",
            waktu_mulai=timezone.now() + timedelta(days=2),
            tempat="Moyudan",
        )
        past = Agenda.objects.create(
            nama_kegiatan="Agenda Terlaksana",
            waktu_mulai=timezone.now() - timedelta(days=2),
            tempat="Moyudan",
        )
        response = self.client.get(reverse("pcm:agenda"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, upcoming.nama_kegiatan)
        self.assertContains(response, past.nama_kegiatan)


class KontakTests(TestCase):
    def test_form_kontak_valid_menyimpan_pesan(self):
        response = self.client.post(
            reverse("pcm:kontak"),
            {
                "nama": "Pengunjung Uji",
                "email": "pengunjung@example.com",
                "subjek": "Pertanyaan kegiatan",
                "pesan": "Saya ingin mengetahui informasi kegiatan PCM Moyudan.",
            },
        )
        self.assertRedirects(response, reverse("pcm:kontak"))
        self.assertEqual(PesanMasuk.objects.count(), 1)
        message = PesanMasuk.objects.get()
        self.assertEqual(message.nama, "Pengunjung Uji")
        self.assertEqual(message.email, "pengunjung@example.com")

    def test_form_kontak_menolak_pesan_terlalu_pendek(self):
        response = self.client.post(
            reverse("pcm:kontak"),
            {
                "nama": "Pengunjung Uji",
                "email": "pengunjung@example.com",
                "subjek": "Pertanyaan",
                "pesan": "Pendek",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(PesanMasuk.objects.count(), 0)
