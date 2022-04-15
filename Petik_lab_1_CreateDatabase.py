import sqlite3
con = sqlite3.connect('disease.db') # створення/з_єднання з базою даних
cur = con.cursor()
cur.execute('''CREATE TABLE disease 
               (diseaseName text, cough text, rheum text, soreThroat text, painPunctual text,
               fever text, sputum text, rashOrSpots text, lungsInvolved text,
               vomiting text)''') #створення бази даних

''' поля таблиці: назва хвороби, [наявні симптоми:] кашель, нежить, біль у горлі, біль десь у тілі, гарячка, мокротиння,
   плями/висипання на шкірі, проблеми з легенями, блювання'''

diseases = [('flu','+','-','-','+','+','-','-','-','+'), #грип '1 4 5 9'
              ('cold','+','+','+','-','+','-','-','-','-'), #застуда '1 2 3 5'
              ('bronhitis','+','-','-','-','+','+','-','+','-'), #бронхіт '1 5 6 8'
              ('allergy','+','+','+','-','-','-','+','-','+'), #алергія '1 2 3 7 9'
              ('sinusitis','-','+','-','+','+','-','-','-','-'), #гайморит '2 4 5'
              ('measles','+','-','-','-','+','+','+','-','-'), #кір '1 5 6 7'
              ('pneumonia','+','-','-','+','+','-','-','+','-'), #пневмонія '1 4 5 8'
              ('tracheitis','+','-','+','-','-','-','-','-','-'), #трахеїт '1 3'
              ('pertussis','+','+','-','-','-','+','-','+','+'), #кашлюк '1 2 6 8 9'
              ('pleuritis','+','-','+','+','-','-','-','+','-')] #плеврит '1 3 4 8' ''' 

cur.executemany("INSERT INTO disease VALUES (?,?,?,?,?,?,?,?,?,?)", diseases) #заповнення таблиці хвороб з симптомами
con.commit()
'''for row in cur.execute('SELECT diseaseName FROM disease WHERE soreThroat = "+"'):
        print(str(row))'''
con.close()
