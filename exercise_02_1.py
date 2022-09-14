Exercise 5: Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extracted
string into a floating point number.

txt = "X-DSPAM-Confidence:0.8475"
count = txt.find('0')         
result = txt[count:]          
ans = float(result)           
print(ans)
