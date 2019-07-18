
import os
import re
l_ann = os.listdir("Annotation/n04350905")
l_img = os.listdir("Images")

# l_ann = [re.match(r'n04350905_(\d*)\.xml', s).group(1) for s in l_ann]

l_ann_match = []
for s in l_ann:
    try:
        match = re.match(r'(.*_\d*)\.xml', s).group(1)
        if match is None:
            print("No match found for ",s)
        else:
            l_ann_match.append(match)
    except:
        print("couldnt match in ",s)

l_img_match = []
for s in l_img:
    try:
        match = re.match(r'(.*_\d*)\.JPEG', s).group(1)
        if match is None:
            print("No match found for ", s)
        else:
            l_img_match.append(match)
    except:
        print("couldnt match img in ", s)

l_intersection = list(set(l_ann_match) & set(l_img_match))

for x in l_ann:
    try:
        if re.match(r'(.*_\d*)\.xml', x).group(1) not in l_intersection:
            os.remove("Annotation/n04350905/{}".format(x))
    except:
        print("something bad happened in l_ann for ", x)

for x in l_img:
    try:
        if re.match(r'(.*_\d*)\.JPEG', x).group(1) not in l_intersection:
            os.remove("Images/{}".format(x))
    except:
        print("something bad happened in l_img for ", x)

