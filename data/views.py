from django.shortcuts import render
from . import models
from .models import EngineDiagnosticsRecord
from . import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.http import HttpResponseRedirect
from .forms import EngineDiagnosticsForms

def index(request):
    context = {}
    return render(request, 'index.html', context)


def test_page(request):
    test_data = list(models.BorgwardEngineDiagnostics.objects.values('parts', 'problem_description'))
    context = {
        "data": test_data
    }
    return render(request, 'test_page.html', context)


# 根据提交的故障码和故障现象，查询到的结果形成json格式
def engine_fault_data_reload(request):
    if request.method == "GET":
        # 查询刚存入数据库的数据，记录里最后一条数据即为刚存入的数据
        fault_code = models.EngineDiagnosticsRecord.objects.values_list("fault_code", flat=True).last()
        fault_phenomenon = models.EngineDiagnosticsRecord.objects.values_list("fault_phenomenon", flat=True).last()
        # 转化字符串为列表
        fault_code = eval(fault_code)
        fault_phenomenon = eval(fault_phenomenon)

        # 根据最新的故障码查询维修方案
        fault_code_result = []
        for item in fault_code:
            # print('item=', item)
            fault_code_eachtime = models.EngineFaultCode.objects.values("fault_code", "interpretation",
                "fault_cause", "diagnostic_scheme").filter(fault_code=item)
            fault_code_result.extend(list(fault_code_eachtime))
        for dic in fault_code_result:
            # 合并故障码及其说明为一组数据
            dic["fault_phenomenon"] = dic["fault_code"] + " " + dic['interpretation']
            del dic['fault_code']
            del dic['interpretation']

        # 根据最新的故障现象查询维修方案
        fault_phenomenon_result = fault_code_result
        for item in fault_phenomenon:
            # print('item=', item)
            fault_phenomenon_eachtime = models.EngineFaultPhenomenon.objects.values("fault_phenomenon", "fault_cause",
                 "diagnostic_scheme").filter(fault_phenomenon=item)
            fault_phenomenon_result.extend(list(fault_phenomenon_eachtime)) # 故障现象的结果存入故障码结果后
        print("fault_phenomenon_result =", fault_phenomenon_result)
        return HttpResponse(json.dumps(fault_code_result, ensure_ascii=False), content_type="application/json")


# 取故障码和故障现象用于下拉选择，distinct去重
def diagnosis(request):
    data = models.EngineFaultCode.objects.values('fault_code').distinct()
    data2 = models.EngineFaultPhenomenon.objects.values('fault_phenomenon').distinct()

    context = {
        "fault_code": data,
        "fault_phenomenon": data2
    }
    # POST请求时，保存提交的记录到数据库
    if request.method == "GET":
        return render(request, "diagnosis.html", context)
    elif request.method == "POST":
        # 实例化record
        record = EngineDiagnosticsRecord()
        # 将用户输入数据存储
        record.time = request.POST["time"]
        record.location = request.POST["location"]
        record.vehicle_model = request.POST["vehicle_model"]
        record.vin = request.POST["vin"]
        record.engine = request.POST["engine"]
        record.fault_code = request.POST.getlist("fault_code")
        record.fault_phenomenon = request.POST.getlist("fault_phenomenon")
        # 保存
        record.save()
        return render(request, 'diagnosis.html', context)


# 测试用
def user_record(request):

    data = models.EngineDiagnosticsRecord.objects.filter.last()
    print("data=", data)
    context = {
        "record_data":data
    }
    return render(request, 'diagnosis.html', context)


# 全部的fault_code数据转化为json格式
def engine_fault_code_data(request):
    if request.method == "GET":
        objects = models.EngineFaultCode.objects.all()
        dic = [obj.engine_fault_code_dict() for obj in objects]
        return HttpResponse(json.dumps(dic, ensure_ascii=False), content_type="application/json")


# 显示各列表信息
def lists(request, table):
    # 从根据不同的请求，来获取相应的数据,并跳转至相应页面
    if table == 'tbox':
        raw_data = models.Tboxdata.objects.all()
        list_template = 'tbox_data.html'
        sub_title = 'tbox数据'

        # 通过GET方法从提交的URL来获取相应参数
        if request.method == 'GET':
            # 建立一个空的参数的字典
            kwargs = {}
            # 建立一个空的查询语句
            query = ''
            # 提交过来的GET值是一个迭代的键值对
            for key, value in request.GET.items():
                # 刨去其中的token和page选项
                if key != 'csrfmiddlewaretoken' and key != 'page':
                    # 由于线路和设备的外键均与node表格有关，当查询线路中的用户名称或设备信息中的使用部门时，可以直接通过以下方式跨表进行查找
                    if key == 'node':
                        kwargs['node__node_name__contains'] = value
                        # 该query用于页面分页跳转时，能附带现有的搜索条件
                        query += '&' + key + '=' + value
                    # 其余的选项均通过key来辨别
                    else:
                        kwargs[key + '__contains'] = value
                        # 该query用于页面分页跳转时，能附带现有的搜索条件
                        query += '&' + key + '=' + value
            # 通过元始数据进行过滤，过滤条件为健对值的字典
            data = raw_data.filter(**kwargs)
        # 如果没有从GET提交中获取信息，那么data则为元始数据
        else:
            data = raw_data

    # 将分页的信息传递到展示页面中去
    data_list, page_range, count, page_nums = pagination(request, data)
    # 建立context字典，将值传递到相应页面
    context = {
        'data': data_list,
        'table': table,
        'query': query,
        'page_range': page_range,
        'count': count,
        'page_nums': page_nums,
        'page_title': '基础数据',
        'sub_title': sub_title,
    }
    # 跳转到相应页面，并将值传递过去
    return render(request, list_template, context)


# 分页函数
def pagination(request, queryset, display_amount=15, after_range_num=5, before_range_num=4):
    # 按参数分页
    try:
        # 从提交来的页面获得page的值
        page = int(request.GET.get("page", 1))
        # 如果page值小于1，那么默认为第一页
        if page < 1:
            page = 1
        # 若报异常，则page为第一页
    except ValueError:
        page = 1
    # 引用Paginator类
    paginator = Paginator(queryset, display_amount)
    # 总计的数据条目
    count = paginator.count
    # 合计页数
    num_pages = paginator.num_pages
    # 当用户提交的页码不是整数时，提取第一页记录。当用户输入的页码太大时，只提取最后一页记录。
    objects = paginator.get_page(page)
    # 根据参数配置导航显示范围
    temp_range = paginator.page_range

    # 如果页面很小
    if (page - before_range_num) <= 0:
        # 如果总页面比after_range_num大，那么显示到after_range_num
        if temp_range[-1] > after_range_num:
            page_range = range(1, after_range_num + 1)
        # 否则显示当前页
        else:
            page_range = range(1, temp_range[-1] + 1)
    # 如果页面比较大
    elif (page + after_range_num) > temp_range[-1]:
        # 显示到最大页
        page_range = range(page - before_range_num, temp_range[-1] + 1)
    # 否则在before_range_num和after_range_num之间显示
    else:
        page_range = range(page - before_range_num + 1, page + after_range_num)
    # 返回分页相关参数
    return objects, page_range, count, num_pages



