from django.template.loader import render_to_string
prefix_list = []
x = 2
for line in open('/home/myaser/programmerena/test/pro/app/templates/prefixlist'):
    line = line.rstrip()
    prefix_list.append((x, line.split(',')))
    x += 1

rendered = render_to_string('AlkhalilPrefixes.xml', {'lists': prefix_list})
open('/home/myaser/AlkhalilPrefixes.xml', 'w').write(rendered.encode('utf8'))



prefix_list = []
x = 2
for line in open('/home/myaser/programmerena/test/pro/app/templates/suffixlist'):
    line = line.rstrip()
    prefix_list.append((x, line.split(',')))
    x += 1

rendered = render_to_string('AlkhalilSuffixes.xml', {'lists': prefix_list})
open('/home/myaser/AlkhalilSuffixes.xml', 'w').write(rendered.encode('utf8'))
