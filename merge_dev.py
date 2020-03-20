import gc
import logging
import os

import numpy as np
import pandas as pd


from args import args

dev_list = []
# for epoch in range(8):
#     data_path = args.data_path + str(epoch)
#     dev_data_path = os.path.join(data_path, 'dev.csv')
#     tmp = pd.read_csv(dev_data_path)
#     dev_list.append(tmp)
# df = pd.DataFrame().append(dev_list)
# df.to_csv(os.path.join(args.raw_data_path, 'all_bert_dev.csv'),index=False)



# train_predic_bert = pd.read_csv(os.path.join(args.raw_data_path, 'all_bert_dev.csv'))
# train_predic_albert = pd.read_csv(os.path.join(args.raw_data_path, 'all_albert_dev.csv'))
# train_predic_roberta = pd.read_csv(os.path.join(args.raw_data_path, 'all_roberta_dev.csv'))
#
# train_predic_bert['bert'] = train_predic_bert['prediction']
# train_predic_bert['albert'] = train_predic_albert['prediction']
# train_predic_bert['roberta'] = train_predic_roberta['prediction']
# train_predic_bert.to_csv(os.path.join(args.raw_data_path, 'train_predic.csv'),index=False)
#
#
# test_predic_bert = pd.read_csv(os.path.join(args.raw_data_path, 'submit-bert.csv'))
# test_predic_albert = pd.read_csv(os.path.join(args.raw_data_path, 'submit-albert.csv'))
# test_predic_roberta = pd.read_csv(os.path.join(args.raw_data_path, 'submit-roberta.csv'))
#
# test_predic_bert['bert'] = test_predic_bert['y'] + 1
# test_predic_bert['albert'] = test_predic_albert['y'] + 1
# test_predic_bert['roberta'] = test_predic_roberta['y'] + 1
#
# test_predic_bert.to_csv(os.path.join(args.raw_data_path, 'test_predic.csv'),index=False)





# dev_list = []
# for epoch in range(args.epochs):
#     data_path = args.data_path + str(epoch)
#     dev_data_path = os.path.join(data_path, 'dev.csv')
#     tmp = pd.read_csv(dev_data_path)
#     dev_list.append(tmp)
# df = pd.DataFrame().append(dev_list)
# df.to_csv(os.path.join(args.raw_data_path, 'all_roberta_dev.csv'),index=False)



# train_predic_bert = pd.read_csv(os.path.join(args.raw_data_path, 'all_bert_dev.csv'))
# train_predic_albert = pd.read_csv(os.path.join(args.raw_data_path, 'all_albert_dev.csv'))
# train_predic_roberta = pd.read_csv(os.path.join(args.raw_data_path, 'all_roberta_dev.csv'))
#
# train_predic_bert['bert'] = train_predic_bert['prediction']
# train_predic_bert['albert'] = train_predic_albert['prediction']
# train_predic_bert['roberta'] = train_predic_roberta['prediction']
# train_predic_bert.to_csv(os.path.join(args.raw_data_path, 'train_predic.csv'),index=False)


# test_predic_bert = pd.read_csv(os.path.join(args.raw_data_path, 'submit-bert.csv'))
# test_predic_albert = pd.read_csv(os.path.join(args.raw_data_path, 'submit-albert.csv'))
# test_predic_roberta = pd.read_csv(os.path.join(args.raw_data_path, 'submit-roberta.csv'))
#
# test_predic_bert['bert'] = test_predic_bert['y'] + 1
# test_predic_bert['albert'] = test_predic_albert['y'] + 1
# test_predic_bert['roberta'] = test_predic_roberta['y'] + 1
#
# test_predic_bert.to_csv(os.path.join(args.raw_data_path, 'test_predic.csv'),index=False)


# def check(row,index):
#     if(row['bert'] == index ):
#         row[str(index)] += 1
#     # if (row['albert'] == index):
#     #     row[str(index)] += 1
#     if (row['roberta'] == index):
#         row[str(index)] += 1
# test_data = pd.read_csv(os.path.join(args.raw_data_path, 'test_predic.csv'))
# test_data['0'] = 0
# test_data['1'] = 0
# test_data['2'] = 0
#
# for index,row in test_data.iterrows():
#     check(row, 0)
#     check(row, 1)
#     check(row, 2)
# test_data['y'] = np.argmax(test_data[['0', '1', '2']].values, -1) - 1
# print(test_data)
# test_data[['id','y']].to_csv(os.path.join(args.raw_data_path, 'toupiao.csv'),index=False)


test_data = pd.read_csv(os.path.join(args.raw_data_path, 'submit-roberta.csv'))
test_data[['id','y']].to_csv(os.path.join(args.raw_data_path, 'submit-roberta.csv'),index=False)

#
#
# def check(row,index):
#     if(row['bert'] == index ):
#         row[str(index)] += 1
#     if (row['albert'] == index):
#         row[str(index)] += 1
#     if (row['roberta'] == index):
#         row[str(index)] += 1
# test_data = pd.read_csv(os.path.join(args.raw_data_path, 'submit729.csv'))
# test_data['bert'] = test_data['y']
# test_data['albert'] = pd.read_csv(os.path.join(args.raw_data_path, 'submit730.csv'))['y']
# test_data['roberta'] = pd.read_csv(os.path.join(args.raw_data_path, 'submit733.csv'))['y']
# test_data['-1'] = 0
# test_data['0'] = 0
# test_data['1'] = 0
#
# for index,row in test_data.iterrows():
#     check(row, -1)
#     check(row, 0)
#     check(row, 1)
# test_data['y'] = np.argmax(test_data[['-1', '0', '1']].values, -1) - 1
# print(test_data)
# test_data[['id','y']].to_csv(os.path.join(args.raw_data_path, 'toupiao.csv'),index=False)
#
#
#
