#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-14 08:54:24
# @Author  : LYF (hflyf123@outlook.com)
# @Link    : https://github.com/hflyf123
# 贪婪算法解决广播台覆盖的问题
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kone"] = set(["id", "nv", "ut"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
