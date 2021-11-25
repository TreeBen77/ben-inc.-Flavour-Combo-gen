# ice-cream Flavor Combo
**You can run this script without downloading it here: https://replit.com/@TreeBen77/ice-cream-Flavor-Combo**

It counts all possible combonations of ice cream using the flavours in the 'flavours' list variable, exculding duplicating flavours or shuffling flavours. This is designed for an activity in Connections Maths Stage 4 'Which Ice-cream' (ISBN: 9781741251876).

### Instructions
1. Download [main.py](https://github.com/TreeBen77/ice-cream-Flavor-Combo/blob/main/main.py) and Python 3. Python 3 can be downloaded here: https://python.org/downloads/
2. Open the file in IDLE and modify line 3 to what flavours you would like to include. (e.g. `flavours = ["C", "S", "V", "M", "P"]`)
3. Run the file. it will take about 7 seconds to generate your results. The results will show: how many attempts it made, amount of possible combonations, number of flavours and every combonation.

## Example Output
Outputs are alway unique because they are randomly brute forced. Don't worry if the combonations are in a different order or the 4 didget numbers are different, this is normal.
```
Flavour Combo gen
Flavours: ['C', 'S', 'V']

0001 SV
0002 CV
0003 CSV
0005 S
0012 V
0013 CS
0016 C

Result: there's 7 possible combinations in 3 flavours. finished in 50017 attempts.
```
### Output Key
|Key|Description|Example
|--|--|--
|4+ Digit Number|Number of attempts to find it.| `0012`
|Mix of Flavours|Ice cream combonation made. | `CSV`
|Final Output Line|Shows all possible combonations, number of flavours and the number of attempts. | `Result: there's 7 possible combinations in 3 flavours. finished in 50017 attempts.`
