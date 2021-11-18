import re, json

'''
with open("corrupted-file.json", "r") as read_file:
    bad_json = read_file.read()
    improved_json  = re.sub(r'"\s*$', '",', bad_json, flags=re.MULTILINE)
    print(improved_json)

    
    good_json = re.sub(r'(?<=[\{\[\s])(?P<word>[\w-]+)(?=[:,\]\s])', '"\g<word>"',
      improved_json)
    with open('out.json', 'w') as fh:
        fh.write(good_json)

    data = json.loads(improved_json)
    # data = json.load(read_file)'''

count = 0
objects = 0
with open('corrupted-file.json') as f:
    for i, c in enumerate(f.read()):
      if c == '\n':
        continue
      elif c == '{':
        if i > 0 and count == 0:
          print()  # start new line before printing bracket
        count += 1
      elif c == '}':
        count -= 1
        if count == 0:  # found a complete JSON object
          objects += 1
      print(c, end='')
    print(f'\n\n\n\n\n\n\n\nfound {objects} objects')  # for debugging 