import os
import shutil


# 将一个文件夹中的所有文件（包括子文件夹），拷贝到另一个文件夹中，去除子文件夹。
def copyfile_to_onedir(srcpath, dstpath):
    # 遍历源文件夹，得到根目录，子目录和文件名列表
    for root, dirs, files in os.walk(srcpath, topdown=True):
        counter = 0
        # 获取文件名依次遍历
        for name in files:
            if os.path.exists(dstpath + '\\' + name):
                pass
            # 如果该文件在目标目录中已经存在，也就是重复文件，下面步骤给文件重命名，再进行拷贝。
            #     counter += 1
            #     # 获取文件名
            #     filename = name[0: name.rindex('.')]
            #     # 获取文件类型（后缀）
            #     filetype = name[name.rindex('.') + 1:]
            #     # 将文件名重命名后，拷贝到目标文件夹，注意，copy的两个参数都要是绝对路径的完整文件名
            #     shutil.copy(os.path.join(root, name), dstpath + '\\' + filename + str(counter) + '.' + filetype)
            else:
                # 如果该文件未重复，那就直接拷贝就好。
                shutil.copy(os.path.join(root, name), dstpath + '\\' + name)

copyfile_to_onedir('D:\HCC-VETC\VETC\TCGA_LIHC\TCGA-LIHC-pathology', "D:\HCC-VETC\VETC\TCGA_LIHC\TCGA-LIHC-pathology\slide_")