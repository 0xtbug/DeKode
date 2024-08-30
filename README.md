# DeKode
**DeKode** is a tools designed to decode strings that have been encoded using lambda methods, as generated by this [tools](https://github.com/htr-tech/PyObfuscate).

# Feature
- Decodes the string encoded with the method:
  - `Lambda base64.b16decode`
  - `Lambda base64.b32decode`
  - `Lambda base64.b64decode`
  - `Lambda zlib.decompress(base64.b16decode)`
  - `Lambda zlib.decompress(base64.b32decode)`
  - `Lambda zlib.decompress(base64.b64decode)`

# Installation
Clone this repository
```bash
git clone https://github.com/0xtbug/DeKode
```
Move direcory
```bash
cd DeKode
```
Install depedencies
```bash
pip install -r requirements.txt
```

# Usage
Move the script want to decode to encode.txt

Run tools
```bash
python main.py
```

The result saved in result.txt

# Contributions
Contributions to the DeKode are welcome. Please ensure that your code adheres to the project's standards and submit a pull request for review.