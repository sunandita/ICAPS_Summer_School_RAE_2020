__author__ = 'patras'

from ete3 import Tree, TreeStyle, TextFace, add_face_to_node

def DrawTree():
    y_old = ''
    count = 0
    while(True):
        f = open('pipefile', 'r')
        y = f.read()
        #y = "root;"
        #y = "((((NonEmergencyMove_Method1)MoveTo_Method1)Recharge_Method1,(NonEmergencyMove_Method1)MoveTo_Method1,((NonEmergencyMove_Method1)MoveTo_Method1,(((NonEmergencyMove_Method1)MoveTo_Method1)Recharge_Method2,(NonEmergencyMove_Method1)MoveTo_Method1,((NonEmergencyMove_Method1)MoveTo_Method1)Search_Method1)Search_Method2)Search_Method1)Search_Method2)Fetch_Method1;"
        #y = "((((a_1)b)c,(d)e,((f)g,(((h)i)j,(k)l,((m)n)o)p)q)r)s;"
        #y = "(((m,n)a,b,c),(a2, b2, c2))k;"
        f.close()
        if y != '' and y != y_old:
            t = Tree(y, format=1)
            ts = TreeStyle()
            ts.show_leaf_name = False
            def my_layout(node):
                F = TextFace(node.name, tight_text=True)
                add_face_to_node(F, node, column=0, position="branch-right")
            ts.layout_fn = my_layout
            #t.show(tree_style=ts)
            t.render("figures/RTree_{}.png".format(count), tree_style=ts)
            count += 1
        y_old = y

if __name__=="__main__":
    f = open('pipefile', 'w')
    f.close()
    DrawTree()