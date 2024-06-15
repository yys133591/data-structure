import random

class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

# 전역변수
memory = []
dataArray = list(random.sample(range(1, 101), 20))
root = None

# 메인 함수
if __name__ == "__main__":
    # 루트 노드 생성
    node = TreeNode()
    node.data = dataArray[0]
    root = node
    memory.append(node)

    # 나머지 노드 생성 및 트리에 삽입
    for randnum in dataArray[1:]:
        node = TreeNode()
        node.data = randnum
        current = root
        while True:
            if randnum < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right
        memory.append(node)

    # 추출된 데이터 출력

    findName = int(input('숫자를 입력하세요: '))
    print('추출된 데이터:', [node.data for node in memory])

    current = root
    while True:
        if findName == current.data:
            print(findName, '을(를) 찾았습니다.')
            print('추가된 이진 트리 데이터:', [node.data for node in memory])
            break
        elif findName < current.data:
            if current.left is None:
                print(findName, '을(를) 찾지 못했습니다.')
                node=TreeNode()
                node.data=findName
                current.left=node
                memory.append(node)
                break
            current = current.left
        else:
            if current.right is None:
                print(findName, '을(를) 찾지 못했습니다.')
                node=TreeNode()
                node.data=findName
                current.right=node
                memory.append(node)
                break
            current = current.right
    print('추가된 이진 트리 데이터:', [node.data for node in memory])
    
    