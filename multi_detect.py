# -*- coding:UTF-8 -*-

from __future__ import print_function
import speech_segmentation as seg

frame_size = 512
frame_shift = 256
sr = None

seg_point = seg.multi_segmentation("tingvoa.com_02.mp3", sr, frame_size, frame_shift, plot_seg=True, save_seg=True,
                                   cluster_method='bic')
print('The segmentation point for this audio file is listed (Unit: /s)',seg_point)


from pydub import AudioSegment
song=AudioSegment.from_mp3("tingvoa.com_02.mp3")
i=1
beg_point=0
for x in seg_point:
    end_point=x*1000
    segment=song[last_point:end_point]
    segment.export("save_audio/{:0>2d}_{:0>7d}_{:0>7d}_".format(i,beg_point,last_point)+".mp3",format="mp3")
    beg_point=end_point
    i=i+1
segment=song[end_point:]
segment.export("save_audio/{:0>2d}_{:0>7d}_{:0>7d}_".format(i,beg_point,len(segment))+".mp3",format="mp3")







