from datetime import date, datetime, timedelta

tipo_carro = "P"  # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    # Time delta acrescenta dias, horas, minutos, segundos.
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")


print(date.today() - timedelta(days=1))  # Removendo um dia da data.

# Estamos adicinando uma hora a mais...aqui a data na date time é ignorado.
resultado = datetime(2025, 3, 15, 19, 13, 20) + timedelta(hours=1)
print(resultado.time())

print(datetime.now().date() - timedelta(days=1))  # Data atual menos um dia.

print(date(2023, 7, 10) - timedelta(days=1))  # Uma data qualquer menos um dia...
