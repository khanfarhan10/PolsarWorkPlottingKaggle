import matplotlib.pyplot as plt
import json, os


ModelJsonPath = '/home/koireader/work/PolsarWorkPlottingKaggle/data/PSPNet_Keras_SegModels_resnet101_GeoDataEps100.json'
ModelName = 'PSPNet Resnet 101' # 'Fpn Densenet 201'
xlabel_size = 40
ylabel_size = 40
title_size = 40
legend_prop = {'size' : 40}
xtick_size = 30
ytick_size = 30

OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok = True)
# dict_to_save = new_dict

# new_dict = {}

# for k in dict_to_save:
# v = dict_to_save[k]
# new_arr = []
# for each in v:
# new_arr.append(float(each)) 
# new_dict[k] = new_arr


# with open(ModelName + '.json', 'w') as fp:
# json.dump(new_dict, fp)

with open(ModelJsonPath, 'r') as fp:
    new_dict = json.load(fp)

# Plot training & validation iou_score values
fig = plt.figure(figsize=(30, 8))
plt.subplot(121)
plt.plot(new_dict['iou_score'], linewidth = 5)
plt.plot(new_dict['val_iou_score'], linewidth = 5)
plt.title('Model IoU Score', fontsize = title_size, fontweight = 'bold')
plt.ylabel('IoU Score', fontsize = ylabel_size, fontweight = 'bold', labelpad = 12)
plt.yticks(fontsize = ytick_size)
plt.xlabel('Epoch', fontsize = xlabel_size, fontweight = 'bold')
plt.xticks(fontsize = xtick_size)
# plt.legend(['Train', 'Test'], loc='upper left')
plt.legend(['Train', 'Test'], loc='lower right', prop = legend_prop)


# Plot training & validation loss values
plt.subplot(122)
plt.plot(new_dict['loss'], linewidth = 5)
plt.plot(new_dict['val_loss'], linewidth = 5)
plt.title('Model Loss', fontsize = title_size, fontweight = 'bold')
plt.ylabel('Loss', fontsize = ylabel_size, fontweight = 'bold', labelpad = 12)
plt.yticks(fontsize = ytick_size)
plt.xlabel('Epoch', fontsize = xlabel_size, fontweight = 'bold')
plt.xticks(fontsize = xtick_size)
plt.legend(['Train', 'Test'], loc='lower right', prop = legend_prop)

plt.gcf().subplots_adjust(bottom=0.15)

# fig.tight_layout()

plt.savefig(os.path.join(OUTPUT_FOLDER, ModelName + '.png'),dpi = 600)
# plt.show()


# changing the fontsize of yticks
# plt.yticks(fontsize=20)

# plt.gcf().subplots_adjust(bottom=0.15)

# alternate option without .gcf
# plt.subplots_adjust(bottom=0.15)

# set the spacing between subplots

''' plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)
plt.show()'''

# set the spacing between subplots

'''plt.subplot_tool()
plt.show()'''

# Try both of these