from va import MycroftSkill, intent_handler
from va.adapt.intent import IntentBuilder
from va.skills.context import adds_context, removes_context
from va.dataModel import UserSkillMetis

import requests

def create_skill(skill_data: UserSkillMetis):
    return ToiletCall(skill_data)

class ToiletCall(MycroftSkill):
    def __init__(self, skill_data: UserSkillMetis):
        MycroftSkill.__init__(self, skill_data=skill_data)

    @intent_handler(IntentBuilder("ToiletHelperCall").require("toilet"))
    def handle_call(self, message, websocket):
        call_api = skill_api(self.skill_data.identifier, self.skill_data.api_key, message.data["utterance"])
        #print('result call api ' + call_api)
        self.speak('Ich habe das Personal benachrichtigt, dass Sie auf die Toilette müssen', websocket=websocket)

    #@intent_file_handler('call.toilet.intent')
    #def handle_call_toilet(self, message, websocket):
        #self.speak('Ich habe das Personal benachrichtigt, dass Sie auf die Toilette müssen', websocket=websocket)

def skill_api(identifier: str, api_key: str, text: str):
    print ('skill_api')
    #payload = {'customer_id' : data.customer_id, 'api_key': data.api_key}
    payload = {
        'identifier': identifier,
        'api_key': api_key,
        'utterance': text
    }
    #response = requests.get(url=skill.auth_skill_url, params=payload, json=dataRequest)
    response = requests.post(url="http://85.215.193.214:8001/api/skill/toilet-call", params=payload)
    print("request status code " + str(response.status_code))
    print('skills ' + str(response.text))
        
    if response.status_code == 200:
        #skill = add_skill_organistaion(user, data, db)                    
        return str(response.text)
    else:
        return None
