def napisat_tri_raza_i_vivesti_chislo_simvolov(stroka):
    posledovatelnost = (stroka, stroka, stroka)
    print(",".join(posledovatelnost))
    print("Kolichestvo bukv: " + str(len(stroka)))

stroka = "Kotiki pupsiki"
napisat_tri_raza_i_vivesti_chislo_simvolov(stroka)
