test_result=["PASS","FAIL","PASS","PASS","SKIP","FAIL"]

give_pass=list(filter(lambda x : x=="PASS", test_result))
print(give_pass)

#o/p: ['PASS', 'PASS', 'PASS']


