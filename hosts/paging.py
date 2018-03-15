# coding: utf-8
import os
import hashlib
import random
import datetime
import ConfigParser
from django.core.paginator import Paginator
class paging():
	'''分页函数'''
        def __init__(self,page,pagenum,select_result):
                self.page = int(page)
                self.pagenum = int(pagenum)
                self.select_result = select_result
                self.p = Paginator(self.select_result,self.pagenum)

        def pt(self):
                '''共有多少条数据'''
                return self.p.count

        def pn(self):
                '''总页数'''
                return self.p.num_pages

        def pr(self):
                '''获取页码列表'''
                return self.p.page_range

        def pl(self):
                '''第page页的数据列表'''
                return self.p.page(self.page).object_list

        def pp(self):
                '''是否有上一页'''
                return self.p.page(self.page).has_previous()

        def np(self):
                '''是否有下一页'''
                return self.p.page(self.page).has_next()

        def ppn(self):
                '''上一页页码号'''
                if self.page <= 1:
                        return '1'
                else:
                        return self.p.page(self.page).previous_page_number()

        def npn(self):
                '''下一页页码号'''
                if self.p.page(self.page).has_next() == False:
                        return self.page
                else:
                        return self.p.page(self.page).next_page_number()

