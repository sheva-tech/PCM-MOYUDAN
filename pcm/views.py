from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import KontakForm
from .models import Agenda, AmalUsaha, Berita, Dokumen, Pimpinan, Ranting


def beranda(request):
    return render(request, "pcm/beranda.html", {
        "jumlah_ranting": Ranting.objects.count(),
        "jumlah_amal_usaha": AmalUsaha.objects.count(),
        "berita_terbaru": Berita.objects.terbit()[:3],
        "agenda_mendatang": Agenda.objects.akan_datang()[:3],
    })


def profil_view(request):
    return render(request, "pcm/profil.html")


def pimpinan(request):
    return render(request, "pcm/pimpinan.html", {"daftar_pimpinan": Pimpinan.objects.all()})


def ranting(request):
    return render(request, "pcm/ranting.html", {"daftar_ranting": Ranting.objects.all()})


def amal_usaha(request):
    kelompok = [(label, AmalUsaha.objects.filter(bidang=kode)) for kode, label in AmalUsaha.Bidang.choices]
    return render(request, "pcm/amal_usaha.html", {"kelompok": [(l, q) for l, q in kelompok if q]})


def berita_list(request):
    q = request.GET.get("q", "").strip()
    daftar = Berita.objects.terbit()
    if q:
        daftar = daftar.filter(Q(judul__icontains=q) | Q(ringkasan__icontains=q) | Q(isi__icontains=q))
    halaman = Paginator(daftar, 6).get_page(request.GET.get("page"))
    return render(request, "pcm/berita_list.html", {"halaman": halaman, "q": q})


def berita_detail(request, slug):
    berita = get_object_or_404(Berita.objects.terbit(), slug=slug)
    lainnya = Berita.objects.terbit().exclude(pk=berita.pk)[:3]
    return render(request, "pcm/berita_detail.html", {"berita": berita, "berita_lainnya": lainnya})


def agenda(request):
    return render(request, "pcm/agenda.html", {
        "akan_datang": Agenda.objects.akan_datang(),
        "terlaksana": Agenda.objects.terlaksana(),
    })


def unduhan(request):
    return render(request, "pcm/unduhan.html", {"daftar_dokumen": Dokumen.objects.all()})


def kontak(request):
    form = KontakForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Terima kasih, pesan Anda sudah terkirim.")
        return redirect("pcm:kontak")
    return render(request, "pcm/kontak.html", {"form": form})