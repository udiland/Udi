import ete3

# load tree (newick format)
t = ete3.Tree("tree.newick", format=1)

# show tree
print(t)
print()
# write to file
# t.write(outfile="")


'''
When you load a tree you will be always placed at the root of the tree. You can
check that by typing:
'''

print(t.is_root())

'''
To go one node down in the tree structure, you need to
call the children.
'''

children = t.get_children()

'''
For a rooted tree and for any other bifurcating nodes,
there will be two children.
'''
print(len(children))

print(children[0])

print(children[1])

'''
You could now assign each child to a variable and search for their own
children (grandchildren).
'''

ch1, ch2 = children

grandchildren1 = ch1.get_children()

grandchildren2 = ch2.get_children()

print(grandchildren1[0])

print(grandchildren1[1])

print(grandchildren2[0])

print(grandchildren2[1])
print()
'''
To see whether one of the
nodes is a leaf you can use:
'''

print(grandchildren1[1].is_leaf())


'''We can also get a leaf by its name'''

leaf = t.get_leaves_by_name('Solyc04g015120.2')[0]

print(leaf)

'''To move up in the tree hierarchy we can simply:'''
parent = leaf.up
print(parent)

'''We can also go to the sister group'''
sister = leaf.get_sisters()[0]
print(sister)

'''We can search nodes that are the common ancestor of a set of leaves:'''

anc = t.get_common_ancestor('Solyc06g071740.1', 'Solyc03g112330.2')
print(anc)




'''Iter through the tree
The traverse function will allow you to go through each one of the tree
nodes in a given order.
'''

num = 1

for node in t.traverse():
    if node.is_leaf():
        print(num, node.name)
        num += 1
print()

# diferent strategy (will give the leaves in order)
num = 1
for node in t.traverse(strategy='postorder'):
    if node.is_leaf():
        print(num, node.name)


'''
Iter through leaves
If you only want to go through each leave, you can use these two options:
'''

for leaf in t.iter_leaves():
    print(leaf)
print()


# You can also go through the leaf names:
for leaf in t.iter_leaf_names():
    print(leaf)
print()

'''Check whether a set of leaves are monophyletic'''

results = t.check_monophyly(['Solyc06g071740.1', 'Solyc06g071730.2', 'Solyc01g090210.2'], "name")
'''
This function outputs:
1.- Whether the leaf names provided form a monophyletic
clade (values True / False)
2.- Which relationship they have (monophyletic or
polyphyletic)
3.- The set of leaf names that break the monophyly'''

print(results)


'''
Add features to nodes

Additional information can be added to nodes by adding features. Imagine
that in our example tree, we want to annotate whether the leaf is a vowel:
'''
t = ete3.Tree('((I,H),((G,(F,(E,D))),((C,(B,A)),J)));', format=1)
print(t)

for leaf in t.iter_leaves():
    if leaf.name == "A" or leaf.name == "I":
        leaf.add_feature("vowel", True)
    else:
        leaf.add_feature("vowel",False)

'''We can access this new feature in the same way we access the normal
attributes. '''

print(leaf.name)
print(leaf.vowel)

# Once created an attribute can also be modified:

leaf.vowel = "Something Else"
print(leaf.vowel)

#You can also create multiple features at the same time
for leaf in t.iter_leaves():
    leaf.add_features(feature1=0, feature2=[])

# To know which features are assigned to your node, you can simply:
for leaf in t.iter_leaves():
    print(leaf.features)


'''
Tree visualization
How to visualize a tree and print it to a file:
'''
#
# t.show()
#
# # You can print the image in different formats by using the render function:
# # t.render("image.pdf") # this will save the tree to the working directory
#
# '''
# Tree style
# To change the visualization format of a tree, you first need to create a tree style,
# that will be applied to the tree:
# '''
# t = ete3.Tree("tree.newick", format=1)
#
# ts = ete3.TreeStyle()
#
# # The tree style controls the main visualization features of the tree. for example:
# # ts.show_leaf_name=True
# # ts.show_branch_length=False
# # ts.show_branch_support=False
#
# # t.show(tree_style=ts)
#
# # Other things the tree style can control:
# ts.mode="c"
# ts.arc_span=180
# ts.arc_start=-180
# ts.title.add_face(ete3.TextFace("Exampole", fsize=20), column=0)
#
# # t.show(tree_style=ts)

'''
Node faces
Faces can be used to add additional information to the trees

To add faces to a tree, you first need to create a Face object and then you need to
add it to one or several nodes in the tree (can be internal nodes or leaves).
Here are the main kinds of faces (this assumes you have exported the
Faces module from ete3: from ete3 export Faces):
'''

from ete3 import Tree, TreeStyle, TextFace
t = Tree( "((a,b),c);" )

# Basic tree style
ts = TreeStyle()
# ts.show_leaf_name = True

# Add two text faces to different columns
t.add_face(TextFace("hola "), column=0, position = "branch-right")
t.add_face(TextFace("mundo!"), column=1, position = "branch-right")
# t.show(tree_style=ts)
print(t)