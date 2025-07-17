import datetime

# Obtém a data e hora atuais
agora = datetime.datetime.now()

# Formata com dois dígitos usando f-string
data_formatada = f"{agora.day:02d}/{agora.month:02d}/{agora.year}"
hora_formatada = f"{agora.hour:02d}:{agora.minute:02d}"

# Exibe o resultado
print("Data:", data_formatada)
print("Hora:", hora_formatada)
