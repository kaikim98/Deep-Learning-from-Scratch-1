import numpy as np


# %% Chapter 5 BackPropagation
# Chapter 5.4 Implement Simple Layer
# Chapter 5.4.1 Mul Layer


class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
        
    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y
        
        return out
    
    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x
        
        return dx, dy
    

apple = 100
apple_num = 2
tax = 1.1

#layers
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

# Forward Propagation
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)

print(price)

# %% Chapter 5.4.2 Add Layer
class AddLayer:
    def __init__(self):
        pass
    
    def forward(self, x, y):
        out = x+y
        return out
    
    def backward(self, dout):
        dx = dout*1
        dy = dout*1
        return dx, dy
    
    
apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 1.1

# Layers
mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_apple_orange_layer = AddLayer()
mul_tax_layer = MulLayer()

# Forward Propagation
apple_price = mul_apple_layer.forward(apple, apple_num)
orange_price = mul_orange_layer.forward(orange, orange_num)
all_price = add_apple_orange_layer.forward(apple_price, orange_price)
price = mul_tax_layer.forward(all_price, tax)

# Back Propagation
dprice = 1
dall_price, dtax = mul_tax_layer.backward(dprice)
dapple_price, dorange_price = add_apple_orange_layer.backward(dall_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print(price)
print(dapple_num, dapple, dorange, dorange_num, dtax)

# %% 5.5 Implement Activation Function Layer
# 5.5.1 ReLU Layer
class Relu:
    def __init__(self):
        self.mask = None
        
    def forward(self, x):
        self.mask = (x <=0)
        out = x.copy()
        out[self.mask] = 0
        
        return out
    
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        
        return dx
    
x = np.array([[1.0,-0.5], [-2.0,3.0]])
mask = (x<=0)
print(mask)

# %% 5.5.2 Sigmoid Layer
class Simgoid:
    def __init__(self):
        self.out = None
    
    def forward(self, x):
        out = 1/ (1+np.exp(-x))
        self.out = out
        
        return out
    
    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out
        return dx
    
# %% 5.6 Implement Affine/Softmax Layer
# 5.6.1 Affine Layer