# _*_ codign:utf8 _*_
"""====================================
@Author:Sadam·Sadik
@Email：1903249375@qq.com
@Date：2022/12/23
@Software: PyCharm
@disc:
======================================="""
import requests
from lxml import etree


def generate(code: int):
    resp = requests.get(f"http://ip.bczs.net/city/{code}", headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    })
    html = etree.HTML(resp.text)
    trs = html.xpath("//tbody/tr")
    with open(f"targets-{code}.txt", "w", encoding="utf-8") as f:
        for i, tr in enumerate(trs):
            tds = tr.xpath(".//td")
            start = tds[0].xpath(".//a")[0].text
            end = tds[1].text
            target = f"{start}-{end}"
            f.write(target + "\n")
            print(f"{i}. {target}")


if __name__ == '__main__':
    generate(650100)
