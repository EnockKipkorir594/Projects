from difflib import SequenceMatcher

with open('file1.txt') as content1 , open('file2.txt') as content2:
    read1 = content1.read()
    read2 = content2.read()
    matches = SequenceMatcher(None, read1, read2).ratio()
    print(f"the plagiarized content is {matches}%")