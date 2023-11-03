from rest_framework.response import Response
from rest_framework.decorators import api_view

import sys
dir = "C:\\Users\\user\\Desktop\\drive-download-20230614T063836Z-001\\djangoMidi\\sqlite_database"
sys.path.append(dir)
import sport_recommand 

dir = "C:\\Users\\user\\Desktop\\drive-download-20230614T063836Z-001\\djangoMidi\\paimon"
sys.path.append(dir)
import paimon

@api_view(['GET'])
def form(request):
    
    name = request.GET.get("name")
    height = request.GET.get("height")
    weight = request.GET.get("weight")
    target = request.GET.get("target")
    status = request.GET.get("status")
    #uid = request.GET.get("uid")
    
    # 轉成英文
    i_height = int(height)
    i_weight = int(weight)
    i_target = int(target)
    print(name)
    print(height)
    print(weight)
    print(target)
    print(status)
    #print(uid)
    # name,height,weight,target,status,uid
    sport = sport_recommand.total_output(name,i_height,i_weight,i_target,status)
    
   

    sp0 = "推薦跑步時數公里數: " + str(sport[0])
    sp1 = "推薦走路步數: "+ str(sport[1])
    datas = {
        "feeding":
            [
                {
                    "img_src": "1.png",
                    "title": "跑步",
                    "content": sp0
                },
                {
                    "img_src": "2.png",
                    "title": "運動種類",
                    "content": sp1
                    
                }
            ]
    }
    return Response(datas)


@api_view(['GET'])
def chat(request):
    # 要換成post要解決前後端分離的csrf-token問題
    uid = request.GET.get("uid")
    message = request.GET.get("message")
    chat = paimon.chatbot_output(message)
    #print(type(chat))
    datas = {
        
        "uid": "pymon",
        "message": chat
    }
    # a = call pymon bot
    # 回傳格式:
    # {
    #        "uid":"pymon",
    #        "message":"油膩豬陀";
    # }
    return Response(datas)
