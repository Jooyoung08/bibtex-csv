#!/usr/bin/env python3
"""
이 코드는 아래 코드를 포크하여 수정한 것임.
Reference code on GitHub
https://github.com/fluffels/bibtex-csv/blob/master/convert.py
////////////////////////////////

사용법
자세한 내용은 README.md 참조
python3 conv.py < test.bib > output.csv
"""

from os import getcwd
from os import listdir
from re import match
from re import search
from re import findall
from sys import stdin
from string import capwords

entries = []
entry = {}
#regist: example of internal members
#알고 있는 멤버 확인
regist = ["J. Y. Lee"]

for line in stdin:
    if (match('^@', line.strip())):
        if entry != {}:
            entries.append(entry)
            entry = {}
    elif (match('url', line.strip())):
        value, = findall('\{(\S+)\}', line)
        entry["url"] = value
    elif (search('=', line.strip())):
        key, value = [v.strip(" {},\n") for v in line.split("=", maxsplit=1)]
        entry[key] = value

# csv 파일 상단의 제목 (optional)
# 아래 실제 정보과 일치하는지 확인 필요
# 데이터 구분을 위해 "|" 사용
# "공백", "," 등의 문자도 사용 가능
print("Title|Journal|ISSN|DOI|Vol|Issue|Year|Month|page|Number of Author|Authors")

entries.append(entry)

for entry in entries:
    author = "NA"
    if "author" in entry:
        author = entry["author"]
    elif "authors" in entry:
        author = entry["authors"]
    spAu = author.split('and')
    #총 저자 수
    Nauthor = len(spAu)
    new_list = [i.strip() for i in spAu]
    #저자 (resist에 저장된 저자만 출력)
    f_au = set(new_list) & set(regist)
    author = ','.join(f_au)

    #논문 제목
    title = "NA"
    if "title" in entry:
        title = entry["title"]

    #게제 저널
    journal = "NA"
    if "journal" in entry:
        journal = entry["journal"]
   
    #게제 연도
    year = "NA"
    if "year" in entry:
        year = entry["year"]

    #게제 월
    month= "NA"
    if "month" in entry:
        month = entry["month"]

    #페이지
    pages = "NA"
    if "pages" in entry:
        pages = entry["pages"]

    #권
    volume = "NA"
    if "volume" in entry:
        volume = entry["volume"]

    #이슈
    issue = "NA"
    if "issue" in entry:
        issue = entry["issue"]

    #게제 저널 ISSN
    issn = "NA"
    if "issn" in entry:
        issn = entry["issn"]
        issn = "-".join([issn[:4], issn[4:]])

    #논문 DOI
    doi = "NA"
    if "doi" in entry:
        doi = entry["doi"]

    print("{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(title, journal, issn, doi, volume, issue, year, month, pages, Nauthor, author))

# Python 기본 문법 확인
# 현재 코드는 [논문 제목, 저널 이름, ISSN, DOI, Vol, Issue, 게제 연도, 게제 월, 페이지, 총 저자 수, 저자] 데이터 출력
# 미리 등록된 저자와 논문 저자와 비교하여 일치하는 경우만 저자 출력
