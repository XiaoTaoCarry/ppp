import math
import numpy as np
from scipy import integrate


class RGBImage:
    """
    a template for image objects in RGB color spaces

    pixels: a 3-dimensional matrix, where pixels[c][i][j] indicates the intensity value in channel c at position (i, j). 
    """

    def __init__(self, pixels):
        """
        initializes a RGBImage instance and necessary instance variables
        """
        # YOUR CODE GOES HERE #
        self.pixels = pixels  # initialze the pixels list here
        row = len(pixels[0])
        col = len(pixels[0][0])
        self._size = (row,col)

    def size(self):
        """
        returns the size of the image
        """
        # YOUR CODE GOES HERE #
        return self._size

    def get_pixels(self):
        """
        returns a DEEP COPY of the pixels
        """
        # YOUR CODE GOES HERE #
        ret = []
        row, col = self.size()
        for i in range(3):
            ti = []
            for j in range(row):
                tj = []
                for k in range(col):
                    tj.append(self.pixels[i][j][k])
                ti.append(tj)
            ret.append(ti)
        return ret            


    def copy(self):
        """
        create a new RGBImage instance using a deep copy of the pixels matrix (you can utilize the get_pixels function) and return this new instance
        """
        # YOUR CODE GOES HERE #
        pixels = self.get_pixels()
        return RGBImage(pixels)

    def get_pixel(self, row, col):
        """
        returns the color of the pixel at position (row, col)
        """
        # YOUR CODE GOES HERE #
        assert row >= 0 and col >= 0
        
        sz = self.size()
        assert row < sz[0] and col < sz[1]

        return (self.pixels[0][row][col],self.pixels[1][row][col],self.pixels[2][row][col])

    def set_pixel(self, row, col, new_color):
        """
        A setter method that updates the color of the pixel at position (row, col) to the new_color in place. The argument new_color is a 3-element tuple (red intensity, green intensity, blue intensity). However, if any color intensity in this tuple is provided as -1, you should not update the intensity at the corresponding channel
        """
        # YOUR CODE GOES HERE #
        if -1 in new_color:
            return

        assert row >= 0 and col >= 0
        
        sz = self.size()
        assert row < sz[0] and col < sz[1]

        for i in range(3):
            self.pixels[i][row][col] = new_color[i]

class GreyImage:

    def __init__(self, pixels):
        """
        initializes a RGBImage instance and necessary instance variables
        """
        # YOUR CODE GOES HERE #
        self.pixels = pixels  # initialze the pixels list here
        row = len(pixels)
        col = len(pixels[0])
        self._size = (row,col)

    def size(self):
        """
        returns the size of the image
        """
        # YOUR CODE GOES HERE #
        return self._size

    def get_pixels(self):
        """
        returns a DEEP COPY of the pixels
        """
        # YOUR CODE GOES HERE #
        ret = []
        row, col = self.size()
        for j in range(row):
            tj = []
            for k in range(col):
                tj.append(self.pixels[j][k])
            ret.append(tj)
        return ret            


    def copy(self):
        """
        create a new RGBImage instance using a deep copy of the pixels matrix (you can utilize the get_pixels function) and return this new instance
        """
        # YOUR CODE GOES HERE #
        pixels = self.get_pixels()
        return RGBImage(pixels)

    def get_pixel(self, row, col):
        """
        returns the color of the pixel at position (row, col)
        """
        # YOUR CODE GOES HERE #
        assert row >= 0 and col >= 0
        
        sz = self.size()
        assert row < sz[0] and col < sz[1]

        return self.pixels[row][col]

    def set_pixel(self, row, col, new_color):
        """
        A setter method that updates the color of the pixel at position (row, col) to the new_color in place. The argument new_color is a 3-element tuple (red intensity, green intensity, blue intensity). However, if any color intensity in this tuple is provided as -1, you should not update the intensity at the corresponding channel
        """
        # YOUR CODE GOES HERE #
        if -1 in new_color:
            return

        assert row >= 0 and col >= 0
        
        sz = self.size()
        assert row < sz[0] and col < sz[1]

        self.pixels[row][col] = new_color

    def to_rgb(self):
        new_pixel = [self.get_pixels()] * 3
        return RGBImage(new_pixel)

def lorenz(p,t,s,r,b):
    x,y,z = p.tolist()          #无质量点的当前位置(x,y,z)
    return s*(y-x),x*(r-z)-y,x*y-b*z #返回dx/dt,dy/dt,dz/dt


# Part 2: Image Processing Methods #
class ImageProcessing:

    @staticmethod
    def arnold_encode(image, shuffle_times=1, key=(1,1)):
        """
        returns the negative image of the given image
        """
        a,b = key
        # choose N
        h, w = image.size()
        N = h   # 或N=w

        # Create a new pixel matrix
        new_pixels = [[0]*h for _ in range(w)] 
        old_pixels = image.get_pixels()

        
        # process
        for time in range(shuffle_times):
            new_pixels = [[0]*h for _ in range(w)]
            for ori_x in range(h):
                for ori_y in range(w):
                    new_x = (1*ori_x + b*ori_y)% N
                    new_y = (a*ori_x + (a*b+1)*ori_y) % N
                    
                    new_pixels[new_x][new_y] = old_pixels[ori_x][ori_y]
            old_pixels = new_pixels

        return GreyImage(new_pixels)

    @staticmethod
    def arnold_decode(image, shuffle_times=1, key=(1,1)):

        a,b = key
        # choose N
        h, w = image.size()
        N = h   # 或N=w

        # Create a new pixel matrix
        new_pixels = [[0]*h for _ in range(w)]
        old_pixels = image.get_pixels()

        for time in range(shuffle_times):
            new_pixels = [[0]*h for _ in range(w)]
            for ori_x in range(h):
                for ori_y in range(w):
                    new_x = ((a*b+1)*ori_x + (-b)* ori_y)% N
                    new_y = ((-a)*ori_x + ori_y) % N

                    new_pixels[new_x][new_y] = old_pixels[ori_x][ori_y]
            old_pixels = new_pixels

        return GreyImage(new_pixels)

    @staticmethod
    def grayscale(image):
        """
        converts the given image to grayscale
        """
        s = image.get_pixels()
        rows, cols = image.size()
        d = [[(s[0][i][j]+s[1][i][j]+s[2][i][j])//3 for j in range(cols)] for i in range(rows)]
        return GreyImage(d)

    @staticmethod
    def xor_key(image, key=1):
        # choose N
        h, w = image.size()
        N = h   # 或N=w

        # Create a new pixel matrix
        new_pixels = [[0]*h for _ in range(w)]
        old_pixels = image.get_pixels()

        for x in range(h):
            for y in range(w):

                new_pixels[x][y] = old_pixels[x][y] ^ key

        return GreyImage(new_pixels)


    @staticmethod
    def lorenz_trans(image, m=1, init=(1.1840,1.3627,1.2519)):
        rows,cols = image.size()
        n = rows * cols

        t = np.arange(0,(n+99)//100,0.01)
        track= integrate.odeint(lorenz,init,t,args=(10,28,2.6))
        factor = 10**m
        X = [t[0] for t in track]
        Y = [t[1] for t in track]
        Z = [t[2] for t in track]
        X = [factor*v - round(factor*v) for v in X]
        Y = [factor*v - round(factor*v) for v in Y]
        Z = [factor*v - round(factor*v) for v in Z]
        track = [X[:n],Y[:n],Z[:n]]             # re-organize the matrix

        # 第三步
        # 3.1 转成1维
        pixels_ori = image.get_pixels()
        temp = []
        for t in pixels_ori:
            temp.extend(t)
        pixels_ori = temp                

        # 3.2 置换
        for X in track:
            # 1. 获取下标
            X = [(i,v) for i,v in enumerate(X)]
            # 2. 根据值排序
            X.sort(key=lambda a: a[1])
            # 3. 获得置换
            X = [i for i,v in X]
            # 4. 执行置换
            pixels_new = [0] * n
            for i in range(n):
                pixels_new[i] = pixels_ori[X[i]]
            pixels_ori = pixels_new
        
        # TODO: 第4步和第5步都未对图片做任何修改
        # 第4步
        # 4.1  生成bx, by, bz序列
        X = [t[0] for t in track]
        Y = [t[1] for t in track]
        Z = [t[2] for t in track]
        track = [X[:n],Y[:n],Z[:n]]             # re-organize the matrix
        bs = []
        for x in track:
            b = [0] * (n+1)
            for i in range(n//3):
                t = 10**m * x[i] - round(10**m * x[i])
                t = abs(t)
                t = t * 10**15
                if i==0:
                    t = t + 127             # plus M[-1]
                else:
                    t = t + pixels_ori[3*i-1]
                t = round(t)
                t = t % 256
                b[x[i]] = t
        
        # 第5步
        e = [0] * n 
        for i  in range(n//3):
            e[3*i] = pixels_ori

        # 转回2维
        pixels_new = [pixels_new[i*cols:(i+1)*cols] for i in range(rows)]
        return GreyImage(pixels=pixels_new)

    @staticmethod
    def lorenz_trans_reverse(image, m=1, init=(1.1840,1.3627,1.2519)):
        rows,cols = image.size()
        n = rows * cols

        t = np.arange(0,(n+99)//100,0.01)
        track= integrate.odeint(lorenz,init,t,args=(10,28,2.6))
        factor = 10**m
        X = [t[0] for t in track]
        X = [factor*v - round(factor*v) for v in X]
        Y = [t[1] for t in track]
        Y = [factor*v - round(factor*v) for v in Y]
        Z = [t[2] for t in track]
        Z = [factor*v - round(factor*v) for v in Z]
        track = [Z[:n],Y[:n],X[:n]]             # re-organize the matrix

        pixels_ori = image.get_pixels()
        temp = []
        for t in pixels_ori:
            temp.extend(t)
        pixels_ori = temp                # 转成1维

        for X in track:
            # 1. 获取下标
            X = [(i,v) for i,v in enumerate(X)]
            # 2. 根据值排序
            X.sort(key=lambda a: a[1])
            # 3. 获得置换
            X = [i for i,v in X]
            # 4. 执行逆置换
            pixels_new = [0] * n
            for i in range(n):
                pixels_new[X[i]] = pixels_ori[i]
            pixels_ori = pixels_new
        
        # 转回2维
        pixels_new = [pixels_new[i*cols:(i+1)*cols] for i in range(rows)]
        return GreyImage(pixels=pixels_new)