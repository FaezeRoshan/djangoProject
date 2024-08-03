

from celery import shared_task
from .models import New, Tag
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse

@shared_task
def addnews():
    html= requests.get('https://www.zoomit.ir/')
    soup = BeautifulSoup(html.content, 'html.parser')
    heading = soup.find_all('a',{'class': "link__CustomNextLink-sc-1r7l32j-0 eoKbWT "
                                      "BrowseArticleListItemDesktop__WrapperLink-zb6c6m-6 bzMtyO"}, href=True)
    hrefs=[]
    for header in heading:
        hrefs.append(header["href"])

    newslist = []
    for href in hrefs:
        res = requests.get(href)
        soup = BeautifulSoup(res.content, 'html.parser')
        titletag = soup.find('h1',{'class': "typography__StyledDynamicTypographyComponent-t787b7-0 fzMmhL"})
        title = titletag.string if titletag else "عنوان نامشخص"
        paragraph = soup.find_all('p', {'class': "typography__StyledDynamicTypographyComponent-t787b7-0 fZZfUi "
                                            "ParagraphElement__ParagraphBase-sc-1soo3i3-0 gOVZGU"})
        texts = [p.get_text() for p in paragraph]
        text = "".join(texts)
        tags = soup.find_all('span', {'class': "typography__StyledDynamicTypographyComponent-t787b7-0"
                                                  " cHbulB"})
        tag = [sp.get_text() for sp in tags]
        source = href
        newslist.append({
           "title": title,
           "text": text,
           "tags": tag,
           "source": source
        })

    for item in newslist:
        news = New.objects.create(
            title= item["title"],
            text= item["text"],
            source= item["source"]
        )
        for tagname in item["tags"]:
            tag, created = Tag.objects.get_or_create(tag= tagname)
            news.tags.add(tag)

        news.save()



    return JsonResponse({'message': 'News added successfully.'})







