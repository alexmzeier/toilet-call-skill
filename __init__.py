from mycroft import MycroftSkill, intent_file_handler


class ToiletCall(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('call.toilet.intent')
    def handle_call_toilet(self, message):
        self.speak_dialog('call.toilet')


def create_skill():
    return ToiletCall()

