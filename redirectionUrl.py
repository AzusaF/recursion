def redirectionUrl(language):
    # 関数を完成させてください
    url =  "www.example.org"

    if language == "Japanese": url  = url + "/ja"
    elif language == "English": url = url + "/en"
    elif language == "Spanish": url = url + "/es"
    elif language == "Russian": url = url + "/ru"
    else: url = url + "/"
    
    return url
