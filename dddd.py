def solution(N, S):
    def parse_seat(seat):
        row = int(seat[:-1]) - 1
        column = ord(seat[-1]) - ord('A')
        return row, column

    def update_seats(seats, occupied_seats):
        for seat in occupied_seats:
            row, column = parse_seat(seat)
            seats[row][column] = False

    # 좌석 생성
    seats = [[True] * 10 for _ in range(N)]

    # 주어진 좌석 정보로 좌석 상태 업데이트
    occupied_seats = S.split()
    update_seats(seats, occupied_seats)

    count = 0
    t = ["1234", "3456", "5678"]
    for s in seats:
        for strs in t:
            valid = True
            for c in strs:
                if not s[int(c)]:
                    valid = False
            if valid:
                count += 1

    print(count)

# 예시 테스트

if __name__ == '__main__':
    print(solution(2, '1A 2F 1C'))
    # print(solution(22, '1A 3C 2B 20G 5A'))
