#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-14 14:58:26
# @Author  : LYF (hflyf123@outlook.com)
# @Link    : https://github.com/hflyf123
# 我自己为了复习，再次重复一遍建立广播站问题
import os

cities_needed = set(["北京", "上海", "广州", "深圳", "杭州", "南京", "合肥", "武汉"])
stations = {}
stations["一套"] = set(["上海", "广州", "杭州"])
stations["二套"] = set(["广州", "深圳", "南京", "合肥", "武汉"])
stations["三套"] = set(["北京", "上海", "广州", "深圳"])
stations["四套"] = set(["杭州", "南京", "合肥", "武汉"])
stations["五套"] = set(["广州", "深圳"])
final_stations_needed = set()
while cities_needed:
    best_station = None
    best_covered = set()
    for station, city in stations.items():
        covered = cities_needed & city
        if len(covered) > len(best_covered):
            best_station = station
            best_covered = covered
    cities_needed -= best_covered
    final_stations_needed.add(best_station)

print(final_stations_needed)
