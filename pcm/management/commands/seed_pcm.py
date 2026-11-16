
from django.core.management.base import BaseCommand

from pcm.models import (
    Profil,
    Pimpinan,
    Ranting,
    AmalUsaha,
    TautanTerkait,
)


class Command(BaseCommand):
    help = "Memasukkan data awal PCM Moyudan"

    def handle(self, *args, **options):

        # 1. Profil PCM
        if not Profil.objects.exists():
            Profil.objects.create(
                nama="Pimpinan Cabang Muhammadiyah Moyudan",
                nama_singkat="PCM Moyudan",
                tagline="Portal resmi Muhammadiyah Moyudan",
                tentang=(
                    "Portal informasi perkembangan dan kegiatan "
                    "Muhammadiyah Moyudan."
                ),
                sejarah=(
                    "Gerakan Muhammadiyah di Moyudan diperkenalkan "
                    "oleh Kiai Amir pada tahun 1924. Pada tahun 1927 "
                    "Muhammadiyah berkembang di Kedungbanteng. "
                    "Cabang Moyudan diakui secara administratif "
                    "pada 16 Oktober 1961 melalui SK PP Muhammadiyah "
                    "Nomor 1517/A."
                ),
            )

        # 2. Data pimpinan periode 2022-2027
        pimpinan_data = [
            ("Drs. H. Abdullah Effendi", "Penasehat", "Penasehat"),
            ("H. Sudiyana Irsyad", "Penasehat", "Penasehat"),
            ("Ngadi Susilo, BA", "Penasehat", "Penasehat"),
            ("Dr. H. Zainudin Akhid", "Penasehat", "Penasehat"),
            ("H. Abu Hanifah, S.Ag, MSI", "Ketua", "Pengurus Inti"),
            ("Drs. H. Suisdialwan, MA", "Wakil Ketua 1", "Pengurus Inti"),
            ("H. Imam Triyono, S.Ag, M.Si", "Wakil Ketua 2", "Pengurus Inti"),
            ("Drs. H. Sarjono, M.Si", "Wakil Ketua 3", "Pengurus Inti"),
            ("H. Abu Yazid, SIP, MM", "Wakil Ketua 4", "Pengurus Inti"),
            ("H. Heru Suprayitno, S.Ag", "Sekretaris", "Pengurus Inti"),
            ("Haris Bahalwan, S.Ag", "Wakil Sekretaris", "Pengurus Inti"),
            ("Drs. H. Suharyanto, MA", "Bendahara", "Pengurus Inti"),
            ("Difa Nuarisapta, S.Pd", "Wakil Bendahara", "Pengurus Inti"),
        ]

        for urutan, (nama, jabatan, bagian) in enumerate(pimpinan_data, 1):
            Pimpinan.objects.get_or_create(
                nama=nama,
                jabatan=jabatan,
                bagian=bagian,
                defaults={
                    "periode": "2022-2027",
                    "urutan": urutan,
                },
            )

        # 3. Data ranting Muhammadiyah Moyudan
        ranting_data = [
            ("Klampis", "Sargino, S.Pd", "Klampis, Sumberrahayu"),
            ("Betakan", "Hafidludin Muhammad, SIP", "Betakan, Sumberrahayu"),
            ("Kembangan", "Drs. Atang Basuki", "Kembangan, Sumberrahayu"),
            ("Dagen", "Nurudin, SE.", "Dagen, Sumberrahayu"),
            ("Karangkemasan", "Widodo, S.T., MT.", "Karangkemasan, Sumberrahayu"),
            ("Barepan", "Ir. H. Kusnu Martoyo, M.Sc, QIA", "Barepan, Sumberrahayu"),
            ("Pandulan Saren", "Heri Maryadi", "Pendulan, Sumberagung"),
            ("Gamplong", "Drs. Agung Hidayat", "Gamplong, Sumberrahayu"),
            ("Sangubanyu", "Muh. Rifqi", "Sangubanyu, Sumberrahayu"),
            ("Bendosari", "Ir. Nursalim", "Barosan, Sumberrahayu"),
            ("Ngaglik", "Drs. Sunardi", "Ngaglik, Sumbersari"),
            ("Tiwir", "Drs. Sumarsam", "Menulis, Sumbersari"),
            ("Sombangan", "Anton Rahmat Widodo, S.T., M.T.", "Sombangan, Sumbersari"),
            ("Semingin Nasri", "Ilham", "Semingin, Sumbersari"),
            ("Tegal Patran", "Muhammad Zamroni", "Patran, Sumbersari"),
            ("Klisat", "Asrowi, S.Pd.I", "Klisat, Sumbersari"),
            ("Kedungbanteng", "Ahmad Ghozi, SE", "Kedungbanteng, Sumberagung"),
            ("Ngentak", "Soffan", "Ngentak, Sumberagung"),
            ("Nulisan", "Drs. Muh. Farid Fauzi", "Nulisan, Sumberagung"),
            ("Gedongan", "H. Muh. Qosim Ausath, S.Ag", "Gedongan, Sumberagung"),
            ("Tegal Ngijon", "Jamil Rifanto, SE. MM.", "Tegal Ngijon, Sumberagung"),
            ("Pucanganom", "Suparyanto, S.Pd.I", "Pucanganom, Sumberagung"),
            ("Jowahan", "H. Marsudi", "Jowahan, Sumberagung"),
            ("Kaliduren Utara", "Maksum", "Kaliduren 2, Sumberagung"),
            ("Kaliduren Selatan", "Niko Agung Kuncoro", "Kaliduren 1, Sumberagung"),
            ("Papringan Gatak", "Basuki", "Papringan Gatak, Sumberagung"),
            ("Karang", "Tri Haryanto, SE.", "Karang, Sumberagung"),
            ("Sermo", "H. Mardi, M.Pd.", "Sermo, Sumberagung"),
            ("Sumberarum", "H. Yulianto, M.Pd.", "Karanganjir, Sumberagung"),
        ]

        for nama, ketua, alamat in ranting_data:
            Ranting.objects.get_or_create(
                nama=nama,
                defaults={
                    "ketua": ketua,
                    "alamat": alamat,
                },
            )

        # 4. Data amal usaha bidang pendidikan
        amal_usaha_data = [
            ("TK ABA Turgenen", "Turgenen, Sumberagung"),
            ("TK ABA Saren", "Saren, Sumberrahayu"),
            ("TK ABA Mergan", "Mergan, Sumberagung"),
            ("TK ABA Barepan", "Barepan, Sumberrahayu"),
            ("TK ABA Kembangan", "Kembangan II, Sumberrahayu"),
            ("TK ABA Kaliduren", "Kaliduren II, Sumberagung"),
            ("TK ABA Sermo", "Sermo, Sumberarum"),
            ("TK ABA Gamplong", "Gamplong IV, Sumberrahayu"),
            ("TPA 'Aisyiyah Ananda", "Moyudan, Sumberrahayu"),
            ("KB 'Aisyiyah Ananda", "Moyudan, Sumberrahayu"),
            ("KB 'Aisyiyah Arum Sari", "Gesikan, Sumbersari"),
            ("SPS 'Aisyiyah Mawar", "Betakan, Sumberrahayu"),
            ("TAA 'Aisyiyah Ananda", "Moyudan, Sumberrahayu"),
            ("SPS 'Aisyiyah Mentari", "Moyudan"),
            ("SD Muhammadiyah Kedungbanteng 1", "Kedungbanteng, Sumberagung"),
            ("SD Muhammadiyah Saren", "Saren, Sumberrahayu"),
            ("SD Muhammadiyah Karanganjir", "Karanganjir, Sumberarum"),
            ("SD Muhammadiyah Semingin", "Sumbersari"),
            ("SD Muhammadiyah Ngijon 2", "Sermo, Sumberarum"),
            ("SD Muhammadiyah Kedungbanteng 2", "Bendosari, Sumbersari"),
            ("SD Muhammadiyah Gamplong", "Gamplong, Sumberrahayu"),
            ("SD Muhammadiyah Ngijon 1", "Turgenen, Sumberagung"),
            ("SMK Muhammadiyah 1 Moyudan", "Gedongan, Sumberagung"),
            ("SMK Muhammadiyah 2 Moyudan", "Ngentak, Sumberagung"),
            ("SMP Muhammadiyah 1 Moyudan", "Barepan, Sumberrahayu"),
        ]

        for nama, alamat in amal_usaha_data:
            AmalUsaha.objects.get_or_create(
                nama=nama,
                defaults={
                    "bidang": AmalUsaha.Bidang.PENDIDIKAN,
                    "alamat": alamat,
                    "deskripsi": "Lembaga pendidikan Muhammadiyah dan Aisyiyah di Moyudan.",
                },
            )

        # 5. Tautan resmi
        TautanTerkait.objects.get_or_create(
            nama="Website Muhammadiyah Moyudan",
            defaults={
                "url": "https://muhammadiyahmoyudan.or.id/",
                "urutan": 1,
            },
        )

        self.stdout.write(
            self.style.SUCCESS("Data awal PCM Moyudan berhasil disiapkan.")
        )
