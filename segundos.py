sec=int(input("Por favor, entre com o número de segundos que deseja converter:"))
dia=sec//86400
sec_dia=sec-(dia*86400)
horra=sec_dia//3600
sec_horra=sec_dia-(horra*3600)
min=sec_horra//60
sec_f=sec_horra-(min*60)
print(dia,"dias,",horra,"horas,",min,"minutos e",sec_f,"segundos.")