import camelot

class Extract:

    def process(self):
        tables = camelot.read_pdf("blabla.pdf", pages='1')
        print(tables)

        tables.export('foo.csv', f='csv', compress=True)
        tables[0].to_csv('foo.csv')