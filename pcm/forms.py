from django import forms

from .models import PesanMasuk


class KontakForm(forms.ModelForm):
    class Meta:
        model = PesanMasuk
        fields = ["nama", "email", "subjek", "pesan"]
        widgets = {"pesan": forms.Textarea(attrs={"rows": 5})}

    def clean_pesan(self):
        pesan = self.cleaned_data["pesan"].strip()
        if len(pesan) < 10:
            raise forms.ValidationError("Pesan terlalu pendek; tulis minimal 10 karakter.")
        return pesan