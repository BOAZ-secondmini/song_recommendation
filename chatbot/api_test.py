
# 문장을 입력받아 거꾸로 출력하는 함수
def test(content):
    S = ""
    
    for i in content:
        S = i + S
    return S