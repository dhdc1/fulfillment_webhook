import json
import os

from flask import Flask
from flask import request
from flask import make_response
import json
import random

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    # Parsing the POST request body into a dictionary for easy access.
    req_dict = json.loads(request.data)
    print(req_dict)
    # Accessing the fields on the POST request boduy of API.ai invocation of the webhook
    intent = req_dict["queryResult"]["intent"]["displayName"]

    if intent == 'BMI - custom - yes':
        bmi = req_dict["queryResult"]["parameters"]["w"] / (req_dict["queryResult"]["parameters"]["h"] / 100) ** 2
        result = "ดัชนีมวลกายของคุณคือ " + str(round(bmi, 2))

    else:

        n = random.randint(100, 110)
        result = {
            "type": "sticker",
            "packageId": "1",
            "stickerId": str(n)
        }

    res = makeWebhookResult(result)

    return res


def makeWebhookResult(result):
    return {
        'fulfillmentMessages': [
            {
                "payload": {
                    "line": {
                        "type": "flex",
                        "altText": "Flex Message",
                        "contents": {
                            "type": "carousel",
                            "contents": [
                                {
                                    "type": "bubble",
                                    "hero": {
                                        "type": "image",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_5_carousel.png",
                                        "size": "full",
                                        "aspectRatio": "20:13",
                                        "aspectMode": "cover"
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Arm Chair, White",
                                                "size": "xl",
                                                "weight": "bold",
                                                "wrap": True
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "$49",
                                                        "flex": 0,
                                                        "size": "xl",
                                                        "weight": "bold",
                                                        "wrap": True
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": ".99",
                                                        "flex": 0,
                                                        "size": "sm",
                                                        "weight": "bold",
                                                        "wrap": True
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Add to Cart",
                                                    "uri": "https://linecorp.com"
                                                },
                                                "style": "primary"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Add to whishlist",
                                                    "uri": "https://linecorp.com"
                                                }
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "hero": {
                                        "type": "image",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_6_carousel.png",
                                        "size": "full",
                                        "aspectRatio": "20:13",
                                        "aspectMode": "cover"
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Metal Desk Lamp",
                                                "size": "xl",
                                                "weight": "bold",
                                                "wrap": True
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "flex": 1,
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "$11",
                                                        "flex": 0,
                                                        "size": "xl",
                                                        "weight": "bold",
                                                        "wrap": True
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": ".99",
                                                        "flex": 0,
                                                        "size": "sm",
                                                        "weight": "bold",
                                                        "wrap": True
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "text",
                                                "text": "Temporarily out of stock",
                                                "flex": 0,
                                                "margin": "md",
                                                "size": "xxs",
                                                "color": "#FF5551",
                                                "wrap": True
                                            }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Add to Cart",
                                                    "uri": "https://linecorp.com"
                                                },
                                                "flex": 2,
                                                "color": "#AAAAAA",
                                                "style": "primary"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Add to wish list",
                                                    "uri": "https://linecorp.com"
                                                }
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "See more",
                                                    "uri": "https://linecorp.com"
                                                },
                                                "flex": 1,
                                                "gravity": "center"
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                }
            },
            {
                "payload": {
                    "line": {
                        "type": "text",
                        "text": "Hello"
                    }
                }
            },
            {
                "payload": {
                    'line': result

                }
            },
            {
                "payload": {
                    "line": {
                        "type": "location",
                        "title": "มาดิ",
                        "address": "แถวนี้แม่งเถื่อน",
                        "latitude": 16.2555,
                        "longitude": 100.33555
                    }
                }
            },
            {
                'payload': {
                    'line': {
                        "type": "template",
                        "altText": "this is a confirm template",
                        "template": {
                            "type": "confirm",
                            "actions": [
                                {
                                    "type": "message",
                                    "label": "Yes",
                                    "text": "Yes"
                                },
                                {
                                    "type": "message",
                                    "label": "No",
                                    "text": "No"
                                }
                            ],
                            "text": "ไปต่อหรือพอแค่นี้?"
                        }
                    }
                }
            }

        ]
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.jinja_env.auto_reload = True

    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
