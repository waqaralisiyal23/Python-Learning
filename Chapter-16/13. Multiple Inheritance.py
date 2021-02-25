# Multiple Inheritance

class A:
    def class_a_method(self):
        return 'I\' just a class A method'

    def hello(self):
        return 'Hello from class A'

class B:
    def class_b_method(self):
        return 'I\' just a class B method'

    def hello(self):
        return 'Hello from class B'

class C(A, B):
    pass

# instance_a = A()
# print(instance_a.class_a_method())

instance_c = C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c.hello())      # class A ka hello() method call hua, kiun iske liye C ka MRO dekho or A ka phle isliye hu rha kiun
# ke order mn A, B diya hai agr B, A dengy tou phle B mn search huga hello method

# print(help(C))
# print(C.mro())
# print(C.__mro__)
