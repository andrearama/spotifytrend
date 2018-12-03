#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 07:48:08 2018

@author: andrea
"""
import numpy as np 

def get_streams_and_position(song, stream_num, pos_num):
    song_stream = stream_num.loc[:,song]
    song_pos = pos_num.loc[:,song]
    tmp = song_stream.loc[song_stream.notnull()] #get the streaming
    tmp2 = song_pos.loc[song_stream.notnull()]   #get the position

    return tmp,tmp2

def standardize_serie(trend, rank = False, fixed_length = 150):
    if rank:
        i = 1
    else:
        i = 0
        trend= trend[i]/max(trend[i])
    trend = np.array(trend)        
    if len(trend)>=fixed_length:
       return trend[:fixed_length]
    else:
        result = np.zeros(fixed_length) + 0.00000001
        result[:trend.shape[0]] = trend
    return result


def get_cluster_variance(D,indexes,medoid_index):
    return np.sum(np.square(D[indexes, medoid_index]))
    
def get_total_variance(D,C,M):
    V=0
    for i in range(len(M)):
        medoid_index =M[i]
        indexes = C[i]
        V=V+get_cluster_variance(D,indexes,medoid_index)
    return V