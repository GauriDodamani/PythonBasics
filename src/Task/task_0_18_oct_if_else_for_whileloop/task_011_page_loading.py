# Simulate a page loading check using a while loop.
# If page_loaded becomes True within 5 seconds, print success; else timeout.
# Hint: Use a counter (like wait_time) and break condition.


#logic:
page_loaded = False
wait_time=0

while wait_time<5:
    print(f" Checking, page is loading.....{wait_time+1}")
    if wait_time==3:
        page_loaded = True
        break

    wait_time = wait_time + 1

if page_loaded:
    print(f" Page loaded successfully {wait_time+1}")
else:
    print(" Time Out.... Page not loaded in 5 seconds")




