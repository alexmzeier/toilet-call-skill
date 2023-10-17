from va import MycroftSkill, intent_file_handler

from va.dataModel import UserSkillMetis

import requests

class ToiletCall(MycroftSkill):
    def __init__(self, skill_data: UserSkillMetis):
        MycroftSkill.__init__(self, skill_data=skill_data)

    @intent_file_handler('call.toilet.intent')
    def handle_call_toilet(self, message, websocket):
        self.speak('Ich habe das Personal benachrichtigt, dass Sie auf die Toilette müssen', websocket=websocket)


def create_skill(skill_data: UserSkillMetis):
    return ToiletCall(skill_data)

