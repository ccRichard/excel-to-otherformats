# -*- coding: utf-8 -*-
# Version   : python3
# Date       : 2018-3-16 14:53:41
# Author     : cc
# Description: redmine operation


import os
import sys
sys.path.append(os.path.split(sys.path[0])[0])
from redminelib import Redmine
import exceltoformats as etw


if __name__ == "__main__":

    # 获取GM指令表格字符
    x = etw.XlsxToWiki("/test.xlsx")
    gm_str = x.out_put()

    # 访问redmine的配置
    url = "http://redmine"
    api_key = "asdfsdfs"
    redmine = Redmine(url, key=api_key, requests={"verify": False})

    # 项目id为1
    project = redmine.project.get(1)

    # 获取GM wiki对象
    gm_wiki = project.wiki_pages.get("Test")
    gm_wiki.text = gm_str
    gm_wiki.save()



