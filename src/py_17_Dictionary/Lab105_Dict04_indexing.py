student_info1={
    "name" : "Gauri",
    "age" : 25,
    "age" :30,
    "address" :{
        "home_adds" : "PU",
        "Office_adds" : "MH"
    }
}

student_info2={
    "name" : "Vinit",
    "age" : 35,
    "address" :{
        "home_adds" : "KA",
        "Office_adds" : "MP"
    }
}

student_info3={
    "name" : "Omkar",
    "age" : 28,
    "address" :{
        "home_adds" : "BMT",
        "Office_adds" : "PU"
    }
}


student_list=[student_info1, student_info2, student_info3]
print(student_list)
print(student_list[2]["address"]["home_adds"])      #BMT