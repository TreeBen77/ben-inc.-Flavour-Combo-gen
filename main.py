import random

flavours = ["C", "S", "V", "M", "P", "R"]

try:
  print(f"Flavour Combo gen\nFlavours: {flavours}\n")

  printed = []
  nofindattempts, attempts = 0, 0
  while True:
    attempts += 1
    nofindattempts += 1

    random.shuffle(flavours)
    choice = random.randint(1, len(flavours))

    icecream = sorted(flavours[0:choice])
    endicecream = str()
    for index in range(0, choice):
      endicecream += icecream[index]
  
    if not endicecream in printed:
      printed.append(endicecream)
      nofindattempts = 0
      print(f"{attempts:04}", endicecream)
    elif nofindattempts > 5000:
      print(f"\nResult: there's {len(printed)} possible combinations in {len(flavours)} flavours. finished in {attempts} attempts.")
      break
except(KeyboardInterrupt):
  print(" ", len(printed))
