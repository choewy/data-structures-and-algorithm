# 챕터 10 - 논리와 스위치

한 줄 요약 : 챕터 10은 대수학과 논리연산의 연관성 및 논리연산의 원리를 아리스토텔레스의 삼단논법, 고양이, 전구 회로 등의 예시를 통해 설명하고 있다.

<p>
<details >
  <summary>
    <b>대수학과 부울 대수의 차이</b>
  </summary>
  <div style="margin: 10px 0;">
      <div>
          <table>
              <thead>
                  <tr>
                      <th>구분</th>
                      <th>피연산자</th>
                      <th>연산자</th>
                      <th>0의 의미</th>
                      <th>1의 의미</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>대수학</td>
                      <td>숫자</td>
                      <td>숫자들의 조합 방법을 결정함</td>
                      <td>숫자 0</td>
                      <td>숫자 1</td>
                  </tr>
                  <tr>
                      <td>부울 대수</td>
                      <td>종류(class)</td>
                      <td>종류들의 집합 관계를 결정함</td>
                      <td>공집합(empty set)</td>
                      <td>전체집합(universe)</td>
                  </tr>
              </tbody>
          </table>
      </div>
  </div>
</details>
</p>

<p>
<details >
  <summary>
    <b>수학의 법칙은 부울 대수에도 적용된다</b>
  </summary>
  <div style="margin: 10px 0;">
      <ul>
          <li>교환 법칙 : 덧셈 또는 곱셈의 피연산자들은 서로 교환 가능하며, 뺄셈과 나눗셈의 피연산자들은 서로 교환이 불가능하다.</li>
          <pre><code><span>A + B = B + A</span></code></pre>
          <li>결합 법칙 : 덧셈 또는 곱셈으로만 구성된 식의 경우 우선순위가 바뀌어도 그 결과는 같다.</li>
          <pre><code><span>A + (B + C) = (A + B) + c</span></code></pre>
          <li>배분 법칙 : 곱셈과 나눗셈 연산은 덧셈과 뺄셈 연산에 대하여 연산자를 배분할 수 있다.</li>
          <pre><code><span>A × (B + C) = (A × B) + (A × C)</span></code></pre>
      </ul>
  </div>
</details>
</p>

<p>
    <details >
      <summary>
        <b>논리곱과 논리합</b>
      </summary>
      <div style="margin: 10px 0;">
          <ul>
              <li>OR는 +, AND는 ×, NOT은 1-E을 의미한다.</li>
              <pre><code><span>A + B = A OR B = A 또는 B</span></code></pre>
              <pre><code><span>A × B = A AND B = A와 B</span></code></pre>
              <li>그리고, 문자를 조건에 따라 1(참)과 0(거짓)으로 대입하여 대수학의 연산 방식으로 연산하면 그 결과가 0 또는 1이 된다.</li>
              <p>수컷을 M, 암컷을 F, 흰색을 W라고 했을 때, 흰색 암컷 고양이는 다음과 같은 논리식으로 나타낼 수 있다.</p>
              <pre><code><span>F × W = 1 × 1 = 1</span></code></pre>
              <li>병렬 회로는 OR, 직렬 회로는 AND</li>
              <img width="400" src="/images/02_01_chapter10.png">
              <img width="400" src="/images/02_02_chapter10.png">
          </ul>
      </div>
    </details>
</p>

