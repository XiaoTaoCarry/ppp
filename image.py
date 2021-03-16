import math

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

