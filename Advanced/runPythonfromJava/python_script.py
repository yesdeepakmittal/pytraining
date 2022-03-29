from num2words import num2words
import pyodbc 

server = 'localhost'
database = 'test' 
username = 'root' 
password = 'root' 
cnxn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

def number_to_words(num):
    ans = num2words(num)
    try:
        idx = ans.index('point')
    except ValueError:
        idx = 0
    if idx:
        ans = ans[:idx] + 'Rupees ' + ans[idx:]
        ans = ans.replace('point','and')
        ans += ' Paise'
    else:
        ans += ' Rupees'
    return ans

with open(f'C:\\Users\\deepak-mittal\\Desktop\\output.txt','w') as fileProxy:
    for i in cursor.execute("SELECT * FROM product"): 
        #converting only numeric column into words & writing it into output.txt file
        print(number_to_words(i[3]),file=fileProxy); 

cnxn.close()