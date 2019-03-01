from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
from tests.qachat import get_qa
from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT

support_search = ["话费", "流量"]


def extract_item(item):
    if item is None:
        return None
    for name in support_search:
        if name in item:
            return name
    return None


def get_response(msg):
    key = '02703d8281304352a359bf1900e2058e'
    api = 'http://www.tuling123.com/openapi/api?key={}&info={}'.format(key, msg)
    return requests.get(api).json()


class ActionSearchConsume(Action):
    def name(self):
        return 'action_search_consume'

    def run(self, dispatcher, tracker, domain):
        item = tracker.get_slot("item")
        item = extract_item(item)
        if item is None:
            dispatcher.utter_message("您好，我现在只会查话费和流量")
            dispatcher.utter_message("你可以这样问我：“帮我查话费”")
            return []

        time = tracker.get_slot("time")
        if time is None:
            dispatcher.utter_message("您想查询哪个月的消费？")
            return []
        # query database here using item and time as key. but you may normalize time format first.
        dispatcher.utter_message("好，请稍等")
        if item == "流量":
            dispatcher.utter_message(
                "您好，您{}共使用{}二百八十兆，剩余三十兆。".format(time, item))
        else:
            dispatcher.utter_message("您好，您{}共消费二十八元。".format(time))
        return []


class ActionUnknowIntent(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self):
        return 'action_unknown_intent'
 
    def run(self, dispatcher, tracker, domain):
        # from rasa_core.events import UserUtteranceReverted
        # text = tracker.latest_message.get('text')
        # qa_message = get_qa(text)
        # if qa_message != "未找到答案":
        #     dispatcher.utter_message("{}".format(qa_message))
        # else:
        #     dispatcher.utter_template('utter_default', tracker, silent_fail=True)
        # return []

        text = tracker.latest_message.get('text')
        qa_message = get_qa(text)

        if qa_message != "未找到答案":
            dispatcher.utter_message("{}".format(qa_message))
        else:
            message = get_response(text)
            if message['code'] == 100000 or message['code'] == 200000:
                dispatcher.utter_message("{}".format(message['text']))
            else:
                dispatcher.utter_template('utter_default', tracker, silent_fail=True)
        return []

        # return [UserUtteranceReverted()]


class CaseForm(FormAction):
    """A custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""
        return "case_form"

    @staticmethod
    def required_slots(tracker):
        # type: () -> List[Text]
        """A list of required slots that the form has to fill"""
        return ["case", "place", "day"]

    def slot_mappings(self):
        return {"case": self.from_entity(entity="case", not_intent="unknown_intent"),
                "place": [self.from_entity(entity="place", intent=["inform_case", "searchCases"]),
                          self.from_text(intent="inform_case")],
                "day": [self.from_entity(entity="day", intent=["inform_case", "searchCases"]),
                        self.from_text(intent="inform_case")]
                }

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        """Define what the form has to do
            after all required slots are filled"""
        # utter submit template
        dispatcher.utter_template('utter_search_template', tracker)
        # slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        # slot_values.update(self.extract_requested_slot(dispatcher,
        #                                                tracker, domain))
        dispatcher.utter_message("{},在{}发生一起性质恶劣的{},引起全市人民的高度关注，以下是详细信息："
                                 .format(tracker.get_slot("day"), tracker.get_slot("place"), tracker.get_slot("case")))
        return []
