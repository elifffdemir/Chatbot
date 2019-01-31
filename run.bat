python -m rasa_nlu.train -c nlu_model_config.yml --fixed_model_name current --data data.json --path models\nlu
python train.py
python bot.py run
