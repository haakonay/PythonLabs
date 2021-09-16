
# passing the processes as a string or array

import subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

c = canvas.Canvas("MyFirstPythonPdf.pdf")
# counts from 0 from left corner
c.drawString(2*cm,27*cm,"this is the text")
#c.line...
c.save()

#p = subprocess.Popen('calc')

# loop running throug running processes
# appropriate x y coordinates
