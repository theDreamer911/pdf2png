from pdf2image import convert_from_path
images = convert_from_path('example.pdf', 50)
for image in images:
    image.save('output.png')
