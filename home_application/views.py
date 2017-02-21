# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
from account.decorators import login_exempt


@login_exempt # wzz:默认所有请求均需要登录，如果不启用登录验证可以加这个装饰器。
def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')


