# 用于测试单独函数或数据，与项目无关

fault_code_result =  [{'fault_code': 'P000B 26', 'interpretation': '排气VVT运行故障（迟缓）', 'fault_cause': '机油压力过低', 'diagnostic_scheme': '检查怠速、低转速机油压力'},
                      {'fault_code': 'P000B 26', 'interpretation': '排气VVT运行故障（迟缓）', 'fault_cause': '排气OCV阀故障','diagnostic_scheme': '检查/更换OCV阀'},
                      {'fault_code': 'P000B 26', 'interpretation': '排气VVT运行故障（迟缓）', 'fault_cause': 'VVT故障','diagnostic_scheme': '检查/更换VVT'},
                      {'fault_code': 'P0017 78', 'interpretation': '排气凸轮轴位置跳动', 'fault_cause': '机油压力过低', 'diagnostic_scheme': '检查怠速、低转速机油压力'},
                      {'fault_code': 'P0017 78', 'interpretation': '排气凸轮轴位置跳动', 'fault_cause': '排气OCV阀故障', 'diagnostic_scheme': '检查/更换OCV阀'},
                      {'fault_code': 'P0017 78', 'interpretation': '排气凸轮轴位置跳动', 'fault_cause': 'VVT故障','diagnostic_scheme': '检查/更换VVT'}]

for dic in fault_code_result:
    dic["fault_code&interpretation"] = dic["fault_code"] + dic['interpretation']
    del dic['fault_code']
    del dic['interpretation']
print(fault_code_result)

# for git remote