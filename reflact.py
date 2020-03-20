# class Teacher():
#     def __init__(self,name):
#         self.name = name
#
#     def English(self):
#         setattr(self,'age',100)
#         print("哈哈")
#
# a = Teacher("张珊")
# a.English()
# def getname():
#     return "ee"
# newfunc = lambda: getname()
# setattr(self,"name",say)
# print(a.name)




class Neuralnetwork(nn.Module):
    def __init__(self, in_dim=70, n_hidden_1=10, n_hidden_2=10, out_dim=1):
        super(Neuralnetwork, self).__init__()
        self.Ti_forward = nn.Sequential(
            nn.Linear(in_dim, n_hidden_1),
            nn.Tanh(),
            nn.Linear(n_hidden_1, n_hidden_2),
            nn.Tanh(),
            nn.Linear(n_hidden_2, out_dim),
        )
        self.O_forward = nn.Sequential(
            nn.Linear(in_dim, n_hidden_1),
            nn.Tanh(),
            nn.Linear(n_hidden_1, n_hidden_2),
            nn.Tanh(),
            nn.Linear(n_hidden_2, out_dim),
        )

    def nomal_forward()
        return nn.Sequential(
            nn.Linear(in_dim, n_hidden_1),
            nn.Tanh(),
            nn.Linear(n_hidden_1, n_hidden_2),
            nn.Tanh(),
            nn.Linear(n_hidden_2, out_dim),
        )
    def forward(self, x, flag_list):
        out = []
        for k in range(x.size(0)):
            tmp = []
            for i, flag in enumerate(flag_list,0):
                if(hasattr(self,flag[k]+"_forward")):
                    tmp.append(getattr(self, flag[k] + "_forward")(x[k][i]))
                else:
                    #newfunc = lambda: nomal_forward()
                    setattr(self, flag[k]+"_forward", nomal_forward)
                    tmp.append(getattr(self, flag[k] + "_forward")(x[k][i]))

            out.append(torch.stack(tmp, 0).sum())
        return torch.stack(out, 0).view(x.size(0),1)