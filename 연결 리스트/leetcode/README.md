# leetcode

## ✔ [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

### 내용

정렬된 두 개의 연결 리스트의 노드를 결합하여 다음 그림과 같이 하나의 정렬된 연결 리스트로 병합하여야 한다.

문제에서 주어진 예시(`list1 = [1, 2, 4]`, `list2 = [1, 3, 4]`)를 그림으로 나타내면 다음과 같다.

<imgs width="600" src="/images/0_0_current.png" />

이 둘은 노드의 값을 기준으로 오름차순으로 정렬되어 있으며, 가장 왼쪽에 있는 노드가 각 연결 리스트의 head라고 할 수 있다. 그렇다면, 임시 노드를 생성하여 head로 정해놓고, 주어진 연결 리스트 2개의 노드 값을 비교한 결과에 따라 임시 노드 뒤에 연결시키면 되지 않을까라는 생각으로 문제에 접근해았다. 코드를 작성하기 전에 이 로직을 그림과 설명으로 나타내보면 다음과 같다.

+) 코드에 남긴 주석과 함께 보면 훨씬 더 직관적으로 이해할 수 있을 것이다.

#### 0. 새로운 연결 리스트의 head 역할을 수행할 Dummy 노드를 생성한다(이 리스트의 현재 노드를 current라고 명명하였다).

<imgs width="600" src="/images/0_1_dummy.png" />

#### 1. 입력받은 list1와 list2의 현재 노드를 각각 node1, node2로 하고, 이들의 값을 비교한다. 그 결과, 값이 동일하므로 `current의 자식 노드(current.next)`를 node2로 연결 및 이동(`current = current = next`)시키고, `node2는 다음 자식 노드(node2.next)`를 호출한다.

<imgs width="600" src="/images/1_link.png" />

#### 2. node2가 존재하므로 다시 node1과 node2의 값을 비교한다. 그 결과, node1의 값이 더 작으므로 `current의 자식 노드(current.next)`를 node1로 연결 및 이동시키고, `node1는 다음 자식 노드(node1.next)`를 호출한다.

<imgs width="600" src="/images/2_link.png" />

#### 3. node1이 존재하므로 다시 node1과 node2의 값을 비교한다. 그 결과, node1의 값이 더 작으므로 `current의 자식 노드(current.next)`를 node1로 연결 및 이동시키고, `node1는 다음 자식 노드(node1.next)`를 호출한다.

<imgs width="600" src="/images/3_link.png" />

#### 4. node1이 존재하므로 다시 node1과 node2의 값을 비교한다. 그 결과, node2의 값이 더 작으므로 `current의 자식 노드(current.next)`를 node2로 연결 및 이동시키고,`node2는 다음 자식 노드(node2.next)`를 호출한다.

<imgs width="600" src="/images/4_link.png" />

#### 5. node2가 존재하므로 다시 node1과 node2의 값을 비교한다. 그 결과, 이 둘의 값이 동일하므로 `current의 자식 노드(current.next)`를 node1로 연결 및 이동시키고,`node1는 다음 자식 노드(node1.next)`를 호출한다.

<imgs width="600" src="/images/5_link.png" />

+) 본 내용은 leetcode에서 제공한 그림(아래 참고)을 토대로 작성하였기 때문에 `그림 1`과 `그림 5`가 헷갈릴 수도 있다. 결론만 말하자면, 두 개의 노드 값이 동일한 경우 node1, node2 중 아무거나 선택해도 무방하다.

<imgs width="600" src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" />

#### 6. node1이 존재하지 않으므로 비교를 종료하고, `current의 자식 노드(current.next)`를 node2로 연결 및 이동시키고,`node2는 다음 자식 노드(node2.next)`를 호출한다.

<imgs width="600" src="/images/6_link.png" />

#### 7. 새롭게 재구성된 연결 리스트의 head는 제외하고 반환하여야 문제에서 원하는 답을 얻을 수 있으므로, `head의 자식 노드(head.next`를 최종 결과로 반환한다.

<imgs width="600" src="/images/7_link.png" />

### 참고자료

- [코딩 테스트, 정렬된 리스트 합치기](https://www.youtube.com/watch?v=kYzjk6xYAYg)

## ✔ [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

### 내용

연결 리스트의 `head`가 입력으로 주어지며, 해당 연결 리스트가 팰린드롬인 경우 `True`를 아닐 경우는 `False`를 반환하여야 한다.

```python

```