def add_vat(base, irpf=12.5, pagas_extras= False ):
    """
    Docstring
    """
    if pagas_extras== True:
        prorrateo= base/6
        base= base + prorrateo

    if type(base)==float and type(irpf)==float:
        return (base * irpf) / 100.0
    else:
        return None
    
        
print(add_vat(irpf=10.5,base=1000.5, pagas_extras=True))