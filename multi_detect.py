# -*- coding:UTF-8 -*-

from __future__ import print_function
import speech_segmentation as seg



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
    "".split
    for x in seg_point:
        end_point=int(x*1000)
        segment=song[beg_point+150:end_point+150]
        segment.export("save_audio_mp3/{0}_{:0>2d}_{:0>6d}_{:0>6d}_".format(filename,i,beg_point+350,end_point+350)+".mp3",format="mp3")
        beg_point=end_point
        i=i+1
    segment=song[end_point:]
    segment.export("save_audio_mp3/{0}_{:0>2d}_{:0>6d}_{:0>6d}_".format(filename,i,beg_point+350,len(song))+".mp3",format="mp3")


def get_mp3_list(mp3_path="mp3"):
    return  os.listdir(mp3_path)
    
def batch_segment_mp3():
    mp3_filename_list=get_mp3_list(mp3_path="mp3")
    
    for file in mp3_filename_list:
        filename=file.replace(".mp3",)# tingvoa.com_03.mp3 -->tingvoa.com_03
        segment_mp3_file("mp3/"+file,filename)


if __name__ == '__main__':
    mp3_filename_list=get_mp3_list()

