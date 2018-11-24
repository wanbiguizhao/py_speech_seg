# -*- coding:UTF-8 -*-

from __future__ import print_function
import speech_segmentation as seg
import os


def segment_mp3_file(filepath,filename):
    """
    filepath 文件的路径mp3/11.mp3
    filename 文件的名称不包含类型名（.mp3）
    """
    frame_size = 500
    frame_shift = 300
    sr = None
    seg_point = seg.multi_segmentation(filepath, sr, frame_size, frame_shift, plot_seg=False, save_seg=False,
                                    cluster_method='bic')
    print('The segmentation point for this audio file is listed (Unit: /s)',seg_point)
    import os
    import os.path
    from pydub import AudioSegment
    song=AudioSegment.from_mp3(filepath)
    i=1
    beg_point=0
    pianyi=200
    seg_len_list=[]
    for x in seg_point:
        end_point=int(x*1000)
        seg_len_list.append([end_point-beg_point,beg_point,end_point])
        segment=song[beg_point+pianyi:end_point+pianyi]
        beg_point=end_point
        i=i+1
    segment=song[end_point:]
    seg_len_list.append([len(song)-beg_point,beg_point,len(song)])#三元组数据,时间长短，开始时间，结束时间
    #segment.export("save_audio_mp3/"+filename+"_{:0>2d}_{:0>3d}_{:0>6d}_{:0>6d}_".format(i,int((end_point-beg_point)/100),beg_point+pianyi,end_point+pianyi)+".mp3",format="mp3")
    #segment.export("save_audio_mp3/"+filename+"_{:0>2d}_{:0>3d}_{:0>6d}_{:0>6d}_".format(i,int((len(song)-beg_point)/100),beg_point+pianyi,len(song))+".mp3",format="mp3")
    
    need_merge=False
    merge_seg_list=[]
    for x in seg_len_list:
        if need_merge:
            merge_seg_list[-1][0]=x[0]+merge_seg_list[-1][0]
            merge_seg_list[-1][-1]=merge_seg_list[-1][-1]
            need_merge=False
        else:
            if x[0]<5500:
                need_merge=True
            merge_seg_list.append(x)
    save_seg_mp3(song,filename,merge_seg_list)
    return merge_seg_list
    
    

def save_seg_mp3(song_np,filename,merge_seg_list):
    i=1
    for y in merge_seg_list:
        pianyi=200
        beg_point,end_point=y[1],y[2]
        segment=song_np[beg_point:end_point]#分割的长度
        segment.export("save_audio_mp3/"+filename+"_{:0>2d}_{:0>3d}_{:0>6d}_{:0>6d}_".format(i,int((end_point-beg_point)/100),beg_point+pianyi,end_point+pianyi)+".mp3",format="mp3")
        i=i+1
    


def get_mp3_list(mp3_path="mp3"):
    return  os.listdir(mp3_path)

import json
def batch_segment_mp3():
    mp3_filename_list=get_mp3_list(mp3_path="mp3")
    dump_json={}
    for file in mp3_filename_list:
        filename=file.replace(".mp3","")# tingvoa.com_03.mp3 -->tingvoa.com_03
        merge_seg_list=segment_mp3_file("mp3/"+file,filename)
        dump_json[filename]=[ [x[0],x[1],x[2],0,0] for x in  merge_seg_list ]
    with open("batch.json","w") as jf:
        json.dump(dump_json,jf,indent=4)



if __name__ == '__main__':
    batch_segment_mp3()

