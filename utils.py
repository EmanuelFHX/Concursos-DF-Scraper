def limpar_salario(valor):
    try:
        valor = valor.replace("R$", "").replace(".", "").replace(",", ".").strip()
        return float(valor)
    except:
        return 0