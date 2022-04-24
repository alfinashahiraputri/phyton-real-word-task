# data about which we want to create a report.
fruit = {
    'elderberries' : 1,
    'figs' : 1,
    'apples' : 2,
    'durians' : 3,
    'bananas' : 5,
    'cherries' : 8,
    'grapes' : 13
}

# Initiate pdf
from reportlab.platypus import SimpleDocTemplate
report = SimpleDocTemplate("report_generated.pdf")

# Import Flowables
from reportlab.platypus import Paragraph, Spacer, Table, Image

# Get Sample Style
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()

# Add Paragraph as Title
report_title = Paragraph('A Complete Inventory of My Fruits', styles['h1'])

# To create a table, we need list-of-list. Convert the dictionary to list-of-list
table_data = [[k,v] for k,v in fruit.items()]

# Create table
report_table = Table(data=table_data)

# Add style to table
from reportlab.lib import colors
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table_styled = Table(data=table_data, style= table_style)

# Generate graphic
inch = 2
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
report_pie = Pie(width=3*inch, height=3*inch)

# Add data to Pie Chart
report_pie.data = []
report_pie.labels = []

for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

# To make Pie Chart Flowable
report_chart = Drawing()
report_chart.add(report_pie)

# Build the PDF with listed elements
report.build([report_title, report_table, report_table_styled, report_chart])
