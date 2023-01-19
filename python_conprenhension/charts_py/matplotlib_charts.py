# %%
import matplotlib
#matplotlib.use
#matplotlib.get_backend()
import matplotlib.pyplot as plt

def generate_bar_chart():
    labels =['a','b','c']

    values = [100, 200, 300,]
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()
    plt.savefig('my.png')

def proub():
    plt.plot([1,2,3,4])
    
    plt.ylabel('some numbers') 
    plt.savefig('m.png')
    plt.show()

if __name__ == "__main__":
    generate_bar_chart()
    proub()

