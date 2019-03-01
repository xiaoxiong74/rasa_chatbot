# Rasa Core and Rasa NLU

## Introduction
这个聊天机器人demo是用开源NLU框架rasa-nlu(https://github.com/RasaHQ/rasa_nlu/tree/master/rasa_nlu)完成意图识别与实体识别，用rasa-core(https://github.com/RasaHQ/rasa_core)完成对话管理和与对话生成。本demo完成的对话主要有
1：办理套餐、查询话费和流量(会话场景1)
2：案件查询(会话场景2)
3：Q&A问答+闲聊(会话场景3、4)
demo主要参考了 [_rasa_chatbot] https://github.com/GaoQ1/rasa_chatbot_cn/  及(https://github.com/zqhZY/_rasa_chatbot)。
```
rasa-nlu:      0.14.4
rasa-core:     0.13.2
rasa-core-sdk: 0.12.1
tensorflow     1.12.0
```

## Command
### train nlu model
```
python bot.py train-nlu   训练NLU模型
```
**total_word_feature_extractor.dat**可去https://pan.baidu.com/s/1-ma0ndXBWL0rnbUqCAcL-w ，密码：lhi4 下载。nlu_model_config.yml中的pipeline可自定义，这里由于数据量较少，用了开源的方法和词向量。如果你的rasa_dataset_training.json上数据足够多，可以尝试使用nlu_embedding_config.yml配置来训练nlu model.

### test nlu model
```
python -m rasa_nlu.server --path models/nlu   启动NUL模型服务

curl -XPOST 192.168.109.232:5000/parse -d '{"q":"我要查昨天下午的抢劫案", "project": "default", "model": "current"}'   
```


### train dialogue
```
python bot.py train-dialogue-keras
```

### test dialogue   client端：可在终端测试聊天效果
```
python -m rasa_core_sdk.endpoint --actions actions &

python -m rasa_core.run --nlu default/current --core models/dialogue_keras --endpoints endpoints.yml  开启core服务(Client)    

```

### dialogue 交互式训练生成新的story
```
python -m rasa_core.train interactive -o models/dialogue_keras -d mobile_domain.yml -s data/mobile_edit_story.md --endpoints endpoints.yml  重头开始训练story，零启动
python -m rasa_core.train interactive --core models/dialogue_keras  --nlu default/current --endpoints endpoints.yml  通过已有story模型训练(构造更多的story,一般用这种方法)
```

### provide dialogue service   Service端：提供对话服务接口
```
python -m rasa_core_sdk.endpoint --actions actions &

python -m rasa_core.run --nlu default/current --core models/dialogue_keras --credentials credentials.yml --endpoints endpoints.yml  开启core服务(Service) 
```

### compare policy
```
python -m rasa_core.train compare -c keras_policy.yml embed_policy.yml -d mobile_domain.yml -s data/mobile_edit_story.md -o comparison_models/ --runs 3 --percentages 0 25 50 70
```

### evaluate policy
```
python -m rasa_core.evaluate compare -s data/mobile_edit_story.md --core comparison_models/ -o comparison_results/
```

## Some tips
### auto generate rasa_dataset_training.json
data/rasa_dataset_training.json 是通过一些规则自动生成的，节省很多人力。仓库是[chatito_gen_nlu_data](https://github.com/GaoQ1/chatito_gen_nlu_data)
具体用法可参考[官方文档](https://rodrigopivi.github.io/Chatito/)
### UI界面介入
UI界面接入测试参考 https://github.com/howl-anderson/WeatherBot_UI 直接更改相应的端口或ip即可使用。
启动方法：
1、启动NLU服务
2、启动dialogue service 
3、启动web服务

期间有任何问题，欢迎随时issue！

## Some magical functions
[rasa-nlu-gao](https://github.com/GaoQ1/rasa_nlu_gq)新增了N多个个自定义组件，具体用法和说明请参考该作者的 [rasa对话系统踩坑记](https://www.jianshu.com/u/4b912e917c2e)，个人觉得对新入坑聊天机器人的童鞋很有帮助，感谢作者的贡献。简单使用方法。
### 首先需要下载rasa-nlu-gao
```
pip install rasa-nlu-gao
```
### 训练模型
```
python bot.py train-nlu-gao
```
### 测试使用模型
```
python -m rasa_nlu_gao.server -c config_embedding_bilstm.yml --path models/nlu_gao/
```
