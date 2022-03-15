# 큐(Queue)

큐는 FIFO(First-In-First-Out, 선입선출) 방식으로 줄 세우기라고 할 수 있다. 학창 시절(또는, 군대 시절) 때 급식실의 모습을 생각해보면 이해하기 쉬울 것이다. 먼저 줄 서서 식사를 마친 사람이 먼저 밖으로 나오는데, 큐는 먼저 입력한 데이터를 먼저 꺼내는 방식이다.

큐는 스택과 마찬가지로 요소를 컬렉션에 추가하거나 꺼내는 연산이 대표적인데, 각각 `enqueue`와 `dequeue`라고 하며, 스택의 `push`와 `pop`과는 차이가 있다. 또한, 스택의 경우 데이터가 쌓이는 구조로 `top`과 `bottom` 중 `top`에서만 데이터를 입력하고 꺼낼 수 있는 반면, 큐에서는 데이터를 입력하는 부분을 `back`이라고 하고, 데이터를 꺼내는 부분을 `front`라고 한다.

<div align="center">
    <img width="600" src="https://ww.namu.la/s/b7785ff70f623fedbcae126015a3ae0a18b2f3a785bdd691d803aad2b10aee91f7b3fc438aadd3676cb84b9608ac18c4ce4dcc9a35eed34a61a2ffffff9b56eb2690d1ecbc99f7aa87a3e5387dfb8c90">
    큐(출처 - 나무위키)
</div>