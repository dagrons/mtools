import os

import gdown

cls_model_folder = os.path.join(os.path.dirname(__file__), "trained_models")
cls_model_path = os.path.join(cls_model_folder, 'malware_classification%resnet34%best.pt')
if not os.path.exists(cls_model_folder):
    os.mkdir(cls_model_folder)
if not os.path.exists(cls_model_path):
    gdown.download(url="https://drive.google.com/file/d/1zFJebJ991tzqnYWsUdcaRaaAZ377y4Wg/view?usp=sharing",
                   fuzzy=True,
                   output=cls_model_path)

sim_model_folder = os.path.join(os.path.dirname(__file__), 'trained_models')
sim_model_path = os.path.join(sim_model_folder,  'malware_sim%doc2vec.pth')  # 要使用的模型字典地址
if not os.path.exists(sim_model_folder):
    os.mkdir(sim_model_folder)
if not os.path.exists(sim_model_path):
    gdown.download(url="https://drive.google.com/file/d/1R8JwkyJIk6zE2ADFF2Lys5zNPpOlBJah/view?usp=sharing",
                   output=sim_model_path,
                   fuzzy=True)



