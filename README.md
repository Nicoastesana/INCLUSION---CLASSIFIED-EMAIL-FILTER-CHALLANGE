# INCLUSION - CLASSIFIED EMAIL FILTER CHALLANGE

## _Astesana's Solution_

## 1- How the process works

The `main.py` file contains the function `classified_email_filter`. It is able of detect if a email might be classified,
and additionally replace any sensitive text with censored
`*****` characters. The args of the function are:

`classified_email_filter(classified, email)`
where:

- **classified**: path of a csv file containing classified words/phrases or a list of them.
- **email**: path of a txt file containing an email text or a string.

_Steps of execution of `classified_email_filter` function:_

1. The email and the list of classified words/phrases are read.
2. For each classified words/phrases:

* 2.a. I search every particular classified words/phrases in the text transforming
* 2.b. I replace them by *****
  characters.

## 2- Details taken and not taken into account

1. The function is lower/upper case-insensitive. It means if in classified words/phrases is the word 'CIA' so this
   program is able of detect also 'Cia' and 'cia'.

* This functionality is helpful for detecting hidden words like `8weapon9`.

* In this case Maybe I want to found only `CIA`, so I can solve it creating 2 lists of classified words/phrases, one for
  the case-sensitive words and other for those not.

2. Possible functionalities not implemented:
* Maybe I would like to detect `CIA` and also `C.I.A.`

## 3- Other aspects
1. Pep 8
2. Python 3.6