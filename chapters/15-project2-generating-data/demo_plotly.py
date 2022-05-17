import plotly.graph_objects as go
import numpy as np

# np.random.seed(1)  # Forces randomization to return the same results

N = 70
my_x = (70 * np.random.randn(N))
my_y = (55 * np.random.randn(N))
my_z = (40 * np.random.randn(N))

print('Types my_x, my_y , my_z:', type(my_x), type(my_y), type(my_z))

my_data = go.Mesh3d(x=my_x, y=my_y, z=my_z, opacity=0.5,
                    color='rgba(244,22,100,0.6)'
                    )

print(my_data)
print('Type of my_data (GO Object): ', type(my_data))

fig = go.Figure(data=my_data)

fig.update_layout(
    scene=dict(
        xaxis=dict(nticks=4, range=[-100, 100], ),
        yaxis=dict(nticks=4, range=[-50, 100], ),
        zaxis=dict(nticks=4, range=[-100, 100], ), ),
    width=700,
    margin=dict(r=20, l=10, b=10, t=10))

fig.show()
