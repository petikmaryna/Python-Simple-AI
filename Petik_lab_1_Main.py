import sqlite3

cleanser = {40: None, 41: None, 44: None, 39: None} #словник для очищення результуючої строки від сторонніх символів
symptoms = {'1':'cough', '2':'rheum', '3':'soreThroat', '4':'painPunctual', '5':'fever', '6':'sputum', '7':'rashOrSpots', '8':'lungsInvolved', '9':'vomiting'}

def userInsertSymptoms(sympDict): #ввід симптомів для юзера
        print("Please, insert space-separated numbers corresponding \nto the symptoms you expirience, for example: 1 7 8 9\n")
        print("Cough(1), rheum(2), sore throat(3), pain in the body(4) \nfever(5), sputum(6), rash or spots on skin(7), \ntroubles with lungs(8), vomiting(9)\n")
        print("My symptoms: ", end = "")
        userAnswer = list(input().split(" "))
        for num in userAnswer: #перевірка, що сиптоми введені корректно
                if num not in sympDict:
                        print("Sorry, you entered something wrong.")
                        return False
        return userAnswer

def processUserSymptoms(sympDict, clean): #пошук хвороби 
        con = sqlite3.connect('disease.db') # з_єднання з базою даних
        cur = con.cursor()
        userSymptoms = userInsertSymptoms(sympDict)
        if not userSymptoms: #перевірка, що симптоми отримані
                return 
        request = 'SELECT diseaseName FROM disease WHERE '
        symptDict = sympDict.copy()
        for sym in userSymptoms: #формування реквесту з припущенням того, що ти симптоми, яких юзер не ввів, у нього можуть бути
                request = request + symptDict[sym] + '= "+" AND '
                del symptDict[sym]
        requestFull = request
        request = request[:len(request)-4]
        #print(request)
        for sym in symptDict.values(): #формування реквесту з припущенням того, що тих симптомів, які юзер не ввів, у нього точно немає(для отримання точного результата хвороби)
                requestFull =  requestFull + sym + '= "-" AND ' 
        requestFull = requestFull[:len(requestFull)-4]
        #print(requestFull)
        for diagnose in cur.execute(requestFull): #вивід найточнішого результату(якщо є)
                print("You could most possibly be ill with ", str(diagnose).translate(clean))
                return True
        print("There are no illness that can be matched fully with symptoms you entered.")
        response = []
        for diagnose in cur.execute(request): #обробляемо результат, щоб його можна було перевірити
                       response.append(str(diagnose).translate(clean))
        if response: #вивід усіх інших результатів, які мають введені юзером симптоми
                print("You could possibly be ill with:")
                for diagnose in cur.execute(request):
                        print(str(diagnose).translate(clean))
                return True
        else: #якщо хвороба не знайдена, функція повертає фолс
                return False
        con.close()

        
while not processUserSymptoms(symptoms, cleanser): #повторяється доки не отримано результат
      pass
