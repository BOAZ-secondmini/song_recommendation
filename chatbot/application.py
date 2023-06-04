# import test
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


import end_to_end
from flask import Flask, request, jsonify


application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello BOAZ!"

@application.route("/music",methods=['POST'])
def music():
    req = request.get_json()
    
    
    content = req['userRequest']['utterance']
    print(content)

    music = end_to_end.main(content)
    
    print("호출 성공")
    
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
