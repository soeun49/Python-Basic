def question4():
    s = """We encourage everyone to contribute to Python. 
    If you still have questions after reviewing the material
    in this guide, then the Python Mentors 
    group is available to help guide new contributors through the process."""

    str1=s.upper().replace(",","").replace(".","").replace("\n","")
    print(str1.split())

    counts=dict()
    for word in str1.split():
        counts[word]=counts.get(word,0)+1
    print(counts.items())














if __name__ == '__main__':
    question4()
