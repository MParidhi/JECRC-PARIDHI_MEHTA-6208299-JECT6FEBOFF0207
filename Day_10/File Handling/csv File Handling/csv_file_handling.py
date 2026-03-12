import csv
from datetime import date

file=open('expense.csv', 'a+', newline='') ##this newline will not give any spaces in between of lines
# w = csv.writer(file)

# w.writerow(['DATE', 'CATEGORY', 'AMOUNT']) ##preferred to write column name
# w.writerows([
#     [date.today(), 'Travel', 2000],
#     [date.today(), 'Food', 550],
#     [date.today(), 'Entertainment', 1700],
# ])

r = csv.reader(file)
file.seek(0)
# print(r) #<_csv.reader object at 0x00000209DE7B9BA0>
print(list(r)) #[['DATE', 'CATEGORY', 'AMOUNT'], ['2026-03-10', 'Travel', '2000'], ['2026-03-10', 'Food', '550'], ['2026-03-10', 'Entertainment', '1700']]

file.close()