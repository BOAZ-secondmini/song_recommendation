import test
from flask import Flask, request, jsonify


application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello goorm!"

@application.route("/music",methods=['POST'])
def music():
    req = request.get_json()
    
    
    content = req['userRequest']['utterance']
    print(content)

    music = test.test(content)
    
    print(music)
    
    # 답변 텍스트 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": music
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)