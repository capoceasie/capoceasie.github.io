import os, skimage
from io import open

#CONFIG
DIMENSIONS = [250, 500, 1000, 2000]

#Retrieve article dirs
main_subs = os.listdir(".")
main_dirs = [s for s in main_subs if os.path.isdir(s)]
print(main_dirs)

#For each article dir ...
for d in main_dirs:
    
    ##Get all article block subdirs
    article_subs = os.listdir(d)
    article_dirs = [s for s in article_subs if os.path.isdir(d + "/" + s)]
    
    ##For all article block
    for dd in article_dirs:
        qdd = d + "/" + dd #qualified dir
        qdd_subs = os.listdir(qdd)
        qdd_images = [s for s in qdd_subs if not os.path.isdir(qdd + "/" + s)]
        qdd_images = [s for s in qdd_images if s.endswith(".jpg") or s.endswith(".png")]
        
        yml_gallery = "picture_path: " + qdd + "\npreview:\n"
        yml_gallery_pictures = []
        
        ##For each image in the block
        for img in qdd_images:
            qimg = qdd + "/" + img #qualified img
            sizes_folder = qdd + "/sizes"
            if not os.path.exists(sizes_folder):
                os.makedirs(sizes_folder)
            print(qimg)
            qimg_data = skimage.io.imread(qimg)
            qimg_width = qimg_data.shape[0]
            qimg_height = qimg_data.shape[1]
            
            yml_gallery_picture = "- filename: " + img.replace(".jpg", "").replace(".png", "") + "\n"
            yml_gallery_picture += "  original: " + img + "\n  thumbnail: " 
            
            #Define Thumbnail as first dimension
            dim = DIMENSIONS[0]
            resized_img_filename = None
            if qimg_width > qimg_height:
                resized_height = int(round(float(qimg_height) / float(qimg_width) * float(dim)))
                resized_img_filename = sizes_folder + "/" + img.replace(" ", "_") + "_" + str(dim) + "x" + str(resized_height) + ".jpg"
            else:
                resized_width = int(round(float(qimg_width) / float(qimg_height) * float(dim)))
                resized_img_filename = sizes_folder + "/" + img.replace(" ", "_") + "_" + str(resized_width) + "x" + str(dim) + ".jpg"
            yml_gallery_picture += resized_img_filename.replace(qdd + "/", "") + "\n  sizes:\n"
            
            for dim in DIMENSIONS:            
                #Landscape format 
                if qimg_width > qimg_height:
                    resized_height = int(round(float(qimg_height) / float(qimg_width) * float(dim)))
                    print((dim, resized_height))
                    qimg_data_resized = skimage.transform.resize(qimg_data, (dim, resized_height), anti_aliasing=True)
                    resized_img_filename = sizes_folder + "/" + img.replace(" ", "_") + "_" + str(dim) + "x" + str(resized_height) + ".jpg"
                    skimage.io.imsave(resized_img_filename, qimg_data_resized)
                    yml_gallery_picture += "  - " + resized_img_filename.replace(qdd + "/", "") + "\n"
                #Portrait format
                else:
                    resized_width = int(round(float(qimg_width) / float(qimg_height) * float(dim)))
                    print((resized_width, dim))
                    qimg_data_resized = skimage.transform.resize(qimg_data, (resized_width, dim), anti_aliasing=True)
                    resized_img_filename = sizes_folder + "/" + img.replace(" ", "_") + "_" + str(resized_width) + "x" + str(dim) + ".jpg"
                    skimage.io.imsave(resized_img_filename, qimg_data_resized)
                    yml_gallery_picture += "  - " + resized_img_filename.replace(qdd + "/", "") + "\n"
            yml_gallery_pictures.append(yml_gallery_picture)
        
        yml_gallery += yml_gallery_pictures[0].replace("- filename", "  filename")
        yml_gallery += "pictures:\n" + "".join(yml_gallery_pictures)
        
        if not os.path.exists("../../_data/galleries/" + d):
            os.makedirs("../../_data/galleries/" + d)
        with open("../../_data/galleries/" + qdd + ".yml", "w") as gallery_file:
            gallery_file.write(yml_gallery)