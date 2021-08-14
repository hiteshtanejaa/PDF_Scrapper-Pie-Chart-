import sys
import camelot
from getCollege import getCollege

def parse(input, pdf):
  print('---Parsing detected tables----')
  tables = camelot.read_pdf(pdf, pages=','.join(map(str,input)))
  tables.export('.\\output\\output.csv', f='csv', compress=True)
  #tables[0].to_csv('output.csv')
  print('---RAR File Generated---')
  print('---RAR file Saved in Output Folder---')

if __name__ == "__main__":
  path = ".\\input\\G570 Computer Science 1st year.pdf"
  code = input("Enter College Code")
  print('----Searching for the pages----')
  pages = getCollege(path, code)
  print('Pages containing results of interest: {0}'.format(pages))
  parse(pages, path)
