import os
import numpy as np
import json

root = 'folder'
# this script will re-calculate xywh in every txt and json files in directory 'root'
for root, dirs, files in os.walk(root):
    for dir in files:
        if dir.endswith('.txt'):
            label = np.loadtxt(root + '/' + dir)

            temp = np.zeros([label.shape[0], 4])
            for idex, i in enumerate(label):
                xmin = np.min(i[5::2])
                xmax = np.max(i[5::2])
                ymin = np.min(i[6::2])
                ymax = np.max(i[6::2])
                label[idex][1] = (xmax + xmin) / 2
                label[idex][2] = (ymax + ymin) / 2
                label[idex][3] = (xmax - xmin)
                label[idex][4] = (ymax - ymin)
                temp[idex] = label[idex][1:5]
            np.savetxt(root + '/' + dir, label)
            print('finished transform ' + dir)

            try:
                with open(root + '/' + dir.replace('txt', 'json'), 'r', encoding='utf8') as fp:
                    label_dict = json.load(fp)
                    # print(label_dict['list'])
                    for idex,i in enumerate(label_dict['list']):
                        i['x'] = temp[idex][0]
                        i['y'] = temp[idex][1]
                        i['w'] = temp[idex][2]
                        i['h'] = temp[idex][3]

                    with open(root + '/' + dir.replace('txt', 'json'), 'w', encoding='utf8') as fp1:
                        json.dump(label_dict, fp1, indent=1)

                print('finished transform ' + dir.replace('txt', 'json'))
            except:
                print('warning: cant find json file relative')
                pass
