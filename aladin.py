import requests
from bs4 import BeautifulSoup


def extract_page_num(keyword):
    page = 1
    url = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&KeyWord={keyword}&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord={keyword}&KeyLastWord={keyword}&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&chkKeyISBN=&chkKeyTag=&chkKeyTOC=&chkKeySubject=&ViewRowCount=50&page={page}"
    aladin_result = requests.get(url)
    aladin_soup = BeautifulSoup(aladin_result.text, 'html.parser')

    numbox_last = aladin_soup.find("div", {"class": "numbox_last"})
    if numbox_last == None:
        print("페이지 1개만 존재!")
        href = 1
        return int(href)

    a = numbox_last.find('a')

    href = a['href']

    if len(href) == 26:
        href = href[-5:-2]
    elif len(href) == 25:
        href = href[-4:-2]
    elif len(href) == 24:
        href = href[-3:-2]
    elif len(href) > 26:
        print("Too Many Pages!!! Maximum Page is 999")
        href = 999
    else:
        print("Pages Num Is Something Wrong!!")
        href = -1

    return int(href)


def extract_tag(keyword, page):
    url = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&KeyWord={keyword}&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord={keyword}&KeyLastWord={keyword}&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&chkKeyISBN=&chkKeyTag=&chkKeyTOC=&chkKeySubject=&ViewRowCount=50&page={page}"
    aladin_result = requests.get(url)
    aladin_soup = BeautifulSoup(aladin_result.text, 'html.parser')
    search_result = aladin_soup.find(id='Search3_Result')
    ss_book_box = search_result.find_all('div', {'class': 'ss_book_box'})

    tag_result_list = []

    for ss_book_list in ss_book_box:
        span = ss_book_list.find('span', {'style': 'font-size: 14px;'})
        if span == None:
            print('[extract_tag] NoneType 발견!!')
        else:
            span = span.get_text()
            tag_result_list.append(span)

    return tag_result_list


def extract_title(keyword, page):
    url = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&KeyWord={keyword}&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord={keyword}&KeyLastWord={keyword}&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&chkKeyISBN=&chkKeyTag=&chkKeyTOC=&chkKeySubject=&ViewRowCount=50&page={page}"
    aladin_result = requests.get(url)
    aladin_soup = BeautifulSoup(aladin_result.text, 'html.parser')
    search_result = aladin_soup.find(id='Search3_Result')
    ss_book_box = search_result.find_all('div', {'class': 'ss_book_box'})

    title_result_list = []

    for ss_book_list in ss_book_box:
        b = ss_book_list.find('b')
        if b == None:
            print('[extract_title] NoneType 발견!!')
        else:
            b = b.get_text()
            title_result_list.append(b)

    return title_result_list


def extract_price(keyword, page):
    url = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&KeyWord={keyword}&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord={keyword}&KeyLastWord={keyword}&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&chkKeyISBN=&chkKeyTag=&chkKeyTOC=&chkKeySubject=&ViewRowCount=50&page={page}"
    aladin_result = requests.get(url)
    aladin_soup = BeautifulSoup(aladin_result.text, 'html.parser')
    search_result = aladin_soup.find(id='Search3_Result')
    ss_book_box = search_result.find_all('div', {'class': 'ss_book_box'})

    price_result_list = []

    for ss_book_list in ss_book_box:
        span = ss_book_list.find('span', {'class': 'ss_p2'})
        b = span.find('b')
        if b == None:
            print('[extract_price] NoneType 발견!!')
        else:
            b = b.get_text()
            price_result_list.append(b)

    return price_result_list


def extract(keyword):
    last_page = extract_page_num(keyword)

    if last_page == -1:
        print("에러발견!!!")
    else:
        book_list = []

        for page in range(last_page):
            print(f"키워드 {keyword}로 알라딘 추출중... 페이지 : {page+1} / {last_page}")

            tags = extract_tag(keyword, page+1)
            titles = extract_title(keyword, page+1)
            prices = extract_price(keyword, page+1)

            for tag, title, price in zip(tags, titles, prices):
                book_list.extend([[tag, title, price]])

    return book_list
