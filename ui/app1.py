import math


import os
import prof_check
import check_msg
import random

import logs

from nltk import sent_tokenize
import json

import msg_handle

messages=['fg','dg','dc']
from flask import jsonify
        
        
         


def reply(msg):
   
    classify_action_return =check_msg.classify_action(msg,messages[len(messages)-1],messages[len(messages)-2])
    
    if classify_action_return==False:
        classify_multiple_return=check_msg.check_multiple_option(msg,messages[len(messages)-1])

        if classify_multiple_return==False:
            classify_yes_or_no_in_option=check_msg.check_yes_or_no_in_option(msg,messages[len(messages)-1])
            if classify_yes_or_no_in_option==False:
                classify_yes_no_return=check_msg.check_yes_or_no(msg,messages[len(messages)-1])

                if classify_yes_no_return ==False:
                    classify_query_return=check_msg.classify_query_(msg)
                    if classify_query_return ==False:
                        classify_chatter_return=check_msg.check_chatterbot(msg)
                        if classify_chatter_return==False:
                            profcheck=prof_check.check_prof(msg)
                            if profcheck==False:
                                print("profcheck")
                                reply = msg_handle.message_handle(msg)
                            else:
                                print("profcheck")
                                reply = profcheck    
                        else:
                            print("classify_chatter_return")
                            reply = classify_chatter_return
                    else:
                        print("classify_query_return")
                        reply = classify_query_return
                else:
                    print("classify_yes_no_return")
                    reply = classify_yes_no_return
            else:
                print("classify_yes_or_no_in_option")
                reply = classify_yes_or_no_in_option

        else:
            print("classify_multiple_return")
            reply = classify_multiple_return
    else:
        print("classify_action_return")
        reply = classify_action_return
    
    
    messages.append(reply)
   
    return  reply



    


