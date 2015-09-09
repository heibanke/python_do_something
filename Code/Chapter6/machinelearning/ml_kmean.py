# -*- coding: utf-8 -*-
# https://github.com/ZeevG/python-dominant-image-colour
# commented by heibanke

from PIL import Image
import random
import numpy

class Cluster(object):
    """
    pixels: 主要颜色所依据的像素点
    centroid: 主要颜色的RGB值
    """
    def __init__(self):
        self.pixels = []
        self.centroid = None

    def addPoint(self, pixel):
        self.pixels.append(pixel)

    def setNewCentroid(self):
        """
        通过pixels均值重新计算主要颜色
        """
        R = [colour[0] for colour in self.pixels]
        G = [colour[1] for colour in self.pixels]
        B = [colour[2] for colour in self.pixels]

        R = sum(R) / len(R)
        G = sum(G) / len(G)
        B = sum(B) / len(B)

        self.centroid = (R, G, B)
        self.pixels = []

        return self.centroid


class Kmeans(object):

    def __init__(self, k=3, max_iterations=5, min_distance=5.0, size=400):
        """
        k: 主要颜色的分类个数
        max_iterations: 最大迭代次数
        min_distance: 当新的颜色和老颜色的距离小于该最小距离时，提前终止迭代
        size: 用于计算的图像大小
        """
        self.k = k
        self.max_iterations = max_iterations
        self.min_distance = min_distance
        self.size = (size, size)

    def run(self, image):
        self.image = image
        #生成缩略图，节省运算量
        self.image.thumbnail(self.size)
        self.pixels = numpy.array(image.getdata(), dtype=numpy.uint8)
        self.clusters = [None]*self.k
        self.oldClusters = None
        #在图像中随机选择k个像素作为初始主要颜色
        randomPixels = random.sample(self.pixels, self.k)

        for idx in range(self.k):
            self.clusters[idx] = Cluster()
            self.clusters[idx].centroid = randomPixels[idx]

        iterations = 0

        #开始迭代
        while self.shouldExit(iterations) is False:
            self.oldClusters = [cluster.centroid for cluster in self.clusters]
            print iterations

            #对pixel和self.clusters中的主要颜色分别计算距离，将pixel加入到离它最近的主要颜色所在的cluster中
            for pixel in self.pixels:
                self.assignClusters(pixel)
            #对每个cluster中的pixels，重新计算新的主要颜色
            for cluster in self.clusters:
                cluster.setNewCentroid()

            iterations += 1

        return [cluster.centroid for cluster in self.clusters]

    def assignClusters(self, pixel):
        shortest = float('Inf')
        for cluster in self.clusters:
            distance = self.calcDistance(cluster.centroid, pixel)
            if distance < shortest:
                shortest = distance
                nearest = cluster
        nearest.addPoint(pixel)

    def calcDistance(self, a, b):
        result = numpy.sqrt(sum((a - b) ** 2))
        return result

    def shouldExit(self, iterations):

        if self.oldClusters is None:
            return False
        #计算新的中心和老的中心之间的距离
        for idx in range(self.k):
            dist = self.calcDistance(
                numpy.array(self.clusters[idx].centroid),
                numpy.array(self.oldClusters[idx])
            )
            if dist < self.min_distance:
                return True

        if iterations <= self.max_iterations:
            return False

        return True

    # The remaining methods are used for debugging
    def showImage(self):
        """
        显示原始图像
        """
        self.image.show()

    def showCentroidColours(self):
        """
        显示主要颜色
        """
        for cluster in self.clusters:
            image = Image.new("RGB", (200, 200), cluster.centroid)
            image.show()

    def showClustering(self):
        """
        将原始图像的像素完全替换为主要颜色后的效果
        """
        localPixels = [None] * len(self.image.getdata())

        for idx, pixel in enumerate(self.pixels):
                shortest = float('Inf')
                for cluster in self.clusters:
                    distance = self.calcDistance(
                        cluster.centroid,
                        pixel
                    )
                    if distance < shortest:
                        shortest = distance
                        nearest = cluster

                localPixels[idx] = nearest.centroid

        w, h = self.image.size
        localPixels = numpy.asarray(localPixels)\
            .astype('uint8')\
            .reshape((h, w, 3))

        colourMap = Image.fromarray(localPixels)
        return colourMap
    
if __name__=="__main__":
    from PIL import Image
    import os
    
    k_image=Kmeans(k=3) #默认参数
    path = './pics/'
    fp = open('file_color.txt','w')
    for filename in os.listdir(path):
        print path+filename
        try:
            color = k_image.run(Image.open(path+filename))
            w_image = k_image.showClustering()
            w_image.save(path+'mean_'+filename,'jpeg')
            fp.write('The color of '+filename+' is '+str(color)+'\n')
        except:
            print "This file format is not support"
    fp.close()