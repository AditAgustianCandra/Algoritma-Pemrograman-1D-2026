jarak = 100
konsumsi_bbm = 40
sisa_bbm = 1.5
harga_bbm_perliter = 10000

total_jarak = jarak * 2
kebutuhan_bbm = total_jarak / konsumsi_bbm
bbm_dibeli = kebutuhan_bbm - sisa_bbm
total_biaya = bbm_dibeli * harga_bbm_perliter

print("Total jarak pulang-pergi:", total_jarak, "km")
print("Total kebutuhan BBM:", kebutuhan_bbm, "liter")
print("BBM yang harus dibeli:", bbm_dibeli, "liter")
print("Total biaya: Rp",total_biaya)