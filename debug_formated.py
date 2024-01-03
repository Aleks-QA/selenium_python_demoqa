data1 = ['Commands', 'Documents', 'WorkSpace', 'React', 'Angular', 'Veu', 'Office', 'Public', 'Private', 'Classified',
         'General', 'Word File.doc']
data2 = ['commands', 'documents', 'workspace', 'react', 'angular', 'veu', 'office', 'public', 'private', 'classified',
         'general', 'wordFile']

# lower большие буквы меняет на маленькие
# replace первое значение меняет на второе
data1 = str(data1).replace(' ', '').replace('.doc', '').replace('.', '').lower()
data2 = str(data2).replace(' ', '').replace('.doc', '').replace('.', '').lower()

# data1 = str(data1).replace(' ','').replace('doc','').replace('.','').lower()
#
# data2 = str(data1).replace(' ','').replace('doc','').replace('.','').lower()

assert data1 == data2, "не равны"
