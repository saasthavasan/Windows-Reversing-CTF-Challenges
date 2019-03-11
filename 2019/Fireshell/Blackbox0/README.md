# Blackbox0

## Writeup

* Use Procom to filter out Blackbox0 activities
* Make a Blackbox0 directory
* The executable was trying to run base64.exe inside Blackbox0 filter
* Copying echo.exe to Blackbox0 directory and renaming it to base64.exe will print the base64 encoded string
* Decoding the base64 string will give the flag

## Flag: **F#{Nice_analisys_bro_=]_}**
