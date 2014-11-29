import difflib

file1=open("file1.txt",'r')
file2=open("file2.txt",'r')
text1=file1.read()
text2=file2.read()
text1_lines = text1.splitlines()
text2_lines=text2.splitlines()
d = difflib.Differ()
print text1_lines 
print "\n\n"
print text2_lines
print "\n\n"
diff = d.compare(text1_lines,text2_lines)
print "\n".join(diff)
