import os
import subprocess
import wmi
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

#output = subprocess.check_output(['wmic','process','list','brief'])

#output = os.popen('wmic process get description, processid').read()

f = wmi.WMI()
processList = []

for process in f.Win32_process():
    #print(f"{process.Name} {process.ProcessId}")
    newElement = f"{process.Name} {process.ProcessID}"
    processList.append(newElement)

processList.sort()
#print(*processList, sep='\n')

c = canvas.Canvas("Processes.pdf")
c.setFont('Helvetica', 12)

y = 28

for items in processList:
    print(items)
    c.drawString(4*cm,(y)*cm,f"{items}")
    y -= 1
c.save()







