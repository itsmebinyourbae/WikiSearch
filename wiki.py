import wikipedia

def anjay():
  print("""###############################
#      - WikiSearch -         #
# Copyright © Andika Bintang  #
#   XI RPL SMK Nurul Islam    #
#      ##############         #
# "pacar tidak perlu,         #
#         wawasan nomer satu" #
###############################""")

def Wiki():
  lang = input("\n Pilih Bahasa en/id : ")
  if lang == "en":
    pass
  elif lang == "id":
    pass
  else:
    print("Kode tidak valid, example \"en\" for English.")
    Wiki()
  wikipedia.set_lang(lang)
  cari = input("Apa yang anda cari? ")
  result = wikipedia.summary(cari)
  print("Hasil : \n\n",result)
anjay()
Wiki()
