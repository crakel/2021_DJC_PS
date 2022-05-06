import sys

tree = {}
con_1 = 0
con_2 = True
con_3 = True
case = 0

root = 0


def check_route(node, total_node):
    global cnt
    cnt += 1
    if cnt > total_node:
        return False
    elif tree[node] == 0:
        return True
    return check_route(tree[node], total_node)



while True:
    flag = False
    node = list(map(int, sys.stdin.readline().split()))
    if node:
        if node[-1] == -1 and node[-2] == -1:
            break

        for i in range(1, len(node), 2):
            if node[i] == 0 and node[i-1] == 0:
                flag = True
                break

            if node[i] in tree.keys() and tree[node[i]] != 0:
                con_2 = False

            if node[i-1] not in tree:
                tree[node[i-1]] = 0

            tree[node[i]] = node[i-1]

    if flag:
        #print(tree)
        case += 1
        for i, v in tree.items():
            cnt = 0
            if not check_route(i, len(tree)-1):
                print("con3")
                con_3 = False

            if v == 0:
                con_1 += 1
                root = i
            # else:
            #     con_3_value += 1

        if con_1 == 1:
            con_1 = True

        # if (len(tree) - 1) == con_3_value:
        #     con_3 = True

        # print(f'con_1 : {con_1}')
        # print(f'con_2 : {con_2}')
        # print(f'con_2 : {con_3}')

        # if len(set(tree.values())) == 1:
        #     if set(tree.values()).pop() == 0:
        #         print("hi")
        #         print(f'Case {case} is a tree.')

        if not con_1 or not con_2 or not con_3:
            print(f'Case {case} is not a tree.')


        else:
            print(f'Case {case} is tree.')

        tree = {}

# import sys
#
# input = sys.stdin.readline
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.child = None
#         self.parant = None
#
#     def __str__(self):
#         return str(self.data)
#
#
# def soluction():
#     def checkCycle(rootNode):
#         cnt = len(rootNode.child)
#         for i in rootNode.child:
#             cnt += checkCycle(node_dict[i])
#         return cnt
#
#     isInput = True
#     answer = True
#     node_dict = dict()
#     root = None
#     global isWorking
#
#     while isInput:
#         buf = input().rstrip().split("  ")
#         if buf[0] == '':
#             continue
#         for temp in buf:
#             a, b = map(int, temp.split(" "))
#             if a == 0 and b == 0:
#                 isInput = False
#                 break
#             elif a < 0 and b < 0:
#                 isWorking = False
#                 isInput = False
#                 break
#             # node를 딕셔너리에 저장한다.
#             if a in node_dict:
#                 node_dict[a].child.append(b)
#             else:
#                 node_dict[a] = Node(a)
#                 node_dict[a].child = [b]
#             if b in node_dict:
#                 # 부모가 2명(들어오는 간선의 수가 2개이면 안된다.)일 순 없다
#                 if node_dict[b].parant == None:
#                     node_dict[b].parant = a
#                 else:
#                     answer = False
#             else:
#                 node_dict[b] = Node(b)
#                 node_dict[b].parant = a
#                 node_dict[b].child = []
#     #  공배열도 트리이다.
#     if len(node_dict) == 0:
#         return True
#     if answer == False:
#         return answer
#     #  루트 노드 찾기 and 부모가 없는 노드가 2개이면 한개의 트리가 아니다.
#     for v in node_dict.values():
#         if v.parant == None:
#             if root == None:
#                 root = v.data
#             else:
#                 answer = False
#                 return answer
#     # 루트가 없어도 트리가 이나다.
#     if root == None:
#         return False
#
#     #  루트로부터 시작해서 모든 노드로 갈 수 있어야 한다.
#     cycle = 1 + len(node_dict[root].child)
#     for i in node_dict[root].child:
#         cycle += checkCycle(node_dict[i])
#     if cycle != len(node_dict):
#         return False
#     return answer
#
#
# if __name__ == "__main__":
#     isWorking = True
#     num = 1
#     while isWorking:
#         check = soluction()
#         if not isWorking:
#             break
#         if check:
#             string = "Case " + str(num) + " is a tree."
#             print(string)
#         else:
#             string = "Case " + str(num) + " is not a tree."
#             print(string)
#         num += 1