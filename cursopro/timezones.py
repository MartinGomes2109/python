from datetime import datetime
import pytz

bogota_timezone = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_timezone)
print('hora de Bogota: ', bogota_date.strftime('%d/%m/%Y, %H:%M:%S') )
print()
Argentina_timezone = pytz.timezone('America/Argentina/Buenos_aires')
Argentina_date = datetime.now(Argentina_timezone)
print('hora de Argentina: ', Argentina_date.strftime('%d/%m/%Y, %H:%M:%S') )
print()
Mexico_timezone = pytz.timezone('America/Mexico_City')
Mexico_date = datetime.now(Mexico_timezone)
print('hora de Mexico: ', Mexico_date.strftime('%d/%m/%Y, %H:%M:%S') )

