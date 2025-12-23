#response time mile seconds to seconds


response_time_ms=[10000,12000,15000]

def mil_sec(x):
    return x/1000


response_to_seconds=list(map(mil_sec, response_time_ms))
print(response_to_seconds)


#o/p: [10.0, 12.0, 15.0]