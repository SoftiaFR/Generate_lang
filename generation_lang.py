__author__ = "Camille Vrignaud, Dylan Guerabes"
__copyright__ = "Copyright 2019, Softia"
__credits__ = ["Camille Vrignaud", "Dylan Guerabes"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Softia"
__email__ = "cvrignaud@softia.fr"
__status__ = "Production"
# Import lib
import xlrd
import sys

# Give the location of the file
loc = sys.argv[1]

# To open Workbook
wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)

# Parse XLSX
for col in range(1, sheet.ncols):
    lang = sheet.cell_value(0, col).lower()
    nameNewFile = "messages."+lang+".xlf"
    with open(nameNewFile, "w", encoding="utf-8") as file:
        start_file = '<?xml version="1.0" encoding="utf-8"?> \n' \
                     '<xliff xmlns="urn:oasis:names:tc:xliff:document:2.0" version="2.0" srcLang="'+lang+'"' \
                     ' trgLang="'+lang+'">\n \t' \
                     '<file id="messages.'+lang+'">\n'
        file.write(start_file)
        for row in range(1, sheet.nrows):
            print("$traduction['"+sheet.cell_value(row, 1)+"'] = $this->translator->trans('"+sheet.cell_value(row, 1)+"',[], null,$session->get('lang'));")
            unit = '\t\t<unit name="'+sheet.cell_value(row, 1)+'">\n' \
                   '\t\t\t<segment>\n' \
                   '\t\t\t\t<source>'+sheet.cell_value(row, 1)+'</source>\n' \
                   '\t\t\t\t<target>'+sheet.cell_value(row, col)+'</target>\n' \
                   '\t\t\t</segment>\n' \
                   '\t\t</unit>\n'
            file.write(unit)
        print('\n\n\n')
        end_file = '\t</file>\n' \
                   '</xliff>'
        file.write(end_file)
