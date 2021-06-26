# Vignere cipher

<br>

### Create a key
```
python vignere.py create-key
```
```
eNPmRVQKiiStbngAEzNuUtYctiPClA
```

<br>

### Encrypt a message
```
python vignere.py encrypt --text "my cool message" --key eNPmRVQKiiStbngAEzNuUtYctiPClA
```
```
q#Mo591Hum!Lbtk
```

<br>

### Decrypt it
```
python vignere.py decrypt --text "q#Mo591Hum!Lbtk" --key eNPmRVQKiiStbngAEzNuUtYctiPClA
```
```
my cool message
```