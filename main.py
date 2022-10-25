import sys

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import TABLOID
import numpy as np
from PyPDF2 import PdfFileMerger
import os
import time

def create_label_strings(beekInfo):

    letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    numbers = range(10)

    labels = []
    for data in beekInfo.items():
        beek, yardInfo = data

        for yardID in range(yardInfo[0]):
            for hive in range(yardInfo[1][yardID]):
                firstLetter =  letters[int(np.floor(yardID/26))]
                if hive<10:
                    hiveStr = '00'+str(hive)
                elif 10 <= hive < 100:
                    hiveStr = '0'+str(hive)
                labels.append(beek+'-'+firstLetter+letters[yardID]+'-'+hiveStr)

    return labels

# create_label_strings({'A':[4,[89,12,85,62]]})

def create_labels_simple(numLabels):
    labels = [str(c) for c in range(numLabels)]
    for i in range(numLabels):
        if len(labels[i]) == 1:
            labels[i] = '0000'+labels[i]
        elif len(labels[i]) == 2:
            labels[i] = '000'+labels[i]
        elif len(labels[i]) == 3:
            labels[i] = '00' + labels[i]
        elif len(labels[i]) == 4:
            labels[i] = '0' + labels[i]

    return labels

# create_labels_simple(2000)


def create_labels(beekInfo):
    labels = create_label_strings(beekInfo)
    labelCounter = 0
    pageCounter = 0
    while True:
        canvas = Canvas(f'labelDir\labels{pageCounter}.pdf', pagesize=TABLOID)
        canvas.setFont('Helvetica-Bold', 96)
        print(labelCounter)
        for i in np.linspace(0, 17, 16):
            height = (16-i)
            if labelCounter >= len(labels):
                break
            canvas.drawString(.25*inch, (height)*inch, labels[labelCounter])
            canvas.drawString((.25+5.5)*inch, (height)*inch, labels[labelCounter+1])
            labelCounter+=2
        pageCounter += 1
        canvas.save()
        if labelCounter >= len(labels):
            break

    pdfMerger = PdfFileMerger()

    for file in os.listdir('labelDir'):
        pdfMerger.append(str(os.path.join('labelDir',file)))

    pdfMerger.write('Master2.pdf')

# create_labels({'A':[2,[50,50]]})


def create_labels_s(labelNum):
    labels = create_labels_simple(labelNum)
    labelCounter = 0
    pageCounter = 0
    while True:
        canvas = Canvas(f'labelDir\labels{pageCounter}.pdf', pagesize=TABLOID)
        canvas.setFont('Helvetica', 220)
        for i in np.linspace(0, 14, 6):
            height = ((17 - 23/9)-i)
            # if labelCounter >= len(labels):
            try:
                canvas.drawString(.5*inch, (height)*inch, labels[labelCounter])
                # canvas.drawString((.15+5.5)*inch, (height)*inch, labels[labelCounter+1])
            except:
                break

            labelCounter+=1
            if labelCounter % 6 == 0:
                break
        pageCounter += 1
        canvas.save()
        if labelCounter >= len(labels):
            break

    pdfMerger = PdfFileMerger()

    labelDir = os.listdir('labelDir')
    for fileNum in range(len(labelDir)):
        pdfMerger.append(str(os.path.join('labelDir', f'labels{fileNum}.pdf')))
    print('done')
    pdfMerger.write('singleLabel.pdf')

create_labels_s(30000)