import smtplib

# my_email = "mmanusx@gmail.com" # kendi email adresimi yazıyorum, mailin çıkış yapacağı adres
# password = "*******"
# connection = smtplib.SMTP("smtp.gmail.com") # smtp nesnesi yaratıp, gmaillin smtp server adresini giriyorum
# connection.starttls() # tls = transport layer security// email server a bağlantıyı güvenliğe alıyor/ mesajı encrypt ediyor
# connection.login(user=my_email, password=password) # bağlantıyı güvene aldıktansonra login olabiliriz
# connection.sendmail(from_addr=my_email,
#                     to_addrs="manus_x@yahoo.com",
#                     msg="Subject:Hello\n\nThis is the body of my email.") # subject ve context eklemek subject olmadan spam a düşecektir
# connection.close()

# <---------------------------------||| connection close kullanmak yerine file open da yaptığım gibi with kullanabilirm ||| --------------------->

# my_email = "mmanusx@gmail.com" # kendi email adresimi yazıyorum, mailin çıkış yapacağı adres
# password = "161816181618mhs." # yahoo da app bağlamak için güvenlik merkezinden app şifresi veriyor kendi şifremiz yerine o şifreyi girmemiz gerekecek
# with smtplib.SMTP("smtp.gmail.com") as connection:# smtp nesnesi yaratıp, gmaillin smtp server adresini giriyorum
#     connection.starttls() # tls = transport layer security// email server a bağlantıyı güvenliğe alıyor/ mesajı encrypt ediyor
#     connection.login(user=my_email, password=password) # bağlantıyı güvene aldıktansonra login olabiliriz
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="manus_x@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.") # subject ve context eklemek subject olmadan spam a düşecektir

# <-----------------------------||| datetime module |||----------------------->

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# if year == 2022:
#     print("Wear a face mask")
# print(day_of_week)
#
#
# # data time sınıfı ile yeni bir nesne yaratmak
# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)
#

#<----------------------------||| Project Start |||----------------------------->

import datetime as dt
import random as rd
import smtplib
now = dt.datetime.now()
weekday = now.weekday()
MY_EMAIL = "mmanusx@gmail.com"
PASSWORD = "****"


if weekday == 0:
    with open("quotes.txt") as file:
        lines = file.readlines()
    quote_of_day = rd.choice(lines)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs="manus_x@yahoo.com",
                            msg=f"Subject: Quote of week\n\n{quote_of_day}"
                            )





















