answer, check_list = [], []
report_dict = {}
for report_id in id_list:
    report_dict[report_id] = []
for case in report:
    report_id, report_name = case.split()
    if report_name not in report_dict[report_id]:
        report_dict[report_id].append(report_name) 
        check_list.append(report_name) 
        cnt_dict = Counter(check_list) 
        for report_id in id_list: answer.append(len([check for check in report_dict[report_id] if cnt_dict[check] >= k]))
