from PIL import Image
import sys
import os

if __name__ == '__main__':
        infp = sys.argv[1]
        files = os.listdir(infp)
        outfolder = sys.argv[2]
        outfp = os.path.join(infp, outfolder)
        try:
            os.mkdir(path = outfp)
        except FileExistsError as e:
            print('Output folder already exists')


        images = list()

        for file in files:
            tempfp = os.path.join(infp,file)
            if os.path.isfile(tempfp) and file.endswith('.jpg'):
                images.append(tempfp)

        converted_images = list()

        for image in images:
            img = Image.open(image)
            head_tail = os.path.split(image)
            filename_extension = head_tail[1]
            filename, extension = filename_extension.split('.')
            tempfp = outfp+filename+'.png'
            img.save(tempfp,format='png')















