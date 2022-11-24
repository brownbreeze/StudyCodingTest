import datetime
g_ch_dict = {
    'C#':'B',
    'C':'A',
    'D#':'D',
    'D':'C',
    'E':'E',
    'F#':'G',
    'F':'F',
    'G#':'I',
    'G':'H',
    'A#':'K',
    'A':'J',
    'B':'L'        
}

def get_music_melody(m):
    global g_ch_dict
    m_list = list()
    i = 0 
    while True:
        if i >= len(m) : break
        if i+1 < len(m) and  m[i+1]=='#' and m[i:i+2] in g_ch_dict:
            m_list.append(g_ch_dict[m[i:i+2]])
            i = i+2
            continue
        if m[i] in g_ch_dict:
            m_list.append(g_ch_dict[m[i]])
        i = i+1
    return m_list

def solution(m, musicinfos):
    correct_list = list()
    m_list = get_music_melody(m)
    m_list = ''.join(m_list)
    for musicinfo in musicinfos:
        datas = musicinfo.split(',')
        start_time = datetime.datetime.strptime(datas[0], '%H:%M')
        end_time = datetime.datetime.strptime(datas[1], '%H:%M')
        running_time = (int)((end_time-start_time).total_seconds() // 60)
    
        ful_music = get_music_melody(datas[3])
        ful_music = ''.join(ful_music)
        real_song = ''
        real_song = real_song + (ful_music * (int)(running_time//len(ful_music)))
        real_song = real_song + ful_music[:running_time-len(real_song)]
        
        if len(real_song) == 0 : continue
        idx = real_song.find(m_list)
        if idx == -1 : continue
        correct_list.append({'time':running_time,'title':datas[2]})
        
    if len(correct_list) == 0: return "(None)"
    correct_list = sorted(correct_list, key=lambda d: d['time'], reverse=True)
    return correct_list[0]['title']
