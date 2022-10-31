from konlpy.tag import Okt  # pip install konlpy
from collections import Counter


def getcommon(data, n=10, debug=False):
    tmp = ""
    if debug:
        for r in data:
            tmp += r["title"]
    else:
        for r in data:
            tmp += r.title
    okt = Okt()  # Okt 함수를 이용해 형태소 분석
    line = []
    n_adj = okt.nouns(tmp)
    # 제외할 단어 추가
    stop_words = "모집 채용 구함 구합 구인 직원 공고"  # 추가할 때 띄어쓰기로 추가해주기
    stop_words = set(stop_words.split(" "))
    n_adj = [word for word in n_adj if not word in stop_words]
    # 가장 많이 나온 단어 1000개 저장
    counts = Counter(n_adj)
    tags = counts.most_common(n)
    return tags


#########################################

if __name__ == "__main__":
    import pymysql

    con = pymysql.connect(
        host="localhost",
        user="jiheon",
        password="",
        db="test",
        cursorclass=pymysql.cursors.DictCursor,
    )
    cur = con.cursor()
    cur.execute(
        """
        SELECT title FROM announce;
    """
    )
    res = cur.fetchall()
    print(getcommon(res, n=100, debug=True))
