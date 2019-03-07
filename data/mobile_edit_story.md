## Generated Story No1
* greet
    - utter_greet
* deny
    - utter_goodbye

## Generated Story No2
* greet
    - utter_greet
* goodbye
    - utter_goodbye

## Generated Story No3
* greet
    - utter_greet
* thanks
    - utter_thanks

## Generated Story No4
* greet
    - utter_greet
* unknown_intent
    - action_unknown_intent
* unknown_intent
    - action_unknown_intent
* goodbye
    - utter_goodbye

## Generated Story No5
* greet
    - utter_greet
* request_search{"item": "\u8bdd\u8d39"}
    - slot{"item": "\u8bdd\u8d39"}
    - utter_ask_time
* inform{"time": "\u4e09\u6708"}
    - slot{"time": "\u4e09\u6708"}
    - utter_confirm
* confirm
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye


## Generated Story No6
* greet
    - utter_greet
* request_search{"item": "\u6d41\u91cf", "time": "\u4e09\u6708"}
    - slot{"item": "\u6d41\u91cf"}
    - slot{"time": "\u4e09\u6708"}
    - utter_confirm
* confirm
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye


## Generated Story No7
* greet
    - utter_greet
* request_management{"package": "\u5957\u9910"}
    - slot{"package": "\u5957\u9910"}
    - utter_ask_package
* inform{"package": "\u5957\u9910\u4e00"}
    - slot{"package": "\u5957\u9910\u4e00"}
    - utter_confirm
* confirm
    - utter_ack_management
    - utter_ask_morehelp
* deny
    - utter_goodbye
* thanks
    - utter_thanks

## Generated Story No8
* greet
    - utter_greet
* request_management{"package": "\u5957\u9910"}
    - slot{"package": "\u5957\u9910"}
    - utter_ask_package
* inform{"package": "\u5957\u9910\u4e00"}
    - slot{"package": "\u5957\u9910\u4e00"}
    - utter_confirm
* confirm
    - utter_ack_management
    - utter_ask_morehelp
* request_search{"item": "\u6d41\u91cf", "time": "\u4e09\u6708"}
    - slot{"item": "\u6d41\u91cf"}
    - slot{"time": "\u4e09\u6708"}
    - utter_confirm
* confirm
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye

## Generated Story No9
* greet
    - utter_greet
* request_management{"package": "\u5957\u9910"}
    - slot{"package": "\u5957\u9910"}
    - utter_ask_package
* request_search{"item": "\u6d41\u91cf", "time": "\u4e09\u6708"}
    - slot{"item": "\u6d41\u91cf"}
    - slot{"time": "\u4e09\u6708"}
    - utter_confirm
* confirm
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye

## Generated Story No10
* greet
    - utter_greet
* request_management{"package": "\u5957\u9910"}
    - slot{"package": "\u5957\u9910"}
    - utter_ask_package
* request_search{"item": "\u6d41\u91cf"}
    - slot{"item": "\u6d41\u91cf"}
    - utter_ask_time
* inform{"time": "\u4e09\u6708"}
    - slot{"time": "\u4e09\u6708"}
    - utter_confirm
* confirm
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye
    
## Generated Story No11
* unknown_intent
    - action_unknown_intent
    
## Generated Story No12
* greet
    - utter_greet
* request_search{"item": "\u6d41\u91cf", "number": 10.0, "duration": 10.0, "time": "2019-10-01T00:00:00.000Z"}
    - slot{"item": "\u6d41\u91cf"}
    - slot{"time": "2019-10-01T00:00:00.000Z"}
    - utter_confirm
* confirm
    - action_search_consume
    - utter_ask_morehelp
* unknown_intent
    - action_unknown_intent
    - action_restart

## Generated Story No13
* unknown_intent
    - action_unknown_intent
* request_search{"item": "\u6d41\u91cf"}
    - slot{"item": "\u6d41\u91cf"}
    - utter_ask_time
* inform_time{"number": "4.0", "duration": "4.0", "time": "2019-04-01T00:00:00.000Z"}
    - slot{"time": "2019-04-01T00:00:00.000Z"}
    - utter_confirm
* confirm
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye

## Generated Story No14
* greet
    - utter_greet
* request_search{"item": "\u6d41\u91cf"}
    - slot{"item": "\u6d41\u91cf"}
    - utter_ask_time
* inform_time{"number": "6.0", "duration": "6.0", "time": "2019-06-01T00:00:00.000Z"}
    - slot{"time": "2019-06-01T00:00:00.000Z"}
    - utter_confirm
* confirm
    - action_search_consume
    - utter_ask_morehelp
* unknown_intent
    - action_unknown_intent

## Generated Story No15
* request_search{"item": "\u6d41\u91cf"}
    - slot{"item": "\u6d41\u91cf"}
    - utter_ask_time
* request_search{"item": "\u8bdd\u8d39"}
    - slot{"item": "\u8bdd\u8d39"}
    - utter_ask_time
* inform_time{"number": "6.0", "duration": "6.0", "time": "2019-06-01T00:00:00.000Z"}
    - slot{"time": "2019-06-01T00:00:00.000Z"}
    - utter_confirm
* confirm
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye

## Generated Story No16
* greet
    - utter_greet
* searchCases{"day": "3 \u6708 5 \u53f7", "place": "\u5eb7\u5e84", "case": "\u6740\u4eba\u6848", "number": 5.0, "duration": 3.0, "time": {"from": "2019-03-05T12:00:00.000Z", "to": "2019-03-05T19:00:00.000Z"}}
    - slot{"time": {"from": "2019-03-05T12:00:00.000Z", "to": "2019-03-05T19:00:00.000Z"}}
    - case_form
    - form{"name": "case_form"}
    - slot{"case": "\u6740\u4eba\u6848"}
    - slot{"place": "\u5eb7\u5e84"}
    - slot{"day": "3 \u6708 5 \u53f7"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_morehelp
* deny

## Generated Story No17
* searchCases{"case": "\u6740\u4eba\u6848"}
    - slot{"case": "\u6740\u4eba\u6848"}
    - utter_ask_place
* inform_case{"place": "\u5927 \u9f99\u5c71"}
    - slot{"place": "\u5927 \u9f99\u5c71"}
    - utter_ask_casetime
* inform_case{"day": "\u524d\u5929", "time": {"from": "2019-02-26T12:00:00.000Z", "to": "2019-02-26T19:00:00.000Z"}}
    - slot{"day": "\u524d\u5929"}
    - slot{"time": {"from": "2019-02-26T12:00:00.000Z", "to": "2019-02-26T19:00:00.000Z"}}
    - case_form
    - form{"name": "case_form"}
    - slot{"day": "\u524d\u5929"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_morehelp
* deny

## Generated Story No18
* greet
    - utter_greet
* searchCases{"case": "\u6848\u5b50"}
    - slot{"case": "\u6848\u5b50"}
    - utter_ask_casetime
* inform_case{"day": "\u6628\u5929\u665a\u4e0a"}
    - slot{"day": "\u6628\u5929\u665a\u4e0a"}
    - utter_ask_place
* inform_case{"place": "\u7ea2\u65d7 \u6cb3\u6c9f"}
    - slot{"place": "\u7ea2\u65d7 \u6cb3\u6c9f"}
    - case_form
    - form{"name": "case_form"}
    - slot{"place": "\u7ea2\u65d7 \u6cb3\u6c9f"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_morehelp
* deny
    - utter_goodbye

## Generated Story No19
* greet
    - utter_greet
* searchCases{"day": "\u524d\u5929", "case": "\u6740\u4eba\u6848", "time": {"from": "2019-02-26T12:00:00.000Z", "to": "2019-02-26T19:00:00.000Z"}}
    - slot{"case": "\u6740\u4eba\u6848"}
    - slot{"day": "\u524d\u5929"}
    - slot{"time": {"from": "2019-02-26T12:00:00.000Z", "to": "2019-02-26T19:00:00.000Z"}}
    - utter_ask_place
* inform_case{"place": "\u5eb7\u5e84"}
    - slot{"place": "\u5eb7\u5e84"}
    - case_form
    - form{"name": "case_form"}
    - slot{"place": "\u5eb7\u5e84"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_morehelp
* deny
    - utter_goodbye

## Generated Story No20
* greet
    - utter_greet
* searchCases{"place": "\u5149\u7535 \u56ed", "case": "\u62a2\u52ab\u6848"}
    - slot{"case": "\u62a2\u52ab\u6848"}
    - slot{"place": "\u5149\u7535 \u56ed"}
    - utter_ask_casetime
* inform_case{"day": "\u4e0a\u5468 \u4e00", "number": 1.0, "time": {"from": "2019-02-25T18:00:00.000Z", "to": "2019-02-26T00:00:00.000Z"}}
    - slot{"day": "\u4e0a\u5468 \u4e00"}
    - slot{"time": {"from": "2019-02-25T18:00:00.000Z", "to": "2019-02-26T00:00:00.000Z"}}
    - case_form
    - form{"name": "case_form"}
    - slot{"day": "\u4e0a\u5468 \u4e00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_morehelp
* deny
    - utter_goodbye
    
## Generated Story No21
* searchCases{"case": "\u6740\u4eba\u6848"}
    - slot{"case": "\u6740\u4eba\u6848"}
    - utter_ask_place
* inform_case{"place": "\u671d\u5929\u95e8"}
    - slot{"place": "\u671d\u5929\u95e8"}
    - utter_ask_casetime
* inform_case{"day": "3 \u6708 1 \u65e5", "number": 1.0, "duration": 3.0, "time": "2019-03-01T00:00:00.000Z"}
    - slot{"day": "3 \u6708 1 \u65e5"}
    - slot{"time": "2019-03-01T00:00:00.000Z"}
    - case_form
    - form{"name": "case_form"}
    - slot{"day": "3 \u6708 1 \u65e5"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_morehelp
* deny
    - utter_goodbye
    
## Generated Story No22
* request_search{"item": "\u6d41\u91cf"}
    - slot{"item": "\u6d41\u91cf"}
    - utter_ask_time
* inform_case{"number": 6.0, "duration": 6.0, "time": "2019-06-01T00:00:00.000Z"}
    - slot{"time": "2019-06-01T00:00:00.000Z"}
    - utter_confirm
* confirm
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye

## Generated Story No23    
* unknown_intent
    - action_unknown_intent
* searchCases{"case": "\u62a2\u52ab\u6848"}
    - slot{"case": "\u62a2\u52ab\u6848"}
    - utter_ask_place
* inform_case{"place": "\u7ea2\u65d7 \u6cb3\u6c9f"}
    - slot{"place": "\u7ea2\u65d7 \u6cb3\u6c9f"}
    - utter_ask_casetime
* inform_case{"day": "\u4e0a\u5468\u4e94", "number": 5.0, "time": {"from": "2019-03-01T12:00:00.000Z", "to": "2019-03-01T19:00:00.000Z"}}
    - slot{"day": "\u4e0a\u5468\u4e94"}
    - slot{"time": {"from": "2019-03-01T12:00:00.000Z", "to": "2019-03-01T19:00:00.000Z"}}
    - case_form
    - form{"name": "case_form"}
    - slot{"day": "\u4e0a\u5468\u4e94"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_morehelp
* searchCases{"day": "\u524d\u5929", "case": "\u6740\u4eba\u6848", "time": {"from": "2019-03-03T18:00:00.000Z", "to": "2019-03-04T00:00:00.000Z"}}
    - slot{"case": "\u6740\u4eba\u6848"}
    - slot{"day": "\u524d\u5929"}
    - slot{"time": {"from": "2019-03-03T18:00:00.000Z", "to": "2019-03-04T00:00:00.000Z"}}
    - utter_ask_place
* inform_case{"place": "\u4e5d\u66f2\u6cb3", "number": "9.0", "time": "2019-03-05T09:00:00.000Z"}
    - slot{"place": "\u4e5d\u66f2\u6cb3"}
    - slot{"time": "2019-03-05T09:00:00.000Z"}
    - case_form
    - form{"name": "case_form"}
    - slot{"place": "\u4e5d\u66f2\u6cb3"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_morehelp
* unknown_intent{"place": "\u91cd\u5e86", "time": "2019-03-05T00:00:00.000Z"}
    - slot{"place": "\u91cd\u5e86"}
    - slot{"time": "2019-03-05T00:00:00.000Z"}
    - action_unknown_intent

## Generated Story No24
* searchCases{"case": "\u6848\u5b50"}
    - slot{"case": "\u6848\u5b50"}
    - utter_ask_place
* unknown_intent{"place": "\u5317\u789a"}
    - slot{"place": "\u5317\u789a"}
    - utter_ask_time
* inform_case{"day": "18 \u5e74 1 \u6708 9 \u65e5", "number": 9.0, "duration": 1.0, "time": "2020-01-09T00:00:00.000Z"}
    - slot{"day": "18 \u5e74 1 \u6708 9 \u65e5"}
    - slot{"time": "2020-01-09T00:00:00.000Z"}
    - case_form
    - form{"name": "case_form"}
    - slot{"day": "18 \u5e74 1 \u6708 9 \u65e5"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_morehelp
* searchCases{"place": "\u5927 \u9f99\u5c71", "case": "\u62a2\u52ab\u6848"}
    - slot{"case": "\u62a2\u52ab\u6848"}
    - slot{"place": "\u5927 \u9f99\u5c71"}
    - utter_ask_casetime
* inform_case{"day": "\u524d\u5929", "time": "2019-03-04T00:00:00.000Z"}
    - slot{"day": "\u524d\u5929"}
    - slot{"time": "2019-03-04T00:00:00.000Z"}
    - case_form
    - form{"name": "case_form"}
    - slot{"day": "\u524d\u5929"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_morehelp
* unknown_intent
    - action_unknown_intent
* unknown_intent
    - action_unknown_intent
* deny{"nr": "\u54c8"}
    - utter_goodbye