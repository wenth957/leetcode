states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {}
stations['kone'] = set(["id", 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])
final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()
    # 当需要覆盖的州不为空时，选出当前最好情况
    for station, states_for_station in stations.items():
        # 遍历电台信息
        covered = states_needed & states_for_station
        # 计算交集，可覆盖的州
        if len(covered) > len(states_covered):
            # 如果可覆盖多于已覆盖
            best_station = station
            states_covered = covered
            # 能够覆盖的
    final_stations.add(best_station)
    states_needed -= states_covered
    # 在新的集合上重新进行选择
print(final_stations)
