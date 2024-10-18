import re

input_f = input("输入单个 lrc 文件路径：")
file = input_f
data = open(file, "r", encoding="utf-8").read()
data = data.strip().split("\n")

def lrc_merge(lrc_input):
    merged_lrc = []
    last_time = None
    last_line = None

    for lines in lrc_input:
        ma_time = re.compile(r'\[\d{2}:\d{2}\.\d{2}\]')
        time = ma_time.match(lines)

        ma_lrc_dur = re.compile(r'<\d{2}:\d{2}\.\d{2}>')
        lrc_dur = ma_lrc_dur.findall(lines)

        if lrc_dur:
            for dur in lrc_dur:
                lines = lines.replace(dur,'')

        line = lines

        if time:
            time = time.group()
            current_lrc = lines.replace(time,'').replace('【','').replace('】','')
        else:
            time = '' # 使 time != last_time
            current_lrc = lines.replace('【','').replace('】','')

        if time == last_time:
            if last_line.replace(time,'') != '':
                merged_lrc.pop() # 删除重复歌词
                merged_line = last_line + '（' + current_lrc + '）'
                merged_lrc.append(merged_line)
            else:
                last_line = last_line + current_lrc # 处理有三行是同一时间，首行为空行的情况
        else:
            if current_lrc == '' and time != None:
                merged_lrc.append(line + '.')
            else:
                merged_lrc.append(line) #merged_lrc.append(''.join([time + current_lrc])
            last_line = line
            last_time = time

    return merged_lrc

lrc_list = lrc_merge(data)

for res in lrc_list:
    print(res)
