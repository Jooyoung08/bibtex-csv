# 개요
--------

논문의 정보를 csv 포맷으로 내보내는 프로그램.

# 테스트 환경
--------

## OS

Rocky Linux 9.3

## Python

이 코드는 Python 3.9.18 에서 테스트 되었음.

## BibTex

BibTex 파일을 생성하는데 다음과 같은 프로그램을 사용.
BibTex에 적절한 정보를 생성하기 위해 적절한 셋팅이 필요함.

### Zotero

Zotero 6.0.30
https://www.zotero.org/

### Zotero Extension

Better BibTex for Zotero 6.7.160
https://retorque.re/zotero-better-bibtex/

# 사용법
--------

## 코드 다운로드

### git 설치 (optional)

#### Rocky Linux/Cent OS/Redhat

```sh
sudo dnf install git
```

#### Ubuntu

```sh
sudo apt-get install git
```

#### Mac

git이 기본적으로 설치되지 않은 경우,
brew 패키지 매니져를 이용하여 git 설치
참조 : https://brew.sh/ko/

```sh
brew install git
```

### git을 통한 다운로드

터미널(Terminal)을 실행하고,
이 코드를 다운로드할 위치로 이동

```sh
git clone https://github.com/Jooyoung08/bibtex-csv.git
```

### GitHub에서 소스 다운로드

다운로드가 완료되면 터미널(Terminal)을 실행하고,

```sh
cd ~/Downloads
unzip bibtex-csv-master.zip
```

## 코드 편집

해당 디렉토리로 이동

```sh
cd bibtex-csv
```

코드 편집

```sh
vi conv.py
```
bibtex 파일에 저장된 정보를 확인 후, 개인 목적에 맞게 코드를 편집.

### 코드 편집이 안되는 경우

파일의 권한 확인 후, 변경

## 실행

```sh
python3 conv.py < test.bib > output.csv
```

---

# 기타

## 샘플 bibtex 파일에 포함된 내용

현재 테스트 용도로 만들어진 BibTex(test.bib)에 포함된 정보

| Item | Details |
| ---- | ----- |
| abstract | 초록 |
| author | 저자 |
| doi | DOI |
| issn | ISSN |
| issue | Issue |
| journal | 저널 이름 |
| keywords | 핵심어 |
| month | 게제 월 |
| pages | 논문 페이지 |
| publisher | 출판사 이름 |
| title | 논문 제목 |
| volume | 권(Vol.) |
| year | 게제 연도 |

---

## 윈도우에서 사용 방법

### 파이썬 설치

1. 윈도우 Microsoft Store 실행

2. Python 검색

3. 파이썬 최신 버전 설치

### 코드 실행

1. Windows PowerShell 실행

2. 코드가 있는 디렉토리로 이동

3. 코드 실행

```sh
cmd \c 'python conv.py < test.bib > output.csv'
```
