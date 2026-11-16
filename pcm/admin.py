from django.contrib import admin

from .models import (
    Agenda, AmalUsaha, Berita, Dokumen, Pimpinan, PesanMasuk, Profil, Ranting, TautanTerkait,
)

admin.site.site_header = "Admin Website PCM Moyudan"
admin.site.site_title = "Admin PCM Moyudan"
admin.site.index_title = "Kelola konten website"


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ("nama", "nama_singkat", "telepon", "email", "jumlah_anggota_ktam")

    def has_add_permission(self, request):
        return not Profil.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Pimpinan)
class PimpinanAdmin(admin.ModelAdmin):
    list_display = ("nama", "jabatan", "bagian", "periode", "urutan")
    list_filter = ("bagian", "periode")
    search_fields = ("nama", "jabatan")
    list_editable = ("urutan",)


@admin.register(Ranting)
class RantingAdmin(admin.ModelAdmin):
    list_display = ("nama", "ketua", "telepon")
    search_fields = ("nama", "ketua")


@admin.register(AmalUsaha)
class AmalUsahaAdmin(admin.ModelAdmin):
    list_display = ("nama", "bidang", "alamat")
    list_filter = ("bidang",)
    search_fields = ("nama", "deskripsi")


@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ("judul", "status", "tanggal_terbit")
    list_filter = ("status",)
    search_fields = ("judul", "ringkasan", "isi")
    prepopulated_fields = {"slug": ("judul",)}
    date_hierarchy = "tanggal_terbit"


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ("nama_kegiatan", "waktu_mulai", "tempat")
    list_filter = ("waktu_mulai",)
    search_fields = ("nama_kegiatan", "tempat")
    date_hierarchy = "waktu_mulai"


@admin.register(Dokumen)
class DokumenAdmin(admin.ModelAdmin):
    list_display = ("judul", "tanggal_unggah")
    search_fields = ("judul", "keterangan")


@admin.register(PesanMasuk)
class PesanMasukAdmin(admin.ModelAdmin):
    list_display = ("subjek", "nama", "email", "waktu_kirim", "sudah_dibaca")
    list_filter = ("sudah_dibaca", "waktu_kirim")
    search_fields = ("nama", "email", "subjek", "pesan")
    readonly_fields = ("nama", "email", "subjek", "pesan", "waktu_kirim")  # sudah_dibaca tetap bisa diubah

    def has_add_permission(self, request):
        return False


@admin.register(TautanTerkait)
class TautanTerkaitAdmin(admin.ModelAdmin):
    list_display = ("nama", "url", "urutan")
    list_editable = ("urutan",)
