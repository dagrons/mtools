import os

import gdown

cls_model_path = os.path.join(os.path.dirname(__file__), "trained_models/malware_sim%doc2vec.pth")
if not os.path.exists(cls_model_path):
    gdown.download(url="https://drive.google.com/file/d/1R8JwkyJIk6zE2ADFF2Lys5zNPpOlBJah/view?usp=sharing",
                   output=cls_model_path,
                   fuzzy=True)


sim_model_path = os.path.join(os.path.dirname(__file__), 'trained_models/malware_classification%resnet34%best.pt')  # 要使用的模型字典地址
if not os.path.exists(sim_model_path):
    gdown.download(url="https://drive.google.com/file/d/1zFJebJ991tzqnYWsUdcaRaaAZ377y4Wg/view?usp=sharing",
                   fuzzy=True,
                   output=sim_model_path)


