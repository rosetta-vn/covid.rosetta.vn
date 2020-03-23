# Python3 script to manipulate translation source
# Dang Doan (minhdang@linux.com)
# 2020-03-23
#
# Call: python3 commands.py

if False:
  # Sort lines by length, longest line first
  infn = "dich_en.txt"
  outfn = "ordered_dich_en.txt"
  with open(infn, "rt") as file:
    lines = file.readlines()
  lengthlines = [len(k) for k in lines]
  ind = sorted(range(len(lengthlines)), key=lambda k: lengthlines[k], reverse=True)
  # https://stackoverflow.com/questions/7851077/how-to-return-index-of-a-sorted-list
  newlines=[lines[k] for k in ind]
  with open(outfn, "wt") as file:
    file.writelines(newlines)

if True:
  # replace phrases
  sourcefile = "ordered_dich_en.txt"
  targetfile = "ordered_dich_vi.txt"
  replacefile = "App.svelte"
  # copy App.svelte from epcalc/src/ to the same folder of this Python script
  # epcalc: https://github.com/gabgoh/epcalc
  # replacefile should be in source script, not the generated "bundle.css.map", "bundle.js.map", "bundle.js"
  # because variables like Location, day would be replaced and output code would be messed up
  with open(sourcefile, "rt") as file:
    sourcelines = file.readlines()
  sourcelines = [line.rstrip("\n") for line in sourcelines]
  with open(targetfile, "rt") as file:
    targetlines = file.readlines()
  targetlines = [line.rstrip("\n") for line in targetlines]
  with open(replacefile, "rt") as file:
    text = file.read()
  for k in range(len(sourcelines)):
    text = text.replace(sourcelines[k], targetlines[k])
  with open(replacefile, "wt") as file:
    file.write(text)
  # then copy replacefile to epcalc/src/ and follow instruction thereby to compile Javascript with: npm run build

print("  Command to generate website with Nodejs and Svelte app: epcalc$ npm run build")