from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from policy.mobile_policy import MobilePolicy
from policy.attention_policy import AttentionPolicy
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.form_policy import FormPolicy
from rasa_core.policies.embedding_policy import EmbeddingPolicy
from rasa_core import config

logger = logging.getLogger(__name__)


def train_dialogue_keras(domain_file="mobile_domain.yml",
                   model_path="models/dialogue_keras",
                   training_data_file="data/mobile_edit_story.md"):

    fallback = FallbackPolicy(
        fallback_action_name="action_unknown_intent",
        nlu_threshold=0.7,
        core_threshold=0.3
    )
    
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=8),
                            MobilePolicy(epochs=100, batch_size=16, max_history=8),
                            FormPolicy(),
                            fallback])

    training_data = agent.load_data(training_data_file)
    agent.train(
            training_data,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_dialogue_embed(domain_file="mobile_domain.yml",
                   model_path="models/dialogue_embed",
                   training_data_file="data/mobile_edit_story.md"):

    fallback = FallbackPolicy(
        fallback_action_name="action_default_fallback",
        nlu_threshold=0.7,
        core_threshold=0.3
    )
    
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=5),
                            EmbeddingPolicy(epochs=100), fallback])

    training_data = agent.load_data(training_data_file)
    agent.train(
            training_data,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_dialogue_transformer(domain_file="mobile_domain.yml",
                               model_path="models/dialogue_transformer",
                               training_data_file="data/mobile_edit_story.md"):
    # 通过加载yml配置文件方式配置policy
    policies = config.load('./policy/attention_policy.yml')
    agent = Agent(domain_file,
                  policies=policies)

    training_data = agent.load_data(training_data_file)
    agent.train(
        training_data,
        validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data = load_data('data/rasa_dataset_training.json')
    trainer = Trainer(config.load("configs/nlu_embedding_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/',
                                      fixed_model_name="current")

    return model_directory


def train_nlu_gao():
    from rasa_nlu_gao.training_data import load_data
    from rasa_nlu_gao import config
    from rasa_nlu_gao.model import Trainer

    training_data = load_data('data/rasa_dataset_training.json')
    trainer = Trainer(config.load("configs/config_embedding_bilstm.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu_gao/',
                                      fixed_model_name="current")

    return model_directory


def train_nlu_elmo():
    from rasa_nlu_gao.training_data import load_data
    from rasa_nlu_gao import config
    from rasa_nlu_gao.model import Trainer

    training_data = load_data('data/rasa_dataset_training.json')
    trainer = Trainer(config.load("configs/elmo_model_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/elmo/',
                                      fixed_model_name="current")

    return model_directory


def train_nlu_wordvector():
    from rasa_nlu_gao.training_data import load_data
    from rasa_nlu_gao import config
    from rasa_nlu_gao.model import Trainer

    training_data = load_data('data/rasa_dataset_training.json')
    trainer = Trainer(config.load("configs/wordvector_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/wordvector/',
                                      fixed_model_name="current")

    return model_directory


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=["train-nlu", "train-dialogue-keras", "train-dialogue-embed", "train-nlu-gao", "train-nlu-elmo",
                     "train-dialogue-transformer", "train-nlu-wordvector"],
            help="what the bot should do ?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-nlu-gao":
        train_nlu_gao()
    elif task == "train-nlu-elmo":
        train_nlu_elmo()
    elif task == "train-nlu-wordvector":
        train_nlu_wordvector()
    elif task == "train-dialogue-keras":
        train_dialogue_keras()
    elif task == "train-dialogue-embed":
        train_dialogue_embed()
    elif task == "train-dialogue-transformer":
        train_dialogue_transformer()
