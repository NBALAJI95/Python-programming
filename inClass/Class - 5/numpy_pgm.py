import numpy as np

def main():
    ran_var = list()
    for i in range(10*10):
        ran_var.append(np.random.randint(0, 100))

    print(len(ran_var))
    a = np.array(ran_var)
    a = a.reshape(10,10)
    print(a)
    print('Min', a.min())
    print('Max', a.max())

if __name__ == '__main__':
    main()