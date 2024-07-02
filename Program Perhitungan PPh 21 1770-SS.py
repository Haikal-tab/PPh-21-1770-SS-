print("---PERHITUNGAN PPH 21 (1770-SS)---", "\n","\n")

print("---PENGHASILAN BRUTO---","\n")

income_1_tahun = float(input(f"Masukkan Gaji per Tahun Anda: Rp"))
print(f"(1). Penghasilan Anda 1 tahun: Rp{income_1_tahun:,}", "\n", "\n")

print("---TUNJANGAN iSTRI---")  #(tarif 10%)
tunjangan_istri = income_1_tahun*(10/100)
print(f"(2). Tunjangan Istri 1 Tahun: Rp{tunjangan_istri:,.0f}", "\n", "\n" )

print("---TUNJANGAN ANAK---")
tunjangan_anak = income_1_tahun*(0/100)
print(f"(3). Tunjangan Anak 1 Tahun: Rp{tunjangan_anak:,.0f}","\n","\n")

print("---JUMLAH GAJI & TUNJANGAN KELUARGA (1+2+3)---")
jumlah_gaji = income_1_tahun+tunjangan_istri+tunjangan_anak
print(f"(4). Jumlah Gaji 1 Tahun: Rp{jumlah_gaji:,.0f}", "\n", "\n")

print("---TUNJANGAN PERBAIKAN PENGHASILAN---")
tunjangan_perbaikan = income_1_tahun*(0/100)
print(f"(5). Tunjangan Perbaikan Penghasilan 1 Tahun: Rp{tunjangan_perbaikan:,.0f}","\n","\n")

print("---TUNJANGAN STRUKTURAL/FUNGSIONAL---")   #(tarif 14%)
tunjangan_struktural = income_1_tahun*(625/4622)
print(f"(6). Tunjangan Struktural/Fungsional 1 Tahun: Rp{tunjangan_struktural:,.0f}","\n","\n")

print("---TUNJANGAN BERAS---")  #(tarif 5%)
tunjangan_beras = income_1_tahun*(1207/23110)
print(f"(7). Tunjangan Beras 1 Tahun: Rp{tunjangan_beras:,.0f}","\n","\n")

print("---TUNJANGAN KHUSUS---")  #(tarif 0%)
tunjangan_khusus = income_1_tahun*(1.31874*10**-5)
print(f"(8). Tunjangan Khusus 1 Tahun: Rp{tunjangan_khusus:,.0f}","\n","\n")

print("---TUNJANGAN LAIN-LAIN---")
tunjangan_lainnya = income_1_tahun*(0/100)
print(f"(9). Tunjangan Lain-lain 1 Tahun: Rp{tunjangan_lainnya:,.0f}","\n","\n")

print("---JUMLAH (4 S.D. 9)---")
jumlah_4sd9 = jumlah_gaji + tunjangan_perbaikan + tunjangan_struktural + tunjangan_beras + tunjangan_khusus + tunjangan_lainnya
print(f"(10). Jumlah Gaji Bruto 1 Tahun: Rp{jumlah_4sd9:,.0f}","\n","\n")



print("---PENGURANG---","\n")

print("---BIAYA JABATAN---")   #(tarif 6%)
biaya_jabatan = income_1_tahun*(0.0643732)
print(f"(11). Biaya Jabatan: Rp{biaya_jabatan:,.0f}","\n","\n")

print("---IURAN PENSIUN---")   #(tarif 5%)
iuran_pensiun = income_1_tahun*(405719/7764960)
print(f"(12). Iuran Pensiun: Rp{iuran_pensiun:,.0f}","\n","\n")

print("---JUMLAH PENGURANGAN (11 + 12)---")
jumlah_pengurangan = biaya_jabatan + iuran_pensiun
print(f"(13). Biaya Jabatan: Rp{jumlah_pengurangan:,.0f}","\n","\n")



print("---PENGHITUNGAN PPh PASAL 21---","\n")

print("---PENGHASILAN NETO (10 - 13)---")
gaji_neto = jumlah_4sd9 - jumlah_pengurangan
print(f"(14). Jumlah Gaji Neto 1 Tahun: Rp{gaji_neto:,.0f}","\n","\n")

print("---PENGHASILAN TIDAK KENA PAJAK (PTKP)---", "\n")
z = float(input("Masukkan Tanggungan Anda (isi '4' jika Anda bukan Tidak Kawin): " ))

print("-----Pria/Wanita Tidak Kawin-----")
if z == 0:
    print(f"PTKP Anda: Rp",int(54*1000000), "\n")
elif z == 1:
    print(f"PTKP Anda: Rp",float(58.5*1000000), "\n")
elif z == 2:
    print(f"PTKP Anda: Rp",int(63*1000000), "\n")
elif z == 3:
    print(f"PTKP Anda: Rp",float(67.5*1000000), "\n")
else: 
    print("Status Anda bukan Pria/Wanita Tidak Kawin", "\n")



a = float(input("Masukkan Tanggungan Anda (Isi '4' jika Anda bukan Pria Kawin):"))

print("-----Pria Kawin-----")
if a==0:
    print(f"PTKP Anda: Rp",float(58.5*1000000), "\n")
elif a==1:
    print(f"PTKP Anda: Rp",int(63*1000000), "\n")
elif a==2:
    print(f"PTKP Anda: Rp",float(67.5*1000000), "\n")
elif a==3:
    print(f"PTKP Anda: Rp",int(72*1000000), "\n")
else: 
    print("Status Anda Bukan Pria Kawin", "\n")



b = float(input("Masukan Tanggungan Anda (Isi '4' jika Anda bukan Suami & Istri Digabung):"))

print("-----Suami & Istri Digabung-----")
if b==0:
    print(f"PTKP Anda: Rp",float(112.5*1000000), "\n")
elif b==1:
    print(f"PTKP Anda: Rp",int(117*1000000), "\n")
elif b==2:
    print(f"PTKP Anda: Rp",float(121.5*1000000), "\n")
elif b==3:
    print(f"PTKP Anda: Rp",int(126*1000000), "\n")
else:
    print("Status Anda Bukan Suami & Istri Digabung", "\n", "\n")



print("---Penghitungan Penghasilan Kena Pajak (PKP)---\n")

p = float(input("Masukkan PTKP Anda: Rp"))
print(f"PTKP: Rp{p:,.0f}")
pkp = gaji_neto-p
print(f"PKP: Rp{pkp:,.0f}", "\n","\n")

print("---PPh Pasal 21 Terutang---")

pph_21 = pkp * 0
print(f"PPh 21 Terutang: Rp{pph_21:.0f}","\n")


print("#ayobayarpajak!")

v = input("Selesai")
