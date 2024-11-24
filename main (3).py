teksts1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
teksts2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

def iegut_vardus(teksts):
    import string
    teksts = teksts.translate(str.maketrans("", "", string.punctuation)).lower()
    return set(teksts.split())

vardi1 = iegut_vardus(teksts1)
vardi2 = iegut_vardus(teksts2)

kopigie = vardi1 & vardi2
sakritibas_procents = (len(kopigie) / ((len(vardi1) + len(vardi2)) / 2)) * 100

print("Kopīgie vārdi:", kopigie)
print(f"Sakritības līmenis: {sakritibas_procents:.2f}%")
