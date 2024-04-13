def solution(N, stages):
    
    # 스테이지별 실패율 저장
    fail_rates = []

    for stage in range(1, N + 1):
        players = len([s for s in stages if s >= stage])
        if players == 0:
            fail_rate = 0
        else:
            fail_rate = stages.count(stage) / players
        fail_rates.append((stage, fail_rate))

    fail_rates.sort(key=lambda x: (-x[1], x[0]))
    return [stage[0] for stage in fail_rates]