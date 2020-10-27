from docx import document


def dodaj_tabele(document, queryset):
    table = document.add_table(rows=0, cols=7)
    lp = 1
    for i in queryset:
        print(i)
        # formatowanie daty
        data = 'w dn. '
        if str(i.data_powrotu)[5:7] == str(i.data_wyjazdu)[5:7]:
            data += str(i.data_wyjazdu)[8:10] + ' - '
        else:
            data += str(i.data_wyjazdu)[8:10] + '.' + str(i.data_wyjazdu)[5:7] + ' - '
        data += str(i.data_powrotu)[8:10] + '.' + str(i.data_wyjazdu)[5:7] + '.' + str(i.data_wyjazdu)[0:4] + ' r.'
        # wpisywanie danych do tabeli
        komorki = table.add_row().cells
        komorki[0].text = str(lp) + ')'
        komorki[1].text = i.stopien
        komorki[2].text = i.imie
        komorki[3].text = str(i.nazwisko).upper()
        komorki[4].text = data
        komorki[5].text = 'do m.'
        komorki[6].text = i.miasto
        lp += 1
    return table