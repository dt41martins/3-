teksts1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
teksts2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

def iegut_vardus(teksts):
    import string
    
    teksts = teksts.translate(str.maketrans("", "", string.punctuation)).lower()
    
    return set(teksts.split())

vardi1 = iegut_vardus(teksts1)
vardi2 = iegut_vardus(teksts2)

sakritibas = vardi1 & vardi2  
unikalie1 = vardi1 - vardi2  
unikalie2 = vardi2 - vardi1  

print("Kopīgie vārdi:", sakritibas)
print("Vārdi tikai tekstā 1:", unikalie1)
print("Vārdi tikai tekstā 2:", unikalie2)
