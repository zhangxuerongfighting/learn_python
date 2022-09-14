txt = "X-DSPAM-Confidence:0.8475"
count = txt.find('0')         
result = txt[count:]          
ans = float(result)           
print(ans)
