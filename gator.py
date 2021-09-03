import sys,os,time
'''
---------------------------------------------
アップロード 14 十二月 2020
かわった 10 一月 2021
これがぼくのはじめてがパイトンプログラムのべんきょうします。
よろしく
---------------------------------------------
'''
#definisi rumus
def tambah(a,b):
  return a+b
def kurang(a,b):
  return a-b
def kali(a,b):
  return a*b
def bagi(a,b):
  return a/b
def pangkat(a,b):
  return a**b

#rumus warna
merah =('\033[31;1m')
kuning= ('\033[1;33m')
hijau = ('\033[0;32m')
dilangit = ('\033[37;1m')
yang = ('\033[32;1m')
biru = ('\033[0;36m')

#banner 
def mulai():
  os.system("clear")
  print(merah,'             ___________________________')
  print('         ∆∆∆∆∆|',kuning,'      ∆°GaToR°∆      ',merah,'|∆∆∆∆∆')
  print('       ∆∆∆∆∆∆∆|',kuning,'      ＼(°o°)／      ',merah,'|∆∆∆∆∆∆∆')
  print('     ∆∆∆∆∆∆∆∆∆|',kuning,'    でんたく(電卓)   ',merah,'|∆∆∆∆∆∆∆∆∆')
  print('              ```````````````````````````')
  print(hijau,'__Kalau Ada yg susah mengapa harus yg mudah :v__ '.center(55))
  print('    ==================='+merah,'^•V1.0•^',hijau+'===================')
  print('')
  print(merah,'=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠='.center(55),biru)
  print('°©Gabut kalkulator = GaToR®°'.center(55))
  print('___________________'.center(55))
  print('|1.  Pertambahan  |'.center(55))
  print('|2.  Pengurangan  |'.center(55))
  print('|3.  Perkalian    |'.center(55))
  print('|4.  Pembagian    |'.center(55))
  print('|5.  Perpangkatan |'.center(55))
  print('|0.  Keluar       |'.center(55))
  print('```````````````````'.center(55))
  print(merah,'=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠=≠='.center(55))
  print(kuning,'   [!]',hijau+'Nb: Kalo pake koma ganti titik ya tod :v',kuning+'[!]')
  print(' ')
  
  #definisi input dari user
  pilih = str()
  while pilih !="1" and pilih != "2" and pilih !="3" and pilih !="4" and pilih !='5' and pilih !="0":
    pilih=str(input(kuning+'[√]'+dilangit+'Silahkan Pilih Option: '))
  if pilih=='0':
    print('Terima Kasih Sudah menggunakan tools gabut ini :v'.center(55))
    print('SemogaHarimuMenyenangkan (≧▽≦)'.center(55))
    print('ありがとうございました'.center(45))
    time.sleep(3)
    os.system("sl")
    exit()
    
  #perulangan dan input
  else:
      print(kuning+'[!]'+hijau+'Masukan Angka Pertama dan Kedua'+kuning+'[!]')
      a=float(input(merah+'[✓]'+hijau+'No1: '))
      b=float(input(merah+'[✓]'+hijau+'No2: '))
      if pilih =='1':
        print(kuning,'  [∆]'+merah+'Hasil: ',tambah(a,b))
        #memanggil definisi banner
        pil=input(kuning+'[!]'+hijau+'Ulangi? y/t: ')
        if pil =='y' or pil == 'Y':
          print(kuning+'                  '+'__[!]'+merah+'STARTED'+kuning+'[!]__')
          time.sleep(3)
          mulai()
        else:
          print('     Terima Kasih Sudah menggunakan tools gabut ini :v ')
          print('SemogaHarimuMenyenangkan (≧▽≦)'.center(55))
          print('ありがとうございました'.center(45))
          print(' ')
          print(kuning+'                    '+'[!]'+merah+'Keluar'+kuning+'[!]')
          time.sleep(3)
      elif pilih=='2':
           print(kuning,'  [∆]'+merah+'Hasil: ',kurang(a,b))
        #memanggil definisi banner
           pil=input(kuning+'[!]'+hijau+'Ulangi? y/t: ')
           if pil =='y' or pil == 'Y':
             print(kuning+'                   __[!]'+merah+'STARTED'+kuning+'[!]__')
             time.sleep(3)
             mulai()
           else:
             print('SemogaHarimuMenyenangkan (≧▽≦)'.center(55))
             print('ありがとうございました'.center(45))
             print (' ')
             print(kuning+'                    '+'[!]'+merah+'Keluar'+kuning+'[!]')
             time.sleep(3)
      elif pilih=='3':
             print(kuning,'  [∆]'+merah+'Hasil: ',kali(a,b))
        #memanggil definisi banner
             pil=input(kuning+'[!]'+hijau+'Ulangi? y/t: ')
             if pil =='y' or pil == 'Y':
               print(kuning+'                   __[!]'+merah+'STARTED'+kuning+'[!]__')
               time.sleep(3)
               mulai()
             else:
               print('SemogaHarimuMenyenangkan (≧▽≦)'.center(55))
               print('ありがとうございました'.center(45))
               print(' ')
               print(kuning+'                    '+'[!]'+merah+'Keluar'+kuning+'[!]')
               time.sleep(3)
      elif pilih=='4':
        print(kuning,'  [∆]'+merah+'Hasil: ',bagi(a,b))
        #memanggil definisi banner
        pil=input(kuning+'[!]'+hijau+'Ulangi? y/t: ')
        if pil =='y' or pil == 'Y':
          print(kuning+'                   __[!]'+merah+'STARTED'+kuning+'[!]__')
          time.sleep(3)
          mulai()
        else:
          print('SemogaHarimuMenyenangkan (≧▽≦)'.center(55))
          print('ありがとうございました'.center(45))
          print(' ')
          print(kuning+'                    '+'[!]'+merah+'Keluar'+kuning+'[!]')
          time.sleep(3)
      elif pilih=='5':
        print(kuning,'  [∆]'+merah+'Hasil: ',pangkat(a,b))
        #memanggil definisi banner
        pil=input(kuning+'[!]'+hijau+'Ulangi? y/t: ')
        if pil =='y' or pil == 'Y':
          print(kuning+'                   __[!]'+merah+'STARTED'+kuning+'[!]__')
          time.sleep(3)
          mulai()
        else:
          print('SemogaHarimuMenyenangkan (≧▽≦)'.center(55))
          print('ありがとうございました'.center(45))
          print(' ')
          print(kuning+'                    '+'[!]'+merah+'Keluar'+kuning+'[!]')
          time.sleep(3)
          
#memanggil banner dari atas
mulai()
