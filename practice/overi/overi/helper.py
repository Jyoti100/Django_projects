from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def pg_records(request, list, num):
    paginator =Paginator(list, num)
    page = request.GET.get('page')
    try:
        # p1 = paginator.page(1)
        page_object = paginator.page(page)
    except PageNotAnInteger:
        page_object=paginator.page(1)
    except EmptyPage:
        page_object = paginator.page(paginator.num_pages)

    return page_object