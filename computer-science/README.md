# 챕터 1 - 친한 친구와의 대화

특수한 상황에 의사소통 하기 위한 방법에 대한 내용으로 구성되어 있다. 여기서 처음 등장하는 것이 모스부호(Morse Code)이며, 모스부호는 짧은 신호인 점(Dot)과 비교적 긴 신호인 선(Dash)으로 이루어져 있다.

우리가 대화를 통해 주고 받는 언어를 음성 언어라고 하며, 이는 언어를 이해할 수 있는 누구나가 인지할 수 있는 일종의 부호이다. 어떠한 매체에 기록해서 소통을 할 수 있는데 이를 문자 언어 혹은 글이라고 한다. 그 외에 손 동작으로 주고 받을 수 있는 수화, 누군가의 대화를 빠르게 글로 옮겨 기록하기 위한 속기술 또는 약기술 등의 다양한 부호가 존재한다.

+) 모스 부호를 보는 순간 배우 톰 행크스가 주연으로 출연한 캐스트 어웨이의 한 장면이 떠올랐다. 이 영화를 간단히 요약하자면, FedEx에서 근무 중이던 톰 행크스(이하, 척 또는 척 놀란드)가 비행기를 통해 화물을 운송하던 중 예기치 못한 비행기 추락 사고로 인해 약 4년간 무인도에 갇혀 생존하는 영화이다.

이 영화에서는 척이 어두컴컴한 밤에 아주 멀리 보이는 배에 손전등으로 SOS 구조 신호를 전달하는 장면이 나오는데, 이때 사용한 부호가 모스 부호이다. 그 장면을 보면 불빛을 짧게 세 번 비춰 S(···)를 나타내고, 길게 세 번 비춰 O(---)를 나타내는 것을 알 수 있다. 이와 같이 책의 초반 내용은 여러 예시를 통해 이와 같이 다양한 부호가 존재하는 목적(부호는 소통하기 위한 하나의 약속)과 그 활용에 대해서 설명하는 것 같다.

# 챕터 2 - 부호와 조합

챕터 2에서는 모스 부호의 자세한 내용이 담겨있다. 모스 부호는 점과 선을 사용한다는 점에서 이진 부호라고 할 수 있으며, 2의 거듭제곱 수만큼의 문자를 표현할 수 있다. 

모스 부호로 많은 신호를 전달할 수 있지만, 점과 선에 규칙이 없기 때문에 신호를 받는 입장에서는 불리할 수 있다는 단점이 있다. 이와 같이 여러 개의 요소를 다양하게 조합하는 방식은 수학에서 조합론 또는 조합적 분석이라고 하며, 책의 내용을 통해 간접적으로 알 수 있다.

+) 조합론 또는 조합적 분석은 확률 및 통계에서 주로 사용하는 분석 방법론이긴 하나, 뒤에서 나올 것으로 예상되는 '0과 1로 어떻게 컴퓨터가 동작하는지'에 대한 원리를 이해하는데 큰 도움이 될 것으로 생각한다.

# 챕터 3 - 점자와 이진 부호

챕터 3에서는 모스 부호의 단점을 보완한 점자에 대해서 기록되어 있다. 점자는 시각장애를 가진 이들이 주로 사용하는 부호이며, 이 또한 이진 부호라는 속성을 지니고 있다. 

책에서 나온 내용과 마찬가지로 우리나라에서도 6점식 한글점자를 사용하고 있으며, 이를 통해 2<sup>6</sup>(64)개의 부호를 나타낼 수 있다. 또한, 64개의 부호들 중에서 많은 부호가 문맥에 따라 다른 의미로 사용되기도 한다. 대표적으로 숫자 1과 영어 a를 나타내는 점자를 예로 들 수 있다.

<img width="200" src="/images/01_1_or_a.png">

이와 같은 상황에서 점자의 의미를 다르게 하려면 시프트 부호와 이스케이프 부호를 사용하면 된다. 시프트(shift) 부호는 점자로 숫자를 나타내기 전에 '여기부터 숫자로 나타낼거야'와 같은 의미를 나타내는 부호이고, 이스케이프(escape) 부호는 '여기부터 소문자를 대문자로 나타낼거야'와 같은 의미를 나타내는 부호이다. 이들은 이진 부호로 문자를 표기할 때 공통적으로 사용된다.

+) 프로그래밍 또는 키보드를 통해 사용되는 시프트 부호와 이스케이프 부호는 점자로부터 유래되었다고 할 수 있다. 이 내용을 통해 어디까지가 시프트에 해당하는 부호이고, 이스케이프에 해당하는 부호인지와 이들의 필요성에 대해서 이해할 수 있을 것으로 생각한다.

# 챕터 4 - 전등을 분해해 봅시다.

모든 원자는 전자, 양자, 중성자로 구성되어 있으며, 전자가 다른 원자로 이동할 때 전기가 발생한다. 챕터 4에서는 전기에 대해서 주로 다뤘으며, 용어, 개념 등을 자세히 확인할 수 있다. 내용 자체는 길지만, 이는 결국 CPU를 비롯한 컴퓨터의 기본 동작 원리를 설명하기 위한 기초 내용이라고 할 수 있다. 책에서는 자세히 풀어서 설명되어 있으므로, 전기에 대한 지식이 없어도 충분히 이해할 수 있을 것이라 생각한다. 컴퓨터의 동작 원리를 파악하기 위해서는 전기에 대해서 깊게 알 필요는 없으나, 전기가 어떻게 발생하고, 전류와 전압 및 저항은 어떠한 관계에 있는지에 대해서는 알고 있으면 나중에 '이건 왜 도입된거지?'와 같은 의문이 발생할 때 큰 도움이 될 것으로 생각한다.
