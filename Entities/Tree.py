class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.children: list = []


class GeneralTree:
    def __init__(self) -> None:
        self.root: Node = None
        self.Tam = 0

    def add_child(self, parent, child, aux_Children=Node(), agregado=False):
        if parent is None:
            self.root = Node(child)
            return
        if agregado:
            return
        if len(self.root.children) == 0:
            self.root.children.append(Node(child))

        else:
            aux_Children = self.root
        for i in range(len(aux_Children.children)):
            if aux_Children.value == parent:
                aux_Children.children.append(Node(child))
                agregado = True
                return
            elif aux_Children.children[i].value == parent:
                self.add_child(parent, child, aux_Children=aux_Children.children[i], agregado=agregado)
            elif agregado:
                break